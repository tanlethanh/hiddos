import json
import random


def get_victim_ip() -> str:
    """
    Get the victim's IP address
    """
    f = open(".hiddos/victim.json")
    meta = json.load(f)

    return meta["ip"]


def random_ip():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip


def rand_int():
    x = random.randint(1000, 9000)
    return x
