
def exec_command():
    from paramiko import client
    from flask import request
    address = request.args.get("address")
    cmd = "ping -c 1 %s" % address
    client = client.SSHClient()
    client.connect("ssh.samplehost.com")
    client.exec_command(cmd)