import click

from ui.cli.command import Command


class Input(Command):
    def __init__(self, title: str, value=None):
        self.title = title
        self.value = value

    def render(self):
        click.echo("%s\t%s" % (self.title, self.value))
