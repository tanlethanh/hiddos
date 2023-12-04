import json
import logging
import os

import click

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


from cli.dns_amplification import dns_amplification
from cli.syn_flood import syn_flood
from cli.ping_of_death import ping_of_death
from cli.teardrop import teardrop
from cli.victim import victim


@click.group()
@click.option(
    "--init", help="Init HiDDoS project", is_flag=True, default=False, type=bool
)
def hiddos(init):
    """HiDDoS - simulate attacking and protection for DDoS attacks"""
    path = ".hiddos"
    meta_path = ".hiddos/victim.json"
    if init:
        if not os.path.exists(path):
            os.makedirs(path)

        if not os.path.exists(meta_path):
            f = open(meta_path, "w")
            init = {
                "name": "HiDDoS victim metadata",
                "version": "0.0.1",
            }
            f.write(json.dumps(init, indent=4))
            f.close()
    else:
        if not os.path.exists(meta_path):
            click.echo(
                "Not found .hiddos config, please init the project first by `hiddos --init` or going to root of project",
                err=True,
            )
            exit(-1)


hiddos.add_command(syn_flood)
hiddos.add_command(dns_amplification)
hiddos.add_command(victim)
hiddos.add_command(teardrop)
hiddos.add_command(ping_of_death)
