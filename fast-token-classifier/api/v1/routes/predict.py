from fastapi import APIRouter

from api.v1.schemas import InputSchema, PredictionsSchema
from fast_token_classifier.info_extraction.predict import (
    classify_tokens,
    json_format_response,
)

pred_router: APIRouter = APIRouter(prefix="/predict")


@pred_router.post(path="", response_model=PredictionsSchema)
async def get_predictions(text: InputSchema) -> PredictionsSchema:
    """This is used to classify the tokens."""
    result = classify_tokens(model_input=text.data)

    return {"result": json_format_response(input_value=result)}  # type: ignore
