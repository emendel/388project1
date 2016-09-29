from roots import *
import hashlib
import sys
message = sys.argv[1] # eecs388+alexthal+1.23

m = hashlib.sha1()
m.update(message)
digest = m.hexdigest()
digest_int = int(digest, 16)
digest_hex_str = hex(digest_int)
digest_hex_str = digest_hex_str[2:(len(digest_hex_str) - 1)]

e = 3
f = "ff"
arbitrary = '00' * 217
hex_string = "0x0001" + f + "003021300906052b0e03021a05000414" + digest_hex_str + arbitrary
print hex_string
decimal_int = int(hex_string, 16)
print decimal_int
cuberoot = integer_nthroot(decimal_int, e)[0] + 1

print cuberoot
print integer_to_base64(cuberoot)