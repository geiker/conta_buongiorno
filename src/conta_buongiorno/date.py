from datetime import datetime

from conta_buongiorno.typing import Message


def first_message_date(messages: list[Message]) -> datetime:
    """
    Get the date of the first message sent.

    Args:
        messages (list[Message]): A list of messages.

    Returns:
        datetime: The date of the first message sent.
    """
    return messages[0]["date"]

def last_message_date(messages: list[Message]) -> datetime:
    """
    Get the date of the last message sent.

    Args:
        messages (list[Message]): A list of messages.

    Returns:
        datetime: The date of the last message sent.
    """
    return messages[-1]["date"]