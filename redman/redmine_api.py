from __future__ import annotations
# https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class

import json
from enum import Enum
from typing import Any, Optional
from urllib import error, parse, request


################################
# projects
################################
def list_projects(url: str, api_key: str) -> Any:
    """GET /projects.[format]"""
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
    """GET /projects/[id].[format]"""
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
class IssueStatus(Enum):
    OPEN = "o", "o"
    CLOSED = "c", "c"
    ALL = "*", "a"

    @classmethod
    def value_of(cls, value: Optional[str]) -> IssueStatus:
        if not value:
            return IssueStatus.OPEN

        for e in IssueStatus:
            if value.startswith(e.value[1]):
                return e

        return IssueStatus.OPEN


def list_issues(base_url: str, api_key: str, project: str, status: IssueStatus = IssueStatus.OPEN) -> Any:
    """GET /issues.[format]"""
    try:
        params = {
            "key": api_key,
            "sort": "due_date,id",
            "f[]": "status_id",
            "op[status_id]": status.value[0],
        }

        url = f"{base_url}/projects/{project}/issues.json?{parse.urlencode(params)}"

        req = request.Request(url)

        with request.urlopen(req) as res:
            return json.load(res)
    except error.HTTPError as err:
        print(err.code)
        return
    except error.URLError as err:
        print(err.reason)
        return


def show_issue(url: str, api_key: str, id: str) -> Any:
    """GET /issues/[id].[format]"""
    try:
        params = {
            "key": api_key,
        }

        req = request.Request(f"{url}/issues/{id}.json?{parse.urlencode(params)}")

        with request.urlopen(req) as res:
            return json.load(res)
    except error.HTTPError as err:
        print(err.code)
        return
    except error.URLError as err:
        print(err.reason)
        return
