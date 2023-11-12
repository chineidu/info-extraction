import json
from typing import Any

import numpy as np
from fastapi import APIRouter
from rich import print

from api.config import settings  # type: ignore[attr-defined]
from api.v1.schemas import InputSchema, PredictionsSchema
from fast_token_classifier.info_extraction.predict import classify_tokens, json_format_response

pred_router: APIRouter = APIRouter()


@pred_router.post(
    "/predict",
    response_model=PredictionsSchema,
)
async def get_predictions(text: InputSchema) -> Any:
    """This is used to classify the tokens."""
    result = classify_tokens(model_input=text.data)
    print(result)

    return {"result": json_format_response(input_value=result)}
