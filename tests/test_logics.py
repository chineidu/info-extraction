"""This module contains the test(s) for the utility function(s)."""

import os
from typing import Any

from fast_token_classifier.creds import authenticate
from fast_token_classifier.info_extraction.utils.utilities import (
    _create_dir,
    _delete_dir,
)


def test_authenticate() -> None:
    """This is used to test the authenticate logic."""
    # Given
    expected: dict[str, Any] = {
        "HUGGINGFACE_TOKEN": "your_huggingface_token",
        "USERNAME": "your_username",
        "PASSWORD": "your_password",
        "NONE": None,
    }

    # When
    (HUGGINGFACE_TOKEN, USERNAME, PASSWORD) = authenticate()

    # Then
    assert HUGGINGFACE_TOKEN != expected.get("HUGGINGFACE_TOKEN")
    assert HUGGINGFACE_TOKEN != expected.get("NONE")
    assert USERNAME != expected.get("USERNAME")
    assert PASSWORD != expected.get("PASSWORD")


def test_create_dir() -> None:
    """This is used to test the _create_dir logic."""
    # Given
    directory_path: str = "sample_dir"

    # When
    result: None = _create_dir(directory_path=directory_path)

    # Then
    assert os.path.exists(directory_path)
    assert result is None


def test_delete_dir() -> None:
    """This is used to test the _delete_dir logic."""
    # Given
    directory_path: str = "sample_dir"

    # When
    result: None = _delete_dir(directory_path=directory_path)

    # Then
    assert not os.path.exists(directory_path)
    assert result is None
