import json
import logging
import os
from urllib import error, parse, request

from plumbum import FG, cli, colors, local
from texttable import Texttable

REDMINE_URL = "http://localhost:13000"
REDMIEN_API_KEI = "bb2fcbf8e06106f10e9dfe6bcf828b9fa8774884"
REDMIEN_USER_NAME = ""
REDMIEN_PASSWORD = ""


class Redman(cli.Application):
    PROGNAME = colors.green
    DESCRIPTION = None
    DESCRIPTION_MORE = None
    VERSION = colors.blue | "1.0.2"
    USAGE = None
    COLOR_USAGE = None
    COLOR_GROUPS = {"Meta-switches": colors.bold & colors.yellow}
    CALL_MAIN_IF_NESTED_COMMAND = True
    ALLOW_ABBREV = False

    cheese = cli.Flag(["cheese"], help="cheese, please")
    chives = cli.Flag(["chives"], help="chives, instead")
    opts = cli.Flag("--ops", help=colors.magenta | "This is help")

    @cli.switch(names="-loglevel", argtype=int)
    def set_log_level(self, level: int) -> None:
        """Sets the log-level of the logger"""
        logging.root.setLevel(level)

    # def main(self, *args) -> int:
    #     super().main()
    #     # projects
    #     # issuses
    #     # TODO: users
    #     if args:
    #         print("Unknown command {0!r}".format(args[0]))
    #         return 1   # error exit code
    #     if not self.nested_command:           # will be ``None`` if no sub-command follows
    #         print("No command given")
    #         return 1   # error exit code

    #     # 設定ファイルのチェック
    #     # 必要コマンドのチェック
    #     # --config=~/.redconfig
    #     # default: my-redmine
    #     # my-redmine:
    #     #   - url: "localhost:13000"
    #     #   - api_key: "bb2fcbf8e06106f10e9dfe6bcf828b9fa8774884"
    #     #   - user_name: "user_name"
    #     #   - password: "passworde"
    #     # --redmine-name=default
    #     os.getenv("HOME")
    #     fzf = local["fzf"]
    #     echo = local["echo"]
    #     (echo["hoge"] | fzf) & FG


@Redman.subcommand("projects")                    # attach 'geet commit'
class Projects(cli.Application):
    """creates a new commit in the current branch"""

    def main(self) -> int:
        params = {
            "key": REDMIEN_API_KEI
        }
        req = request.Request(f"{REDMINE_URL}/projects.json?{parse.urlencode(params)}")
        try:
            with request.urlopen(req) as res:
                body = json.load(res)
        except error.HTTPError as err:
            print(err.code)
            return 1
        except error.URLError as err:
            print(err.reason)
            return 1

        projects = body.get("projects")
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

        fzf = local["fzf"]
        echo = local["echo"]
        hoge = echo[table.draw()] | fzf["--header-lines=2"]
        a = hoge & FG
        print(a)
        print(hoge)
        return 0


@Redman.subcommand("issues")                      # attach 'geet push'
class Issues(cli.Application):
    """pushes the current local branch to the remote one"""

    def main(self) -> None:
        print("doing the push...")


def main() -> None:
    app = Redman()
    app.run()
