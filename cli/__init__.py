import json
import logging
import os

import click

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from cli.cloud import cloud
from cli.dns_amplification import dns_amplification
from cli.ping_of_death import ping_of_death
from cli.ssh import ssh
from cli.syn_flood import syn_flood
from cli.teardrop import teardrop
from cli.utils.common import show_hiddos_config


@click.group(invoke_without_command=True)
@click.option(
    "--show-config", help="Show config", is_flag=True, default=False, type=bool
)
def hiddos(show_config):
    """HiDDoS - simulate attacking and protection for DDoS attacks"""

    if show_config:
        config = show_hiddos_config()
        click.echo(json.dumps(config, indent=4))
        return


@click.command("init", help="Init HiDDoS project")
def init():
    path = ".hiddos"
    meta_path = ".hiddos/victim.json"
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


hiddos.add_command(init)
hiddos.add_command(ssh)
hiddos.add_command(cloud)
hiddos.add_command(syn_flood)
hiddos.add_command(dns_amplification)
hiddos.add_command(teardrop)
hiddos.add_command(ping_of_death)
