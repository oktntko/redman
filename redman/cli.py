import json
import os
import re
import subprocess
from urllib import error, parse, request

import yaml
from fire import Fire
from texttable import Texttable

REDMINE_URL = "http://localhost:13000"
REDMIEN_API_KEI = "bb2fcbf8e06106f10e9dfe6bcf828b9fa8774884"
REDMIEN_USER_NAME = ""
REDMIEN_PASSWORD = ""

REDMANRC = os.path.join(os.path.expanduser("~"), ".redmanrc")

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


def projects() -> None:
    params = {
        "key": REDMIEN_API_KEI
    }
    req = request.Request(f"{REDMINE_URL}/projects.json?{parse.urlencode(params)}")
    try:
        with request.urlopen(req) as res:
            body = json.load(res)
    except error.HTTPError as err:
        print(err.code)
        return
    except error.URLError as err:
        print(err.reason)
        return

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


def issues(project: str) -> None:
    params = {
        "key": REDMIEN_API_KEI,
        "project": project,
        "op[status_id]": "o"
    }
    req = request.Request(f"{REDMINE_URL}/issues.json?{parse.urlencode(params)}")
    try:
        with request.urlopen(req) as res:
            body = json.load(res)
    except error.HTTPError as err:
        print(err.code)
        return
    except error.URLError as err:
        print(err.reason)
        return

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


def config() -> None:
    if not os.path.exists(REDMANRC):
        config_file_default = {
            "default": "my-project",
            "my-project": {
                "REDMINE_URL": "<your Redmine url>",
                "REDMINE_API_ACCESS_KEY": "<your Redmine Access Key>"
            }
        }
        with open(REDMANRC, "a", encoding="UTF-8") as config_file:
            yaml.dump(config_file_default, config_file)

    _ = subprocess.run(
        f"eval ${{EDITOR:-vi}} {REDMANRC}",
        shell=True, check=False)


def main() -> None:
    Fire({
        "projects": projects,
        "users": users,
        "issues": issues,
        "config": config,
    })
