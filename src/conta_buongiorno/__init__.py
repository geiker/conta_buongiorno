import os

import rich
import typer
from rich.console import Console
from rich.table import Table
from typing_extensions import Annotated

from conta_buongiorno.count import (avg_time_buongiorno_sent,
                                    first_buongiorno_sent,
                                    last_buongiorno_sent,
                                    total_buongiorno_count)
from conta_buongiorno.date import first_message_date, last_message_date
from conta_buongiorno.utils import buongiorno_list_get, create_table

console = Console()


app = typer.Typer()

@app.command()
def main(file: Annotated[typer.FileText, typer.Argument(help="File to read buongiorno from.")]):
    lines = file.readlines()
    messages_list = buongiorno_list_get(lines)

    # Clear the terminal based on the OS
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    console.rule('Conta Buongiorno', style='bold red')

    console.print()

    # Print total number of lines using color and formatting
    console.print(f"Total number of lines:      [bold red]{len(lines)}[/bold red]")
    console.print(f"Total number of buongiorno: [bold red]{len(messages_list)}[/bold red]")
    console.print(f"First message found:        [bold red]{first_message_date(messages_list)}[/bold red]")
    console.print(f"Last message found:         [bold red]{last_message_date(messages_list)}[/bold red]")
    console.print(f"Total days:                 [bold red]{(last_message_date(messages_list) - first_message_date(messages_list)).days}[/bold red]")

    console.print()
    
    buongiorno_count = total_buongiorno_count(messages_list)
    avg_time = avg_time_buongiorno_sent(messages_list)
    first_messages = first_buongiorno_sent(messages_list)
    last_messages = last_buongiorno_sent(messages_list)

    console.print(
        create_table(
            title="Total Buongiorno count",
            datas=buongiorno_count.items(),
            columns=[
                {"header": "Sender", "justify": "right", "style": "cyan", "no_wrap": True, "footer": "Total"},
                {"header": "Count", "style": "magenta", "footer": str(sum(buongiorno_count.values()))},
            ],
            show_footer=True
        )
    )

    console.print()

    console.print(
        create_table(
            title="Average time between Buongiorno",
            datas=avg_time.items(),
            columns=[
                {"header": "Sender", "justify": "right", "style": "cyan", "no_wrap": True},
                {"header": "Time", "style": "magenta"}
            ]
        )
    )

    console.print()

    console.print(
        create_table(
            title="First Buongiorno sent",
            datas=first_messages.items(),
            columns=[
                {"header": "Sender", "justify": "right", "style": "cyan", "no_wrap": True},
                {"header": "Count", "style": "magenta"}
            ]
        )
    )

    console.print()

    console.print(
        create_table(
            title="Last Buongiorno sent",
            datas=last_messages.items(),
            columns=[
                {"header": "Sender", "justify": "right", "style": "cyan", "no_wrap": True},
                {"header": "Count", "style": "magenta"}
            ]
        )
    )