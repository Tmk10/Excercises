"""Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string."""

import zlib

value = bytes("hello world!hello world!hello world!hello world!","utf-8")
compressedvalue = zlib.compress(value)
print(compressedvalue)
print(zlib.decompress(compressedvalue))


