# Built-in Imports
import sys
import os
import re
import datetime as dt

# External Imports
import click
from rich import print, box
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.ansi import AnsiDecoder
from rich.panel import Panel

console = Console()
CURRENT_TIME = dt.datetime.now()
CURRENT_DATE = CURRENT_TIME.date()

class DayOfWeek():
    def __init__(self) -> None:
        pass
    
    
    @click.command()
    @click.option(
        '--d', '--dt', '--date',
        prompt="Enter the date to calculate the day of week for, format: YYYY-MM-DD.",
        help="The date to calculate the day of week for, format: YYYY-MM-DD")
    def calculate_day_of_week(self, date) -> None:
        pass
    
    
    @click.command()
    @click.option(
        '--d', '--def', '--default',
        help="Use a default date to calculate the day of week for, format: YYYY-MM-DD."
    )
    def calculate_day_of_week_default(self, default) -> None:
        pass
    
    @click.command()
    @click.option(
        '--c', '--cur', '--current',
        help="Calculate the day of the week for the current data, year, month, day."
    )
    @click.argument('year', type=click.INT, default=CURRENT_DATE.year, required=0)
    @click.argument('month', type=click.INT, default=CURRENT_DATE.month, required=0)
    @click.argument('day', type=click.INT, default=CURRENT_DATE.day, required=0)
    def calculate_day_of_week_current(self, current, year, month, day) -> None:
        pass
    
    
if __name__ == '__main__':
    pass