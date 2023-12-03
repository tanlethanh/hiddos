import json
import random
from subprocess import PIPE, run

import click


def get_victim_ip() -> str:
    """
    Get the victim's IP address
    """
    f = open(".hiddos/victim.json")
    meta = json.load(f)

    return meta["ip"]


def get_dns_ip() -> str:
    """
    Get the DNS's IP address
    """
    f = open(".hiddos/victim.json")
    meta = json.load(f)

    return meta["dns_ip"]


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
