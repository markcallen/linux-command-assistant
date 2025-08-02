import os
import json
import click
import subprocess
from pathlib import Path
from linux_command_assistant.main import get_command_for_question, load_api_key

CONFIG_DIR = Path.home() / ".local" / "share" / "linux_command_assistant"
CONFIG_FILE = CONFIG_DIR / "config.json"

@click.group()
def main():
    pass

@main.command()
@click.argument('question')
def ask(question):
    """Ask a Linux terminal question."""
    api_key = load_api_key()
    if not api_key:
        click.echo("Run `linux-help init` to set your OpenAI API key.")
        return
    os.environ["OPENAI_API_KEY"] = api_key
    command = get_command_for_question(question)
    click.echo(f"Running: {command}")

    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        click.echo(result.stdout)
        if result.stderr:
            click.echo(result.stderr, err=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"Error: {e.stderr}", err=True)

@main.command()
def init():
    """Set up your OpenAI API key."""
    api_key = click.prompt("Enter your OpenAI API key", hide_input=True)
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump({"api_key": api_key}, f)
    click.echo(f"API key saved to {CONFIG_FILE}")
