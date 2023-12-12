from datetime import datetime
from typing import TypedDict


class Message(TypedDict):
    date: datetime
    sender: str
    message: str