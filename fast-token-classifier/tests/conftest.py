# type: ignore
"""This module is used for setting up Pytest fixtures."""

import pytest


@pytest.fixture
def user_input_1() -> str:
    """This is used to load the sample model input."""
    data: str = "My name is Chineidu and I work at Indicina in Lagos, Nigeria."
    yield data


@pytest.fixture
def user_input_2() -> str:
    """This is used to load the sample model input."""
    data: str = "Olumo Rock is a landmark in Abeokuta, Nigeria."
    yield data
