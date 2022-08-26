import paramiko
import time

devices = [
    {
        'ip_address' : '192.168.1.5',
        'vendor' : 'cisco',
        'username' : 'cisco1',
        'password' : '123'
    },
    {
        'ip_address' : '192.168.1.3',
        'vendor' : 'mikrotik',
        'username' : 'admin',
        'password' : ''        
    }
]

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for device in devices:
    ssh_client.connect(hostname=device['ip_address'],username=device['username'], password=device['password'])
    print("\nSuccess login to {}".format(device['ip_address']))
    
    if device['vendor'] == 'cisco':
        conn = ssh_client.invoke_shell()

        conn.send("conf t\n")
        conn.send("int lo2\n")
        conn.send("ip add 10.1.1.3 255.255.255.255\n")
        time.sleep(1)

        output = conn.recv(65535)
        print(output.decode())
    else:
        ssh_client.exec_command('interface bridge add name=loopback1\n')
        ssh_client.exec_command('ip address add address=10.2.2.2/32 interface=loopback1\n')

    ssh_client.close()