from fastapi import APIRouter, HTTPException
from app.models.request_model import AdditionRequest
from app.models.response_model import AdditionResponse
from app.services.addition_service import process_addition
import logging
from datetime import datetime

router = APIRouter()

@router.post("/add", response_model=AdditionResponse)
async def add_numbers_endpoint(request: AdditionRequest):
    started_at = datetime.now()
    try:
        result = process_addition(request.payload)
        completed_at = datetime.now()
        return AdditionResponse(
            batchid=request.batchid,
            response=result,
            status="complete",
            started_at=started_at,
            completed_at=completed_at
        )
    except ValueError as e:
        logging.error(f"ValueError: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.error(f"Unhandled Exception: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
