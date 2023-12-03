terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.29.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "hiddos-victim" {
  ami                    = "ami-0230bd60aa48260c6"
  instance_type          = "t2.nano"
  key_name               = aws_key_pair.tf_ec2_key.key_name
  vpc_security_group_ids = [aws_security_group.ec2_security_group.id]

  tags = {
    Name = "hiddos"
  }

  user_data = <<-EOF
              #!/bin/bash
              python3 -m http.server 80
              EOF
}

# EC2 instance Security Group
resource "aws_security_group" "ec2_security_group" {
  name        = "ec2_security_group"
  description = "Allow all inbound/outbound traffic for easily attack"

  # Accept all inbound requests
  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Accept all outbound requests
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create RSA key of size 4096 bits
resource "tls_private_key" "tf_ec2_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

# Create local file
resource "local_file" "tf_ec2_key" {
  content  = tls_private_key.tf_ec2_key.private_key_pem
  filename = "${path.module}/tf_ec2_key.pem"
}

# Create AWS key pair
resource "aws_key_pair" "tf_ec2_key" {
  key_name   = "tf_ec2_key"
  public_key = tls_private_key.tf_ec2_key.public_key_openssh
}

output "instance_user_data" {
  description = "ID of the EC2 instance"
  value       = aws_instance.hiddos-victim.user_data
}

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = "http://${aws_instance.hiddos-victim.public_ip}"
}
