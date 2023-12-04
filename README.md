<h1 align="center">HiDDoS</h1>
<p align="center">A simulation CLI used to learn and simulate DoS/DDoS attacks using cloud services and cyber tools</p>

## Setup

### Setup dependencies

We use Terraform with [AWS](https://docs.aws.amazon.com/) provider to launch an ec2 instance as a victim, you need to setup an AWS account and config `credentials` in the local environment

To make attacks more efficient, we use `sendpfast` of `scapy` that need `tcpreplay` dependency, you need to install it before running the CLI

### Setup cli

We already have a CLI to run the simulation easily. Firstly, you need to build the CLI in development mode

```shell
pip install --editable .
```

After above step, you already have a cli to simulate and test DoS/DDoS attack. View detail of the cli `hiddos --help`, And remember to just run the CLI at root of project

Init HiDDoS project

```shell
hiddos init
```

First things first, you need to init and launch cloud machines (DNS server and Victim machine)

```shell
hiddos cloud --launch
```

If you work directly with Terraform, remember to run `hiddos cloud --ip` to resync the IP config for other commands

What happens after running `launch` command?
-> This command launches some cloud setup using Terraform, with 2 ec2 instances, one for a victim and one for a DNS server (used to simulate a DNS Amplification attack). Also it setups some config and creates `.hiddos` directory used by other commands

## Start

### Pure attack

After setup victim, you're now able to attack this one

Each attack is defined as a subcommand, remember to use `--help` to explore all the options to attack or protect. Eg. `hiddos syn-flood --help`

#### SYN Flood

To know the detail of the SYN Flood attack [cloudflare.com/learning/ddos/syn-flood-ddos-attack](https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack/)

Start attacking the victim by default config

```shell
hiddos syn-flood
```

```shell
hiddos syn-flood --mode ddos --count 999999
```

You need to open `Wireshark` and watch network changes, a tone of SYN packages sent to the victim. Our setup primarily points to port 80 of HTTP requests, the `cli` will shows a URL for you to launch a web page as a legitimate client. After a few seconds, the server victim will be down, and you can not reach the server to get the web page.

### Connect and SSH

Go to cloud directory and run terraform setup

```shell
cd cloud
terraform apply
```

After `terraform apply`, it shows IP address of launched instance used to connect ssh from locally. Also, an ssh key will be generated, you need to enable key permission

```shell
chmod 400 ./rf_ec2_key.pem
```

Connect to the instance by SSH

```shell
ssh ec2-user@<ip address> -i ./rf_ec2_key.pem
```

## References

[DNS amplification example](https://gist.github.com/thom-s/7b3fcdcb88c0670167ccdd6ebca3c924?permalink_comment_id=3578341)
