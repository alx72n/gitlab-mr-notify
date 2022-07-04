"""Test application gitlab_mr_notify."""

import pytest

"""
Feature: Notify about open merge requests in GitLab to Mattermost channel.
"""


@pytest.mark.notimplemented
def test_gitlab_mr_notify_env_variables() -> None:
    """
    Scenario: Notify about open merge requests in GitLab to Mattermost
        channel
        Given GitLab environment variables are set
            And Mattermost environment variables are set
        When I run gitlab_mr_notify.py script
        Then A list of the last 100 open merge requests is printed to the
            stdout
            And A message with the same content is sent to Mattermost channel
    """
    # TODO Implement test test_gitlab_mr_notify_env_variables().


@pytest.mark.notimplemented
def test_gitlab_mr_notify_env_file() -> None:
    """
    Scenario: Notify about open merge requests in GitLab to Mattermost
        channel
        Given GitLab environment variables are set via environment file
            And Mattermost environment variables are set via environment file
        When I run gitlab_mr_notify.py script
        Then A list of the last 100 open merge requests is printed to the
            stdout
            And A message with the same content is sent to Mattermost channel
    """
    # TODO Implement test test_gitlab_mr_notify_env_file().
