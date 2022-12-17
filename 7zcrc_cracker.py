import sys
import zlib
import py7zr
import string
from itertools import product

if len(sys.argv) < 2:
    print('Usage: 7zcrc_cracker.py <7z_file>')
    exit()


file_list = []
crc_list = []
cracked = 0

try:
    archive = py7zr.SevenZipFile(sys.argv[1], mode='r')
except:
    print('[x] Invalid 7z provided!')
    exit()
archive_list = archive.list()
print('')
for archive in archive_list:
    if archive.uncompressed == 4:
        print('\033[1m\033[92m[*] Found vulnerable file to CRC32 bruteforcing!\033[0m')
        print('\033[1m\033[94mFilename:\033[0m {}'.format(archive.filename))
        print('\033[1m\033[94mCRC32:\033[0m {}'.format(hex(archive.crc32)))
        print('')
        file_list.append(archive.filename)
        crc_list.append(hex(archive.crc32))

all_char = string.printable

for l in range(5):
    generator = product(all_char, repeat=int(l))

print('\033[1;33m<=================================================>\033[0m')
print('')

for p in generator:
    pt = ''.join(p)
    crc = hex(zlib.crc32(pt.encode('utf8')) & 0xffffffff)
    if crc in crc_list:
        print('\033[1m\033[92m[!] Cracked plaintext for file!\033[0m')
        print('\033[1m\033[94mFilename: {}'.format(file_list[crc_list.index(crc)]))
        print('\033[1m\033[94mPlaintext: {}'.format(pt))
        print('')
        cracked += 1
        if cracked == len(crc_list):
            exit()