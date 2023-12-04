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
def hiddos():
    """HiDDoS - simulate attacking and protection for DDoS attacks"""
    click.echo("HiDDoS - simulate attacking and protection for DDoS attacks")

    path = ".hiddos"
    if not os.path.exists(path):
        os.makedirs(path)

    meta_path = ".hiddos/victim.json"
    if not os.path.exists(meta_path):
        f = open(meta_path, "w")
        init = {
            "name": "HiDDoS victim metadata",
            "version": "0.0.1",
        }
        f.write(json.dumps(init, indent=4))
        f.close()


hiddos.add_command(syn_flood)
hiddos.add_command(dns_amplification)
hiddos.add_command(victim)
hiddos.add_command(teardrop)
hiddos.add_command(ping_of_death)
