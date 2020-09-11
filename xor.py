import binascii
from Crypto.Util.number import bytes_to_long, long_to_bytes

# KEY1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e ^ KEY1
# KEY3 = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1 ^ KEY2
# FLAG = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf ^ KEY1 ^ KEY2 ^ KEY3

# print(long_to_bytes(FLAG))


# print(chr(ord('c') ^ 0x0e))
# print(chr(ord('r') ^ 0x0b))
# print(chr(ord('y') ^ 0x21))
# print(chr(ord('p') ^ 0x3f))
# print(chr(ord('t') ^ 0x26))
# print(chr(ord('o') ^ 0x04))
# print(chr(ord('{') ^ 0x1e))


# print(chr(ord('}') ^ 0x04))


# myXORkey


XOR = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
b = bytes.fromhex(XOR)

print(b)

myXORkey = "myXORkey"

s = ''
l = 0
for i in b:
    # print(i)
    s += chr(i ^ ord(myXORkey[l % 8]))
    l += 1

print(s)
# print(s)
# print(XOR)
# print(''.join(list(map(lambda x: chr(ord(x) ^ myXORkey), XOR))))
