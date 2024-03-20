from fastapi import FastAPI, Query, Depends
from fastapi.responses import JSONResponse
from typing import Optional
from datetime import date
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
async def root():
    return JSONResponse({"result": "Hello world!"})


class HotelsSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        start: Optional[int] = Query(None, ge=1, le=5),
        has_spa: Optional[bool] = None,
    ) -> None:
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.start = start
        self.has_spa = has_spa


class SHotel(BaseModel):
    address: str
    name: str
    start: int


@app.get("/hotels")
async def get_hotels(search_args: HotelsSearchArgs = Depends()) -> list[SHotel]:
    """Endpoint for all hotels"""
    hotels = [
        {
            "address": "ул. Гаранира, 1, Алтай",
            "name": "Super Hotel",
            "start": 5,
        }
    ]

    return hotels


# SName because SchemaName
class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
async def add_booking(booking: SBooking):
    pass
