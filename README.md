# gitlab_mr_notify

`gitlab_mr_notify.py` script sends a message to a Mattermost channel about
open Merge Requests in GitLab.

## Requirements

- Python modules:
  - jinja2
  - pydantic
  - python-dotenv
  - requests
- File `.env` with environment variables in the working directory.

