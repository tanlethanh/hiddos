# EC2 instance Security Group
resource "aws_security_group" "hiddos_ec2_security_group" {
  name        = "hiddos_ec2_security_group"
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
