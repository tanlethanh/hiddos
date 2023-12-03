# HiDDoS

A setup to learn and simulate DoS/DDoS attack

## Setup

### Setup dependencies

We use Terraform with [AWS](https://docs.aws.amazon.com/) provider to launch an ec2 instance as a victim, you need to setup a AWS account and config `credentials` in local environment

### Setup cli

We already have a cli for easily run the simulation. Firstly, you need to build the cli

```shell
pip install --editable .
```

After above step, you already have a cli to simulate and test DoS/DDoS attack

View detail of the cli

```shell
hiddos --help
```

First things first, you need to init and launch victim machine

```shell
hiddos victim --launch
```

## Start

### Pure attack

After setup victim, you're now able to attack this one

Each attack is define as a subcommand, remember to use `--help` to explore all the options to attack or protect. Eg. `hiddos syn-flood --help`

#### SYN Flood

```shell
hiddos syn-flood # Start attack with default config DoS mode, send 10000 packages
```

```shell
hiddos syn-flood --mode ddos -num-pkg 999999
```

### Connect and SSH

Go to cloud directory and run terraform setup

```shell
cd cloud
terraform apply
```

After `terraform apply`, it shows ip address of launched instance used to connect ssh from local. Also, a ssh key will be generated, you need enable key permission

```shell
chmod 400 ./rf_ec2_key.pem
```

Connect to the instance by SSH

```shell
ssh ec2-user@<ip address> -i ./rf_ec2_key.pem
```
