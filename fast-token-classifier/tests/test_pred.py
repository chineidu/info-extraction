# type: ignore
"""This module contains the test(s) for the endpoint(s)."""

from typing import Any

import numpy as np

from fast_token_classifier.info_extraction.predict import (
    classify_tokens,
)


def test_prediction(user_input_1: str) -> None:
    """This is used to test the predictions."""
    # Given
    expected: dict[str, Any] = {
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

    # When
    result = classify_tokens(model_input=user_input_1)

    # Then
    assert result[0].get("entity_group") == expected.get("result")[0].get("entity_group")
    assert np.isclose(a=result[0].get("score"), b=expected.get("result")[0].get("score"))
    assert result[0].get("word") == expected.get("result")[0].get("word")
    assert result[0].get("start") == expected.get("result")[0].get("start")
    assert result[0].get("end") == expected.get("result")[0].get("end")

    assert result[-1].get("entity_group") == expected.get("result")[-1].get("entity_group")
    assert np.isclose(a=result[-1].get("score"), b=expected.get("result")[-1].get("score"))
    assert result[-1].get("word") == expected.get("result")[-1].get("word")
    assert result[-1].get("start") == expected.get("result")[-1].get("start")
    assert result[-1].get("end") == expected.get("result")[-1].get("end")
