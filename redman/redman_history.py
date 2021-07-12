import os
from typing import List, Optional

REDMAN_HISTORY = os.path.join(os.path.expanduser("~"), ".redman_history")


def create_history_file_default_if_not_exists() -> None:

    if not os.path.exists(REDMAN_HISTORY):
        with open(REDMAN_HISTORY, "a", encoding="UTF-8") as file:
            file.write("")


def add_history(redine_name: str = None, status: str = "open", project_id: str = None, user_id: str = None) -> None:

    history = "\t".join([
        str(redine_name) if redine_name else "",
        str(status) if status else "",
        str(project_id) if project_id else "",
        str(user_id) if user_id else "",
    ]) + "\n"
    with open(REDMAN_HISTORY, "a", encoding="UTF-8") as file:
        file.write(history)


def load_history() -> Optional[List[str]]:

    if not os.path.exists(REDMAN_HISTORY):
        return None

    with open(REDMAN_HISTORY, "r", encoding="UTF-8") as file:
        return file.readlines()
