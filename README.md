# HiDDoS

A setup to learn and simulate DoS/DDoS attack

## Setup

### Setup dependencies

We use Terraform with [AWS](https://docs.aws.amazon.com/) provider to launch an ec2 instance as a victim, you need to setup a AWS account and config `credentials` in local environment

### Setup cli

We already have a cli for easily run the simulation. Firstly, you need to build the cli

```bash
pip install --editable .
```

After above step, you already have a cli to simulate and test DoS/DDoS attack

View detail of the cli

```bash
hiddos --help
```

First things first, you need to init and launch victim machine

```bash
hiddos victim --launch
```

### Connect and SSH

Go to cloud directory and run terraform setup

```bash
cd cloud
terraform apply
```

After `terraform apply`, it shows ip address of launched instance used to connect ssh from local. Also, a ssh key will be generated, you need enable key permission

```bash
chmod 400 ./rf_ec2_key.pem
```

Connect to the instance by SSH

```bash
ssh ec2-user@<ip address> -i ./rf_ec2_key.pem
```
