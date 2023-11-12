"""This module contains the Pytest fixtures."""
from typing import Any, Generator

"""This midule is used for setting up Pytest fixtures."""

import pytest
from fastapi.testclient import TestClient

from api.app import app
from api.v1.schemas import InputSchema


@pytest.fixture()
def client() -> Generator:
    """This is used to setup the test client."""
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}


@pytest.fixture
def user_input_1() -> InputSchema:
    """This is used to load the sample model input."""
    data: dict[str, Any] = {"data": "My name is Chineidu and I work at Indicina in Lagos, Nigeria."}
    yield data


@pytest.fixture
def user_input_2() -> InputSchema:
    """This is used to load the sample model input."""
    data: dict[str, Any] = {"data": "Olumo Rock is a landmark in Abeokuta, Nigeria."}
    yield data
