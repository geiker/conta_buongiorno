from collections import defaultdict

from conta_buongiorno.typing import Message


def total_buongiorno_count(messages: list[Message]) -> dict[str, int]:
    """
    Count the number of 'buongiorno' per person.

    Args:
        messages (List[Message]): A list of messages.

    Returns:
        dict[str, int]: A dictionary where the keys are the senders and the values are the counts of 'buongiorno' messages.
    """
    messages_by_sender = defaultdict(int)
    for m in messages:
        messages_by_sender[m["sender"]] += 1

    messages_by_sender = dict(messages_by_sender)

    # Sort by number of messages
    messages_by_sender = sorted(messages_by_sender.items(), key=lambda x: x[1], reverse=True)

    result: dict[str, int] = {}
    for sender, count in messages_by_sender:
        result[sender] = count

    return result


def first_buongiorno_sent(messages: list[Message]) -> dict[str, int]:
    """
    Counts the number of first 'buongiorno' messages sent by each sender.

    Args:
        messages (List[Message]): A list of messages, where each message is a dictionary

    Returns:
        dict[str, int]: A dictionary where the keys are the senders and the values are the counts
            of first 'buongiorno' messages sent by each sender.
    """
    # Group messages by date
    days = defaultdict(list)
    for m in messages:
        fmt_date = m["date"].strftime("%d/%m/%y")
        days[fmt_date].append(m)

    # Sort messages in each day
    for day, days_messages in days.items():
        days_messages = sorted(days_messages, key=lambda x: x["date"], reverse=False)
        days[day] = days_messages

    # Count first messages
    first_messages = defaultdict(int)
    for day, days_messages in days.items():
        first_messages[days_messages[0]["sender"]] += 1

    # Sort senders by count in descending order
    first_messages = dict(first_messages)
    first_messages = sorted(first_messages.items(), key=lambda x: x[1], reverse=True)

    # Create result dictionary
    result: dict[str, int] = {}
    for sender, count in first_messages:
        result[sender] = count

    return result

def last_buongiorno_sent(messages: list[Message]) -> dict[str, int]:
    """
    Counts the number of last 'buongiorno' messages sent by each sender.

    Args:
        messages (List[Message]): A list of messages, where each message is a dictionary

    Returns:
        dict[str, int]: A dictionary where the keys are the senders and the values are the counts
            of last 'buongiorno' messages sent by each sender.
    """
    # Group messages by date
    days = defaultdict(list)
    for m in messages:
        fmt_date = m["date"].strftime("%d/%m/%y")
        days[fmt_date].append(m)

    # Sort messages in each day
    for day, days_messages in days.items():
        days_messages = sorted(days_messages, key=lambda x: x["date"], reverse=False)
        days[day] = days_messages

    # Count last messages
    last_messages = defaultdict(int)
    for day, days_messages in days.items():
        last_messages[days_messages[-1]["sender"]] += 1

    # Sort senders by count in descending order
    last_messages = dict(last_messages)
    last_messages = sorted(last_messages.items(), key=lambda x: x[1], reverse=True)

    # Create result dictionary
    result: dict[str, int] = {}
    for sender, count in last_messages:
        result[sender] = count

    return result

def avg_time_buongiorno_sent(messages: list[Message]) -> dict[str, str]:
    """
    Calculate the average time of 'buongiorno' messages sent by each sender.

    Args:
        messages (list[Message]): A list of messages, where each message is a dictionary
            with 'sender' and 'date' keys.

    Returns:
        dict[str, str]: A dictionary mapping each sender to their average time of 'buongiorno'
            messages in the format 'hour:minute'.
    """
    # Create a defaultdict to store the list of minutes for each sender
    avg_time_by_sender = defaultdict(list)

    # Iterate over each message
    for m in messages:
        # Extract the hour and minutes from the 'date' key
        hour = m["date"].hour
        minutes = m["date"].minute

        # Convert the hour to minutes and add it to the minutes variable
        minutes += hour * 60

        # Append the total minutes to the list of minutes for the sender
        avg_time_by_sender[m["sender"]].append(minutes)

    # Convert the defaultdict to a regular dictionary
    avg_time_by_sender = dict(avg_time_by_sender)

    # Calculate the average minutes for each sender
    for sender, minutes in avg_time_by_sender.items():
        avg_time_by_sender[sender] = sum(minutes) / len(minutes)

    # Sort the dictionary by the average minutes in ascending order
    avg_time_by_sender = sorted(avg_time_by_sender.items(), key=lambda x: x[1], reverse=False)

    # Create a result dictionary to store the average time in 'hour:minute' format
    result: dict[str, str] = {}
    for sender, minutes in avg_time_by_sender:
        # Convert the minutes to hours and minutes
        hour = str(int(minutes / 60)).zfill(2)
        minutes = str(int(minutes % 60)).zfill(2)

        # Store the average time in the result dictionary
        result[sender] = f"{hour}:{minutes}"

    return result