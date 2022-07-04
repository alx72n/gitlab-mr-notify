"""Test Mattermost integration."""

import pytest

"""
Feature: Send a message to a Mattermost channel.
"""


@pytest.mark.notimplemented
def test_send_message_env_variables() -> None:
    """
    Scenario: Send a message to a Mattermost channel
        Given Mattermost environment variables are set
            And <message> with the list of open merge requests is set
        When I run send_message() function
        Then A message is sent to a Mattermost channel
    """
    # TODO Implement test test_send_message_env_variables().


@pytest.mark.notimplemented
def test_send_message_env_file() -> None:
    """
    Scenario: Send a message to a Mattermost channel
        Given Mattermost environment variables are set via environment file
            And <message> with the list of open merge requests is set
        When I run send_message() function
        Then A message is sent to a Mattermost channel
    """
    # TODO Implement test test_send_message_env_file().
