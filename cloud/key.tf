# Create RSA key of size 4096 bits
resource "tls_private_key" "hiddos_tf_ec2_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

# Create local file
resource "local_file" "tf_ec2_key" {
  content  = tls_private_key.hiddos_tf_ec2_key.private_key_pem
  filename = "${path.module}/tf_ec2_key.pem"
}

# Create AWS key pair
resource "aws_key_pair" "hiddos_tf_ec2_key" {
  key_name   = "hiddos_tf_ec2_key"
  public_key = tls_private_key.hiddos_tf_ec2_key.public_key_openssh
}
