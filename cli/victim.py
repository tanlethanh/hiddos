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
    if ip:
        command = [
            "terraform",
            "output",
            "--raw",
            "-state=./cloud/terraform.tfstate",
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
    else:
        click.echo(ctx.get_help())

    click.echo("\n")
