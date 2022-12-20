output "namecheck" {
  value = "user name is ${var.username}"
}

output "imagecheck" {
  value = "docker image for k8s pod: ${var.username}"
}
