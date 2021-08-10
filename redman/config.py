import os
import subprocess
from typing import Optional, Tuple

import yaml

REDMANRC = os.path.join(os.path.expanduser("~"), ".redmanrc")


def create_config_file_default_if_not_exists() -> None:

    if not os.path.exists(REDMANRC):
        config_file_default = {
            "default": "my-redmine",
            "my-redmine": {
                "REDMINE_URL": "<your Redmine url>",
                "REDMINE_API_ACCESS_KEY": "<your Redmine Access Key>"
            }
        }
        with open(REDMANRC, "a", encoding="UTF-8") as config_file:
            yaml.dump(config_file_default, config_file)


def edit_config_file() -> None:
    subprocess.run(
        f"eval ${{EDITOR:-vi}} {REDMANRC}",
        shell=True, check=False)


def load_config(redmine_name: Optional[str]) -> Tuple[Optional[str], Optional[str]]:

    if not os.path.exists(REDMANRC):
        return None, None

    with open(REDMANRC, "r", encoding="UTF-8") as config_file:
        config = yaml.safe_load(config_file)

    if not redmine_name:
        redmine_name = config.get("default")
        if not redmine_name:
            return None, None

    obj = config.get(redmine_name)

    if not obj:
        return None, None

    return obj.get("REDMINE_URL"), obj.get("REDMINE_API_ACCESS_KEY")
