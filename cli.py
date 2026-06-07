import click
from notes import NoteManager

manager = NoteManager()

@click.group()
def cli():
    """Simple note-taking CLI."""
    pass

@cli.command()
@click.argument("text")
def add(text):
    """Add a new note."""
    manager.add(text)
    click.echo(f"Note added: {text}")

@cli.command()
def list():
    """List all notes."""
    notes = manager.get_all()
    if not notes:
        click.echo("No notes yet.")
        return
    for i, note in enumerate(notes, 1):
        click.echo(f"{i}. {note['text']}")

@cli.command()
@click.argument("index", type=int)
def delete(index):
    """Delete a note by index."""
    manager.delete(index - 1)
    click.echo(f"Note {index} deleted.")

if __name__ == "__main__":
    cli()
