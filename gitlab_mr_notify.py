# /usr/bin/env python

"""Notify about GitLab open merge requests to Mattermost channel."""

from typing import Final
from typing import Any
from inspect import cleandoc
import json
import requests
from pydantic import BaseSettings
from jinja2 import Template
from requests import Response


class Settings(BaseSettings):
    """Script settings."""

    gitlab_author_id: int
    gitlab_author_username: str
    gitlab_base_url: str
    gitlab_private_token: str

    mattermost_channel: str
    mattermost_channel_id: str
    mattermost_posts_api: str
    mattermost_token: str

    class Config:
        """Config for the script settings."""

        env_file = ".env"
        env_file_encoding = "utf-8"


def open_merge_requests(author_id: int) -> str:
    """Search open merge requests by author id."""
    url: Final[str] = f"{SETTINGS.gitlab_base_url}/api/v4/merge_requests"
    querystring: Final[dict[str, str]] = {
        "author_id": str(author_id),
        "state": "opened",
        "sort": "asc",
        "per_page": "100",
    }
    headers: Final[dict[str, str]] = {
        "PRIVATE-TOKEN": SETTINGS.gitlab_private_token
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.text


def compose_message(open_mrs: str, username: str) -> str:
    """Compose message to send."""
    template_message: Template = Template(
        cleandoc(
            """**Opened Merge Requests by [{{ username }}]({{ gitlab_base_url }}/users/{{ username }}/activity)**

    {% for mr in merge_requests -%}
    - [{{ mr['references']['full'] }} {{ mr['title'] }}]({{ mr['web_url'] }})
    {% endfor %}
    """
        )
    )
    merge_requests: Final[list[dict[Any, Any]]] = json.loads(open_mrs)
    return str(
        template_message.render(
            merge_requests=merge_requests,
            username=username,
            gitlab_base_url=SETTINGS.gitlab_base_url,
        )
    )


def send_message(message: str) -> None:
    """Send message to Mattermost channel."""
    headers: dict[str, str] = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SETTINGS.mattermost_token}",
    }

    message_data: dict[str, str] = {
        "channel_id": SETTINGS.mattermost_channel_id,
        "message": message,
    }

    response: Response = requests.post(
        url=SETTINGS.mattermost_posts_api, headers=headers, json=message_data
    )
    response.raise_for_status()


SETTINGS: Final[Settings] = Settings()


def main() -> None:
    """Entrypoint of the script."""

    open_mrs: str = open_merge_requests(SETTINGS.gitlab_author_id)
    message: str = compose_message(open_mrs, SETTINGS.gitlab_author_username)
    print(message)
    send_message(message)


if __name__ == "__main__":
    main()
