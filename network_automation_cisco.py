import paramiko
import time

ip_address = '192.168.1.5'
username = 'cisco1'
password = '123'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username, password=password)

print("Success login to {}".format(ip_address))
conn = ssh_client.invoke_shell()

conn.send("conf t\n")
conn.send("int lo0\n")
conn.send("ip add 10.1.1.1 255.255.255.255\n")
time.sleep(1)

output = conn.recv(65535)
print(output.decode())

ssh_client.close()