import click


@click.command()
def syn_flood():
    """SYN flood attack"""
    click.echo("\n-----------------------------------------")
    click.echo("Attacking with SYN flood")
    click.echo("-----------------------------------------")
