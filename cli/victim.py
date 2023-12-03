import json
from subprocess import PIPE, run

import click


@click.command()
@click.pass_context
@click.option(
    "--launch", help="Launch victim machine on AWS EC2 by Terraform", is_flag=True
)
@click.option("--ip", help="IP address of victim", is_flag=True)
def victim(ctx, launch, ip):
    click.echo("\n\n-------------------- Victim ---------------------\n")
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
            click.echo("Victim machine launched successfully")
        else:
            err = result.stderr.decode("utf-8")
            click.echo(f"Fail to launch victim machine:\n{err}", err=True)
            return

        ip = True

    if ip:
        command = [
            "terraform",
            "-chdir=./cloud",
            "output",
            "--raw",
            "instance_public_ip",
        ]
        result = run(command, stdout=PIPE, stderr=PIPE)
        if result.returncode == 0:
            out = result.stdout.decode("utf-8")
            click.echo(f"Victim IP address: {out}")
            f = open(".hiddos/victim.json")
            meta = json.load(f)
            meta["ip"] = out
            json.dump(meta, open(".hiddos/victim.json", "w"), indent=4)
            f.close()

        else:
            err = result.stderr.decode("utf-8")
            click.echo(f"Fail to get ip from terraform output:\n{err}", err=True)
            click.echo("Note: Make sure you have launched victim machine by Terraform")
            return
    else:
        click.echo(ctx.get_help())

    click.echo("\n")
