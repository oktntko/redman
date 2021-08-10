from __future__ import annotations
# https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class

import json
from enum import Enum
from typing import Any, Optional, Tuple
from urllib import error, parse, request


################################
# projects
################################
def list_projects(base_url: str, api_key: str) -> Tuple[Any, Optional[error.URLError]]:
    """GET /projects.[format]"""
    try:
        params = {
            "key": api_key
        }
        req = request.Request(f"{base_url}/projects.json?{parse.urlencode(params)}")

        with request.urlopen(req) as res:
            return json.load(res), None
    except error.URLError as err:
        return None, err


################################
# users
################################
class UserStatus(Enum):
    ANONYMOUS = 0
    ACTIVE = 1
    REGISTERED = 2
    LOCKED = 3
    UNKNOWN = -1

    @classmethod
    def value_of(cls, value: Optional[int]) -> UserStatus:
        if not value:
            return UserStatus.UNKNOWN

        for e in UserStatus:
            if value == e.value:
                return e

        return UserStatus.UNKNOWN


def list_users(base_url: str, api_key: str) -> Tuple[Any, Optional[error.URLError]]:
    """GET /users.json"""
    try:
        params = {
            "key": api_key
        }
        req = request.Request(f"{base_url}/users.json?{parse.urlencode(params)}")

        with request.urlopen(req) as res:
            return json.load(res), None
    except error.URLError as err:
        return None, err


def show_user(base_url: str, api_key: str, id: str) -> Tuple[Any, Optional[error.URLError]]:
    """GET /users/[id].[format]"""
    try:
        params = {
            "key": api_key,
            "include": "memberships,groups",
        }

        req = request.Request(f"{base_url}/users/{id}.json?{parse.urlencode(params)}")

        with request.urlopen(req) as res:
            return json.load(res), None
    except error.URLError as err:
        return None, err


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


def list_issues(base_url: str, api_key: str,
                status: IssueStatus = IssueStatus.OPEN, project_id: str = None, user_id: str = None
                ) -> Tuple[Any, Optional[error.URLError]]:
    """GET /issues.[format]"""
    try:
        params = {
            "key": api_key,
            "sort": "due_date,id",
            "f[]": "status_id",
            "op[status_id]": status.value[0],
        }

        if project_id:
            params["f[]"] = "project_id"
            params["op[project_id]"] = "="
            params["v[project_id][]"] = project_id

        if user_id:
            params["f[]"] = "assigned_to_id"
            params["op[assigned_to_id]"] = "="
            params["v[assigned_to_id][]"] = user_id

        url = f"{base_url}/issues.json?{parse.urlencode(params)}"

        req = request.Request(url)

        with request.urlopen(req) as res:
            return json.load(res), None
    except error.URLError as err:
        return None, err


def show_issue(base_url: str, api_key: str, id: str) -> Tuple[Any, Optional[error.URLError]]:
    """GET /issues/[id].[format]"""
    try:
        params = {
            "key": api_key,
        }

        req = request.Request(f"{base_url}/issues/{id}.json?{parse.urlencode(params)}")

        with request.urlopen(req) as res:
            return json.load(res), None
    except error.URLError as err:
        return None, err
