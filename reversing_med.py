import interact

p = interact.Process()

# found at address 0x601080 in your Data tab 
# Target bytes extracted from 0x601080
target_bytes = [
    0x75, 0x3a, 0xc0, 0xc8, 0x33, 0xcf, 0xcc, 0x2e, 
    0xcc, 0xc7, 0x17, 0xec, 0xb0, 0x37, 0xeb, 0x9b,
    0x70, 0xe6, 0x8c, 0x63, 0xa7
]

password = ""

for i in range(21):
    # Match the 32-bit imul truncation logic
    xor_key = (i * 0x54) & 0xFF
    
    # Reverse the XOR operation
    original_char = target_bytes[i] ^ xor_key
    password += chr(original_char)

p.readuntil('Enter password:')
p.sendline(password)
p.interactive()