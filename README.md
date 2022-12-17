# 7z crc cracker

Is a python script to recover plaintext of files based on their CRC32. Compressed files contains CRC32 (checksums) of the plaintext files. If the file is short enough, like 4 bytes, it is fairly easy to try all possible combinations to obtain the same CRC32 value.

I don't really think this is useful in a real world scenario, however this might be used in certain CTF challenges.

**Do you like this project? Become a sponsor!**

[![sponsor](https://img.shields.io/badge/-Become%20a%20sponsor%20❤-ff6964)](https://github.com/sponsors/mgp25)

 ## Test

 ```
 python 7zcrc_cracker.py archive.7z

[*] Found vulnerable file to CRC32 bruteforcing!
Filename: file1
CRC32: 0x69ecf2f0

<=================================================>

[!] Cracked plaintext for file!
Filename: file1
Plaintext: YnVp
```
