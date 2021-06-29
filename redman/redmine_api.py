import json
from typing import Any
from urllib import error, parse, request


################################
# projects
################################
def list_projects(url: str, api_key: str) -> Any:
    try:
        params = {
            "key": api_key
        }
        req = request.Request(f"{url}/projects.json?{parse.urlencode(params)}")

        with request.urlopen(req) as res:
            return json.load(res)
    except error.HTTPError as err:
        print(err.code)
        return
    except error.URLError as err:
        print(err.reason)
        return


def show_project() -> None:
    pass


################################
# users
################################
def list_users() -> None:
    pass


def show_user() -> None:
    pass


################################
# issues
################################
def list_issues(url: str, api_key: str, project: str) -> Any:
    try:
        params = {
            "key": api_key,
            "project": project,
            "op[status_id]": "o"
        }

        req = request.Request(f"{url}/issues.json?{parse.urlencode(params)}")

        with request.urlopen(req) as res:
            return json.load(res)
    except error.HTTPError as err:
        print(err.code)
        return
    except error.URLError as err:
        print(err.reason)
        return


def show_issue() -> None:
    pass
