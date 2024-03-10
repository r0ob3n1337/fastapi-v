from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, JSONResponse
from typing import Optional
from datetime import date
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
async def root():
    return JSONResponse({"result": "Hello world!"})


@app.get("/hotels")
async def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    start: Optional[int] = Query(None, ge=1, le=5),
    has_spa: Optional[bool] = None,
):
    """Endpoint for all hotels"""
    return location, date_from, date_to


# SName because SchemaName
class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
async def add_booking(booking: SBooking):
    pass
