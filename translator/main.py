# Built-in Modules
import re as reg
import time

# Dependencies
from googletrans import Translator, LANGUAGES

from rich import print, box
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text

console = Console()
translator = Translator()

TABLE_COLUMNS = ["Translate From", "Translate To", "Translated Message"]

#region Utility Methods
def type_write(text: str, speed: int) -> None:
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()

def filter_message(message: str) -> str:
    filtered_msg = reg.sub(r'[^a-zA-Z0-9 \n\.]', ' ', message)
    return filtered_msg

def translate_to(message: str, dest: str) -> str:
    msg = translator.translate(message, dest=dest)
    return msg.text

def translate_from(message: str, src: str) -> str:
    msg = translator.translate(message, src=src)
    return msg.text

def translate_to_and_from(message: str, src: str = 'auto', dest: str = 'en') -> str:
    msg = translator.translate(message, dest=dest, src=src)
    return msg.text

def check_language(language: str) -> bool:
    return language in LANGUAGES

def output_tabular(message: str, src: str, dest: str) -> None:
    table = Table(title="Translation Results", show_lines=True)
    
    for column in TABLE_COLUMNS:
        table.add_column(column, justify="center", header_style="bold magenta")
        
    table.add_row(src, f'{dest} ({LANGUAGES[dest]})', message)
    
    return table
#endregion


if __name__ == '__main__':
    console.clear()
    msg = Prompt.ask(
        "Enter a message you want to translate",
        default="Hello, World!"
    )
    
    src = Prompt.ask(
        "Enter the source language (default = auto)",
        choices= [lang for lang in LANGUAGES.keys()],
        default="auto"
    )
    
    dest = Prompt.ask(
        "Enter the language to translate to (default = en)",
        choices= [lang for lang in LANGUAGES.keys()],
        default="en"
    )
    
    filtered_msg = filter_message(msg)
    translated_msg = translate_to_and_from(filtered_msg, src, dest)
    
    print(output_tabular(translated_msg, src, dest))