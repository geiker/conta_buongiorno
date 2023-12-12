from __future__ import annotations

import string
from datetime import datetime

from rich.table import Table

from conta_buongiorno.typing import Message


def create_table(title: str, datas: list[any], columns: list[dict], **kwargs) -> Table:
    """Create a table with the given columns"""
    table = Table(title=title, **kwargs)
    for c in columns:
        table.add_column(**c)

    for data in datas:
        table.add_row(*[str(d) for d in data])
    
    return table


def buongiorno_list_get(lines: list[str]) -> list[Message]:
    """Filter lines that contain the word 'buongiorno'"""
    messages: list[Message] = []
    
    for l in lines:
        # When exporting from WhatsApp all media are omitted
        if 'Media omessi' in l: continue
        try:
            # Message Example:
            # * 01/01/21, 07:49 - Mamma: Buongiorno
            # * Date, Time - Sender: Message
            
            # Getting only the date and time
            date_str, other = l.split(" - ", 1)

            # From other we get the sender and the message
            sender, message = other.split(": ", 1)

            # Final result:
            # date = 01/01/21, 07:49
            # sender = Mamma
            # message = Buongiorno

            # Cleaning the message, removing newlines and spaces
            message = message.replace("\n", "")
            message = message.lower()

            # Removing all non-ascii characters and spaces
            # ? Why we are removing spaces? Because "Buon giorno" is not the same as "Buongiorno"
            message = "".join([c for c in message if c in string.ascii_letters])

            # Cleaning the date, removing spaces
            date_str = date_str.strip()

            # Converting the date to a datetime object
            date = datetime.strptime(date_str, "%d/%m/%y, %H:%M")

            if 'buongiorno' in message:                
                messages.append({
                    "date": date,
                    "sender": sender,
                    "message": message
                })
        except Exception:
            pass

    return messages