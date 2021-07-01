from fire import Fire
from texttable import Texttable

from .color import Color
from .redmanrc import (create_config_file_default_if_not_exists,
                       edit_config_file, load_config)
from .redmine_api import (IssueStatus, UserStatus, list_issues, list_projects, list_users,
                          show_issue, show_project, show_user)
from .sh_fzf import fzf_issues, fzf_projects, fzf_users


def projects(redine_name: str = None) -> None:

    url, api_key = load_config(redine_name)
    if not url or not api_key:
        print("invalidate config")
        return

    body = list_projects(url, api_key)

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

    fzf_projects(table.draw())
    return


def users(redine_name: str = None) -> None:
    url, api_key = load_config(redine_name)
    if not url or not api_key:
        print("invalidate config")
        return

    body = list_users(url, api_key)

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

    fzf_users(table.draw(), url, api_key)
    return


def user(id: str, url: str, api_key: str) -> None:
    body = show_user(url, api_key, id)

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


def issues(redine_name: str = None, status: str = "open", project_id: str = None, user_id: str = None) -> None:
    url, api_key = load_config(redine_name)
    if not url or not api_key:
        print("invalidate config")
        return

    body = list_issues(url, api_key, IssueStatus.value_of(status), project_id, user_id)

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

    fzf_issues(table.draw(), url, api_key)
    return


def issue(id: str, url: str, api_key: str) -> None:
    body = show_issue(url, api_key, id)

    issue = body.get("issue")
    preview = f"""{issue.get("tracker").get("name")}

{Color.背景緑} {Color.RESET} {Color.緑}{Color.BOLD}#{issue.get("id")} {issue.get("subject")}{Color.RESET}
------------------------------------------------
 {issue.get("status").get("name")} | {issue.get("priority").get("name")} |
------------------------------------------------
{issue.get("description")}
    """
    print(preview)


def config() -> None:
    create_config_file_default_if_not_exists()

    edit_config_file()


def main() -> None:
    Fire({
        "projects": projects,
        "users": users,
        "issues": issues,
        "show": {
            "user": user,
            "issue": issue,
        },
        "config": config,
    })
