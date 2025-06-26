from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class Appointment(BaseModel):
    name: str
    email: str
    date: str
    time: str

@app.post("/book")
def book_appointment(data: Appointment):
    # Dummy calendar logic
    print(f"Booked for: {data.name}, {data.email}, {data.date} at {data.time}")
    return {"message": "Appointment booked"}
