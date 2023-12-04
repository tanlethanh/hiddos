import json
from subprocess import PIPE, run

import click

from cli.utils.common import load_terraform_output


@click.command()
@click.pass_context
@click.option(
    "--launch", help="Launch cloud machine on AWS EC2 by Terraform", is_flag=True
)
@click.option(
    "--ip", help="Reload IP address of EC2 instances from cloud", is_flag=True
)
def cloud(ctx, launch, ip):
    click.echo("-------------------- Victim ---------------------\n")
    if launch:
        click.echo("Init Terraform for launching victim machine on AWS EC2...")
        command = ["terraform", "-chdir=./cloud", "init"]
        result = run(command, stdout=PIPE, stderr=PIPE)
        if result.returncode == 0:
            click.echo("Init Terraform successfully")
        else:
            err = result.stderr.decode("utf-8")
            click.echo(f"Fail to init Terraform:\n{err}", err=True)
            return

        click.echo("Launching victim machine on AWS EC2 by Terraform...")
        command = ["terraform", "-chdir=./cloud", "apply", "-auto-approve"]
        result = run(command, stdout=PIPE, stderr=PIPE)
        if result.returncode == 0:
            click.echo("Machines launched successfully")
        else:
            err = result.stderr.decode("utf-8")
            click.echo(f"Fail to launch machines:\n{err}", err=True)
            return

        ip = True

    if ip:
        f = open(".hiddos/victim.json")
        meta = json.load(f)
        ip = load_terraform_output("instance_public_ip")
        click.echo(f"Victim IP address: {ip}")
        meta["ip"] = ip
        dns_ip = load_terraform_output("dns_public_ip")
        meta["dns_ip"] = dns_ip
        click.echo(f"DNS IP address: {dns_ip}")
        json.dump(meta, open(".hiddos/victim.json", "w"), indent=4)
        f.close()
    else:
        click.echo(ctx.get_help())

    click.echo("\n")
