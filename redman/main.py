# -*- coding=utf-8 -*-
from shutil import which
from typing import Optional

import click
from click.core import Context
from texttable import Texttable

from color import Color
from redman_history import add_history, load_history
from redmanrc import (create_config_file_default_if_not_exists,
                      edit_config_file, load_config)
from redmine_api import (IssueStatus, UserStatus, list_issues, list_projects,
                         list_users, show_issue, show_user)
from sh_fzf import fzf


class Help:
    REDMINE_NAME = "redmine name. not project name. see your \"~/.redmanrc\". setup use \"redman config\". "
    ISSUE_STATUS = "choose from \"open\", \"close\", \"all\". default \"open\"."


REDMAN_COMMAND = "redman" if which("redman") else "python -m redman"


@click.group(invoke_without_command=True)
@click.pass_context
def redman(context: Context) -> None:
    if context.invoked_subcommand is None:
        history()


################################
# helper
################################
@redman.command()
def history() -> None:
    history_list = load_history()
    if not history_list:
        issues()
        return

    history_list.reverse()
    for history in history_list:
        if history.count("\t") == 3:
            redmine_name, status, project_id, user_id = history.split("\t")
            break

    issues(redmine_name if redmine_name else None,
           status if status else "open",
           project_id if project_id else None,
           user_id if user_id else None)


@redman.command()
def config() -> None:
    create_config_file_default_if_not_exists()

    edit_config_file()


################################
# projects
################################
@redman.command()
@click.option("--redmine_name", "-n", help=Help.REDMINE_NAME)
def projects(redmine_name: Optional[str]) -> None:

    url, api_key = load_config(redmine_name)
    if not url or not api_key:
        print("invalidate config")
        return

    body, err = list_projects(url, api_key)
    if err:
        print(err.reason)
        return

    projects = body.get("projects")
    if len(projects) <= 0:
        print("no project")
        return

    rows = [[
        "ID", "IDENTIFIER", "NAME", "DESCRIPTION",
    ]]
    rows.extend([[
        project.get("id"),
        project.get("identifier"),
        project.get("name"),
        project.get("description"),
    ] for project in projects])

    table = Texttable()
    table.set_deco(Texttable.HEADER | Texttable.VLINES)
    table.add_rows(rows)

    fzf(table.draw(),
        f"--bind=\"enter:abort+execute({REDMAN_COMMAND} issues --project_id={{1}} --redmine_name={redmine_name or ''} | more > /dev/tty)\"")


################################
# users
################################
@redman.command()
@click.option("--redmine_name", "-n", help=Help.REDMINE_NAME)
def users(redmine_name: Optional[str]) -> None:

    url, api_key = load_config(redmine_name)
    if not url or not api_key:
        print("invalidate config")
        return

    body, err = list_users(url, api_key)
    if err:
        print(err.reason)
        return

    users = body.get("users")
    if len(users) <= 0:
        print("no user")
        return

    rows = [[
        "ID", "LOGIN_ID", "NAME", "MAIL", "ADMIN", "LAST_LOGIN_ON",
    ]]
    rows.extend([[
        user.get("id"),
        user.get("login"),
        user.get("lastname") + " " + user.get("firstname"),
        user.get("mail"),
        "YES" if user.get("admin") else "",
        user.get("last_login_on"),
    ] for user in users])

    table = Texttable()
    table.set_deco(Texttable.HEADER | Texttable.VLINES)
    table.add_rows(rows)

    fzf(table.draw(),
        f"--preview=\"redman show user {{1}} --redmine_name={redmine_name or ''}\" \
          --bind=\"enter:abort+execute({REDMAN_COMMAND} issues --user_id={{1}} --redmine_name={redmine_name or ''} | more > /dev/tty)\"")


################################
# issues
################################
@redman.command()
@click.option("--redmine_name", "-n", help=Help.REDMINE_NAME)
@click.option("--status", "-s", type=click.Choice(["open", "close", "all"]), default="open", help=Help.ISSUE_STATUS)
@click.option("--project_id", "-p", type=str)
@click.option("--user_id", "-u", type=str)
def issues(redmine_name: Optional[str], status: str, project_id: Optional[str], user_id: Optional[str]) -> None:

    url, api_key = load_config(redmine_name)
    if not url or not api_key:
        print("invalidate config")
        return

    body, err = list_issues(url, api_key, IssueStatus.value_of(status), project_id, user_id)
    if err:
        print(err.reason)
        return

    issues = body.get("issues")
    if len(issues) <= 0:
        print("no issue")
        return

    rows = [[
        "ID", "TRACKER", "STATUS", "PRIORITY", "SUBJECT", "ASSIGNED", "DUE_DATE", "DESCRIPTION"
    ]]

    rows.extend([[
        issue.get("id"),
        issue.get("tracker").get("name"),
        issue.get("status").get("name"),
        issue.get("priority").get("name"),
        issue.get("subject"),
        issue.get("assigned_to", {}).get("name"),
        issue.get("due_date"),
        issue.get("description").replace("\n", " "),
    ] for issue in issues])

    table = Texttable(max_width=0)
    table.set_deco(Texttable.HEADER | Texttable.VLINES)
    table.add_rows(rows)

    stdin = table.draw()
    result = fzf(stdin,
                 f"--preview=\"{REDMAN_COMMAND} show issue {{1}} --redmine_name={redmine_name or ''}\"")
    if not result:
        return

    result = result.strip()

    add_history(redmine_name, status, project_id, user_id)

    for i, row in enumerate(stdin.splitlines()):
        row = row.strip()
        if row == result:
            print(f"""#{issues[i - 2].get("id")} {issues[i - 2].get("subject")}""")
            return


################################
# show
################################
@click.group()
def show() -> None:
    pass


@show.command()
@click.argument("id", type=str)
@click.option("--redmine_name", "-n", help=Help.REDMINE_NAME)
def user(id: str, redmine_name: Optional[str]) -> None:

    url, api_key = load_config(redmine_name)
    if not url or not api_key:
        print("invalidate config")
        return

    body, err = show_user(url, api_key, id)
    if err:
        print(err.reason)
        return

    user = body.get("user")
    preview = f"""{Color.背景緑} {Color.RESET} {user.get("lastname") + " " + user.get("firstname")}

{Color.灰}status     {Color.RESET}: {UserStatus.value_of(user.get("status")).name}
{Color.灰}login_id   {Color.RESET}: {user.get("login")}
{Color.灰}mail       {Color.RESET}: {user.get("mail")}
{Color.灰}api_key    {Color.RESET}: {user.get("api_key")}
{Color.灰}last_login {Color.RESET}: {user.get("last_login_on")}
{Color.灰}twofa      {Color.RESET}: {user.get("twofa_scheme")}

{Color.灰}groups     {Color.RESET}: {", ".join([group.get("name") for group in user.get("groups")])}
{Color.灰}memberships{Color.RESET}: {", ".join([group.get("project").get("name") for group in user.get("memberships")])}
    """

    print(preview)


@show.command()
@click.argument("id", type=str)
@click.option("--redmine_name", "-n", help=Help.REDMINE_NAME)
def issue(id: str, redmine_name: Optional[str]) -> None:

    url, api_key = load_config(redmine_name)
    if not url or not api_key:
        print("invalidate config")
        return

    body, err, = show_issue(url, api_key, id)
    if err:
        print(err.reason)
        return

    issue = body.get("issue")
    preview = f"""{issue.get("tracker").get("name")}

{Color.背景緑} {Color.RESET} {Color.緑}{Color.BOLD}#{issue.get("id")} {issue.get("subject")}{Color.RESET}
------------------------------------------------
 {issue.get("status").get("name")} | {issue.get("priority").get("name")} |
------------------------------------------------
{issue.get("description")}
    """
    print(preview)


def cli() -> None:
    redman(obj={})


redman.add_command(show)

if __name__ == "__main__":
    cli()
