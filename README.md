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

Environment variables:

<table>
    <tr>
        <th>Variable</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>GITLAB_BASE_URL</td>
        <td>Url of GitLab instance.</td>
    </tr>
    <tr>
        <td>GITLAB_PRIVATE_TOKEN</td>
        <td>Token to call GitLab api requests.</td>
    </tr>
    <tr>
        <td>GITLAB_AUTHOR_USERNAME</td>
        <td>Username of Merge Request author.</td>
    </tr>
    <tr>
        <td>GITLAB_AUTHOR_ID</td>
        <td>User id of Merge Request author.</td>
    </tr>
    <tr>
        <td>MATTERMOST_POSTS_API</td>
        <td>Url of Mattermost instance api.</td>
    </tr>
    <tr>
        <td>MATTERMOST_TOKEN</td>
        <td>Token to call Mattermost api requests.</td>
    </tr>
    <tr>
        <td>MATTERMOST_CHANNEL</td>
        <td>Channel name of Mattermost where to post message about merge
          requests.
        </td>
    </tr>
    <tr>
        <td>MATTERMOST_CHANNEL_ID</td>
        <td>Id of Mattermost channel where to post message about merge
          requests.
        </td>
    </tr>
</table>
