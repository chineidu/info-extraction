# type: ignore
"""This module is used for setting up Pytest fixtures."""
from typing import Any

import pytest


@pytest.fixture
def user_input_1() -> dict[str, Any]:
    """This is used to load the sample model input."""
    data: dict[str, Any] = {"data": "My name is Chineidu and I work at Indicina in Lagos, Nigeria."}
    yield data


@pytest.fixture
def user_input_2() -> dict[str, Any]:
    """This is used to load the sample model input."""
    data: dict[str, Any] = {"data": "Olumo Rock is a landmark in Abeokuta, Nigeria."}
    yield data
