from typing import Any

from pydantic import BaseModel


class IndexSchema(BaseModel):
    """This is the schema for the index response."""

    message: str
    status: str


class InputSchema(BaseModel):
    """Schema for the model input."""

    data: str

    class Config:
        """Sample Payload"""

        schema_extra = {
            "example": {"data": "My name is Chineidu and I work at Indicina in Lagos, Nigeria."}
        }


class PredOut(BaseModel):
    entity_group: str
    score: float
    word: str
    start: int
    end: int


class PredictionsSchema(BaseModel):
    result: list[PredOut]
