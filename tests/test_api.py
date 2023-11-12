"""This module contains the test(s) for the endpoint(s)."""

from typing import Any

from fastapi.testclient import TestClient
from pytest import mark

from api.api_config import settings
from api.v1.schemas import InputSchema

API_VERSION_STR: str = settings.API_VERSION_STR
HOST: str = settings.HOST
PORT: int = settings.PORT


def test_health_check(client: TestClient) -> None:
    """This checkes the health of the API."""
    # Given
    expected: dict[str, Any] = {
        "message": f"{settings.PROJECT_NAME!r} app is working",
        "status": "success!",
        "status_code": 200,
    }
    URL: str = f"http://{HOST}:{PORT}/health"

    # When
    response = client.get(URL)
    result: dict[str, Any] = response.json()

    # Then
    assert response.status_code == expected.get("status_code")
    assert result.get("message") == expected.get("message")
    assert result.get("status") == expected.get("status")


# ==== `Mark` the test as an `integration test` ====
@mark.integration
def test_token_classification(client: TestClient, user_input_1: InputSchema) -> None:
    """This is used to test the predict endpoint."""
    # Given
    expected: dict[str, int] = {
        "status_code": 200,
        "result": [
            {
                "entity_group": "PER",
                "score": 0.998051,
                "word": "Chineidu",
                "start": 11,
                "end": 19,
            },
            {
                "entity_group": "ORG",
                "score": 0.99873996,
                "word": "Indicina",
                "start": 34,
                "end": 42,
            },
            {
                "entity_group": "LOC",
                "score": 0.9987972,
                "word": "Lagos",
                "start": 46,
                "end": 51,
            },
            {
                "entity_group": "LOC",
                "score": 0.99931777,
                "word": "Nigeria",
                "start": 53,
                "end": 60,
            },
        ],
    }
    URL: str = f"http://{HOST}:{PORT}/{API_VERSION_STR}/predict"

    # When
    response = client.post(URL, json=user_input_1)
    model_result: list[str, Any] = response.json().get("result")

    # Then
    assert response.status_code == expected.get("status_code")

    assert model_result[0].get("entity_group") == expected.get("result")[0].get("entity_group")
    assert model_result[0].get("score") == expected.get("result")[0].get("score")
    assert model_result[0].get("word") == expected.get("result")[0].get("word")
    assert model_result[0].get("start") == expected.get("result")[0].get("start")
    assert model_result[0].get("end") == expected.get("result")[0].get("end")

    assert model_result[-1].get("entity_group") == expected.get("result")[-1].get("entity_group")
    assert model_result[-1].get("score") == expected.get("result")[-1].get("score")
    assert model_result[-1].get("word") == expected.get("result")[-1].get("word")
    assert model_result[-1].get("start") == expected.get("result")[-1].get("start")
    assert model_result[-1].get("end") == expected.get("result")[-1].get("end")
