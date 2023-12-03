resource "aws_instance" "hiddos-victim" {
  ami = "ami-02a2af70a66af6dfb"
  # ami                    = "ami-0230bd60aa48260c6"
  instance_type          = "t2.nano"
  key_name               = aws_key_pair.hiddos_tf_ec2_key.key_name
  vpc_security_group_ids = [aws_security_group.hiddos_ec2_security_group.id]

  tags = {
    Name = "hiddos-victim"
  }

  user_data = <<-EOF
              #!/bin/bash
              python3 -m http.server 80
              EOF
}

output "instance_user_data" {
  description = "ID of the EC2 instance"
  value       = aws_instance.hiddos-victim.user_data
}

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.hiddos-victim.public_ip
}

output "instance_http_url" {
  description = "HTTP URL of the EC2 instance"
  value       = "http://${aws_instance.hiddos-victim.public_ip}"
}
