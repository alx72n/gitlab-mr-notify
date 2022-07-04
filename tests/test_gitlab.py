"""Test GitLab integration."""

import pytest

"""
Feature: Get a list of open merge requests in GitLab.
"""


@pytest.mark.notimplemented
def test_open_merge_requests_env_variables() -> None:
    """
    Scenario: Get a list of open merge requests in GitLab
        Given GitLab environment variables are set
            And GitLab `author_id` is provided
        When I run open_merge_requests() function
        Then A list of the last 100 open merge requests not in a wip status is
            printed to the stdout
    """
    # TODO Implement test test_open_merge_requests_env_variables().


@pytest.mark.notimplemented
def test_open_merge_requests_env_file() -> None:
    """
    Scenario: Get a list of open merge requests in GitLab
        Given GitLab environment variables are set via environment file
            And GitLab `author_id` is provided
        When I run open_merge_requests() function
        Then A list of the last 100 open merge requests not in a wip status is
            printed to the stdout
    """
    # TODO Implement test test_open_merge_requests_env_file().
