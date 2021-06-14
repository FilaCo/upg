import click

from ui.cli.command import Command


class Option(Command):
    def __init__(self, title: str, is_chosen: bool = False):
        self.title: str = title
        self.is_chosen: bool = is_chosen

    def render(self):
        if self.is_chosen:
            click.secho(self.title, fg="cyan")
        else:
            click.secho(self.title)
