from struct import *
from pyfiglet import Figlet
import os

f = Figlet(font='slant')
g = f.renderText('pchtxt 2 ips')
print(g)
h = f.renderText('      By Sorakana')
print(h)
key = input("続行するにはエンターキーを押してください _ _ _")
os.system('cls')

while True:
    infile = input("処理するファイル: ")
    outfile = input("処理後のファイル名: ") + ".ips"

    txt = open(infile, mode='r', encoding="utf-8_sig")
    ips32 = b'IPS32'
    address_offset = 0x100
    output = []

    output.append(ips32)

    txt.readline()

    for line in txt:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        if len(parts) != 2:
            print("convert:", line)
            continue

        addr = int(parts[0], 16) + address_offset
        addr_bytes = addr.to_bytes(4, byteorder='big')
        patch = bytes.fromhex(parts[1])
        patch_size = len(patch).to_bytes(2, byteorder='big')

        output.append(addr_bytes)
        output.append(patch_size)
        output.append(patch)

    output.append(b'EEOF')

    ips_data = b''.join(output)

    with open(outfile, 'wb') as f:
        f.write(ips_data)

    print("処理が完了しました。\nSaved as", outfile)
    ans = input('\n\nほかのコードを変換しますか?[y/n]')        
    if ans == "n":
        break
