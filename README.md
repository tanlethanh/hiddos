# HiDDoS

A setup to learn and simulate DoS/DDoS attack

## Setup

### Setup cli

We already have a cli for easily run the simulation. Firstly, I need to build the cli

```bash
pip install --editable .
```

### Setup cloud machine

We use Terraform with [AWS](https://docs.aws.amazon.com/) provider to launch an ec2 instance as a victim, you need to setup a AWS account and config `credentials` in local environment

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
