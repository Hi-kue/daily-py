# Built-in Imports
import sys
import os
import re
import json
import datetime as dt
from dataclasses import dataclass


# External Imports
import click
from rich import print, box
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

DEFAULT_FILE = 'data/data.json'

PRIORITIES = {
    ['n', 'none']: 'None',
    ['l', 'low']: 'Low',
    ['m', 'medium']: 'Medium',
    ['h', 'high']: 'High'
}

@dataclass
class TodoItem:
    title: str = 'N?A'
    description: str = 'N?A'
    priority: str = 'None'
    created_at: dt.datetime = dt.datetime.now()
    
    def __dict__(self) -> dict[str, any]:
        return {
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'created_at': self.created_at
        }
        
    def __str__(self) -> str:
        return 

#region Helper Functions
def check_file_reg(filepath: str) -> bool:
    return '/' in filepath

def check_existence_of_file(filepath: str) -> str:
    borat = ""
    
    if(check_file_reg(filepath)):
        borat = 'at'
    
    if not os.path.isfile(filepath):
        console.log(f'File {filepath} is not a proper file.')
        return DEFAULT_FILE
    
    if not os.path.exists(filepath): 
        console.log(f'File {borat} {filepath} doesn\'t exist. ')
        return DEFAULT_FILE
    
    return filepath if filepath is not None else DEFAULT_FILE
#endregion

@click.group()
def todo_cli():
    pass

@click.command()
@click.argument('priority', type=click.Choice(PRIORITIES.keys()), default='n')
@click.argument('filepath', type=click.Path(exists=False), required=0)
@click.option(
    '-t', '-tt', '--title',
    prompt="Enter a valid title for the task:",
    help="The title for the specified task.")
@click.option(
    '-d', '-desc', '--description',
    prompt="Enter a description for the task:",
    help="The description for the specified task.")
def add_todo(title, description, priority, filepath):
    file_name = filepath if filepath is not None else DEFAULT_FILE
    
    with open(file_name, 'a+') as file:
        new_todo = TodoItem(title=title, description=description, priority=priority)
        file.write(json.dumps(new_todo.__dict__))
        file.write('\n')
    
    console.log(f'Task "{title}" has been added to the file.')
    
    
@click.command()
@click.argument("idx", type=click.INT, required=1)
def delete_todo(idx, filepath):
    with open(filepath, 'r') as file:
        td_list = file.read().splitlines()
        td_list.pop(idx)
        
    with open(filepath, 'w') as file:
        file.write('\n'.join(td_list))
        file.write('\n')

def update_todo():
    pass

def patch_todo():
    pass

@click.command()
@click.option(
    '-p', '-pri', '--priority',
    type=click.Choice(PRIORITIES.keys()),
    prompt="Enter the priority level you are looking for:",
    default='n')
@click.argument('filepath', type=click.Path(exists=True), required=0)
def list_todo(priority, filepath):
    file_name = check_existence_of_file(filepath)
    
    with open(file_name, 'r') as file:
        td_list = file.read().splitlines()
        
    if priority is None:
        for idx, todo in enumerate(td_list):
            console.log(f'({idx}) - {todo}')
    else:
        for idx, todo in enumerate(td_list):
            if f'priority: {PRIORITIES[priority]}' in todo:
                print(f'({idx}) - {todo}')

@todo_cli.add_command(add_todo)
@todo_cli.add_command(delete_todo)
@todo_cli.add_command(update_todo)
@todo_cli.add_command(patch_todo)
@todo_cli.add_command(list_todo)

if __name__ == '__main__':
    todo_cli()