import json
import os
import random
from subprocess import PIPE, run

import click

config_paths = [
    ".hiddos/victim.json",
    "../.hiddos/victim.json",
    "../../.hiddos/victim.json",
]


def get_victim_ip() -> str:
    """
    Get the victim's IP address
    """
    for p in config_paths:
        if os.path.exists(os.path.join(os.getcwd(), p)):
            f = open(p)
            meta = json.load(f)
            click.echo(f"Victim IP address: {meta}")
            click.echo(f"Victim IP address: {p}")
            return meta["ip"]

    click.echo("Cannot find .hiddos config", err=True)
    click.exceptions.Exit(-1)


def get_dns_ip() -> str:
    """
    Get the DNS's IP address
    """
    for p in config_paths:
        if os.path.exists(os.path.join(os.getcwd(), p)):
            f = open(p)
            meta = json.load(f)
            return meta["dns_ip"]

    click.echo("Cannot find .hiddos config", err=True)
    click.exceptions.Exit(-1)


def show_hiddos_config() -> dict:
    """
    Get the DNS's IP address
    """
    for p in config_paths:
        if os.path.exists(os.path.join(os.getcwd(), p)):
            f = open(p)
            meta = json.load(f)
            return meta

    click.echo("Cannot find .hiddos config", err=True)
    click.exceptions.Exit(-1)


def random_ip():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip


def rand_int():
    x = random.randint(1000, 9000)
    return x


def load_terraform_output(key: str) -> str:
    command = [
        "terraform",
        "-chdir=./cloud",
        "output",
        "--raw",
        key,
    ]
    result = run(command, stdout=PIPE, stderr=PIPE)
    if result.returncode == 0:
        out = result.stdout.decode("utf-8")
        return out

    else:
        err = result.stderr.decode("utf-8")
        click.echo(f"Fail to get ip from terraform output:\n{err}", err=True)
        click.echo("Note: Make sure you have launched victim machine by Terraform")
        return
    pass
