from fire import Fire
from texttable import Texttable

from .color import Color
from .redmanrc import (create_config_file_default_if_not_exists,
                       edit_config_file, load_config)
from .redmine_api import (IssueStatus, list_issues, list_projects, list_users,
                          show_issue, show_project, show_user)
from .sh_fzf import fzf_issues, fzf_projects


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
        "ID", "NAME", "DESCRIPTION",
    ]]
    rows.extend([[
        project.get("identifier"),
        project.get("name"),
        project.get("description"),
    ] for project in projects])

    table = Texttable()
    table.set_deco(Texttable.HEADER | Texttable.VLINES)
    table.add_rows(rows)

    fzf_projects(table.draw())
    return


def users() -> None:
    pass


def issues(project: str, redine_name: str = None, status: str = "open") -> None:
    print(project)

    url, api_key = load_config(redine_name)
    if not url or not api_key:
        print("invalidate config")
        return

    body = list_issues(url, api_key, project, IssueStatus.value_of(status))

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
            "issue": issue,
        },
        "config": config,
    })
