from pwn import *  # pip install pwntools
import json
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes

r = remote('socket.cryptohack.org', 13377, level='debug')


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


while True:
    received = json_recv()

    if received['type'] == "base64":
        encoded = base64.b64decode(received['encoded']).decode()
    elif received['type'] == "hex":
        encoded = long_to_bytes(int(received['encoded'], 16)).decode('ascii')
    elif received['type'] == "rot13":
        encoded = codecs.decode(received['encoded'], 'rot_13')
    elif received['type'] == "bigint":
        encoded = long_to_bytes(int(received['encoded'], 16)).decode('ascii')
    elif received['type'] == "utf-8":
        encoded = ''.join([chr(b) for b in received['encoded']])

    print(encoded)
    # print(received["encoded"])

    to_send = {
        "decoded": encoded
    }
    json_send(to_send)
