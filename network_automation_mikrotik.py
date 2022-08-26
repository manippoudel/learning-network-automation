import paramiko

ip_address = '192.168.1.3'
username = 'admin'
password = ''

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username, password=password)

print("Success login to {}".format(ip_address))

ssh_client.exec_command("interface bridge add name=loopback0\n")
ssh_client.exec_command("ip address add address 10.2.2.1/32 interface=loopback0\n")

ssh_client.close()