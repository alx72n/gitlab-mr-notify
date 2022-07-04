"""Test messages functionality."""

import pytest

"""
Feature: Compose a message with the list of open merge requests.
"""


@pytest.mark.notimplemented
def test_compose_message() -> None:
    """
    Scenario: Compose a message with the list of open merge requests
        Given <open_mrs> with the list of open merge requests is set
            And <username> with the username of the GitLab user is set
        When I run compose_message() function
        Then A message with the list of open merge requests in GitLab for the
            selected user <username> in markdown format is returned.
    """
    # TODO Implement test test_compose_message().