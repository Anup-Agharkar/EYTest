from pydantic import BaseModel, field_validator
from typing import List

class AdditionRequest(BaseModel):
    batchid: str
    payload: List[List[int]]

    @field_validator('payload')
    def check_payload(cls, v):
        if not v:
            raise ValueError('Each sublist in payload must have at least one integer')
        return v
