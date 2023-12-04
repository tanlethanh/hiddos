import os
import subprocess

import click

from cli.utils.common import get_dns_ip, get_victim_ip

paths = [
    "cloud/tf_ec2_key.pem",
    "../cloud/tf_ec2_key.pem",
    "../../cloud/tf_ec2_key.pem",
    "../../../cloud/tf_ec2_key.pem",
]


@click.command(help="SSH to victim or dns server")
@click.option(
    "--target", help="SSH to victim or dns server", type=click.Choice(["victim", "dns"])
)
def ssh(target):
    click.echo("\n\n-------------------- Run SSH ---------------------\n")
    for p in paths:
        abs_path = os.path.join(os.getcwd(), p)
        if os.path.exists(abs_path):
            click.echo("Found SSH key")
            subprocess.run(["chmod", "400", abs_path])
            break

    if not target:
        return
    elif target == "victim":
        remote = f"ec2-user@{get_victim_ip()}"
    elif target == "dns":
        remote = f"ec2-user@{get_dns_ip()}"

    click.echo(f"SSH to {remote}")
    subprocess.run(["ssh", "-i", abs_path, remote])
