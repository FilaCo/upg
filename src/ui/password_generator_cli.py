import click

from pass_gen.password_generator import PasswordGenerator


@click.group()
def cli():
    pass


@cli.command()
@click.option('--custom', '-c')
def generate(custom: bool):
    return custom_generate() if custom else default_generate()


def custom_generate():
    pass


def default_generate():
    password_generator = PasswordGenerator()

    password_generator.add_ascii_lowercase()
    password_generator.add_ascii_uppercase()
    password_generator.add_digits()
    password_generator.add_punctuation()
    password_generator.length = 25

    password = password_generator.generate()

    click.echo("Your new password: %s" % password)
