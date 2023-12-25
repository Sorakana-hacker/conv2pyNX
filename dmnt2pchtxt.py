import binascii
from pyfiglet import Figlet
import os

f = Figlet(font='slant')
g = f.renderText('dmnt 2 pchtxt')
print(g)
h = f.renderText('      By Sorakana')
print(h)
key = input("続行するにはエンターキーを押してください _ _ _")
os.system('cls')

while True:
    a = input('チート名: ')
    b = input('チート作者名: ')
    c = input('コード(一行): ')
    e = c[18:]
    hex_be = e
    bytes_be = binascii.unhexlify(hex_be)
    bytes_le = bytes_be[::-1]
    hex_le = binascii.hexlify(bytes_le).decode()
    z = c[:17]
    zz = z[9:]
    bb = '[' + b + ']'
    print('// ' + a + ' ' + bb)
    print(hex_le.upper() + ' ' + zz)
    ans = input('ほかのコードを変換しますか?[y/n]')        
    if ans == "n":
        break
