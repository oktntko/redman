
import re
import subprocess

from fire import Fire
from texttable import Texttable

from .redmanrc import (create_config_file_default_if_not_exists,
                       edit_config_file, load_config)
from .redmine_api import (list_issues, list_projects, list_users, show_issue,
                          show_project, show_user)

# 設定ファイルのチェック
# 必要コマンドのチェック
# --config=~/.redconfig
# default: my-redmine
# my-redmine:
#   - url: "localhost:13000"
#   - api_key: "bb2fcbf8e06106f10e9dfe6bcf828b9fa8774884"
#   - user_name: "user_name"
#   - password: "passworde"
# --redmine-name=default


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
        "NO", "ID", "NAME", "DESCRIPTION",
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

    _ = subprocess.run(
        f"echo '{table.draw()}' | fzf --header-lines=2",
        shell=True, check=False, stdout=subprocess.PIPE) \
        .stdout.decode("utf-8").strip()
    print(_)
    return


def users() -> None:
    pass


def issues(project: str, redine_name: str = None) -> None:

    url, api_key = load_config(redine_name)
    if not url or not api_key:
        print("invalidate config")
        return

    body = list_issues(url, api_key, project)

    issues = body.get("issues")
    if len(issues) <= 0:
        print("no issue")
        return

    rows = [[
        "TRACKER", "STATUS", "PRIORITY", "#NO SUBJECT", "DESCRIPTION"
    ]]

    rows.extend([[
        issue.get("tracker").get("name"),
        issue.get("status").get("name"),
        issue.get("priority").get("name"),
        f"#{issue.get('id')} {issue.get('subject')}",
        issue.get("description"),
    ] for issue in issues])

    table = Texttable()
    table.set_deco(Texttable.HEADER | Texttable.VLINES)
    table.add_rows(rows)

    _ = subprocess.run(
        f"echo '{table.draw()}' | fzf --header-lines=2",
        shell=True, check=False, stdout=subprocess.PIPE) \
        .stdout.decode("utf-8").strip()
    m = re.search(r"#.*\|", _)
    if m:
        b = m.group()[:-1].strip()
        print(b)

    return


def config() -> None:
    create_config_file_default_if_not_exists()

    edit_config_file()


def main() -> None:
    Fire({
        "projects": projects,
        "users": users,
        "issues": issues,
        "config": config,
    })
