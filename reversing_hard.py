from interact import Process

lookup = [0xd8, 0x32, 0x5c, 0xef, 0x05, 0x9a]

def solve(challenge):
    encrypted_hash = 0
    for i in range(6):
        encrypted_hash = encrypted_hash << 5
        encrypted_hash ^= ord(challenge[i + 14])

    buf = [0] * 6
    for i in range(6):
        buf[i] ^= ord(challenge[i])
        buf[i] ^= ord(challenge[i + 0x07])
        buf[i] ^= ord(challenge[i + 0x15])
    for i in range(6):
        buf[i] = (buf[i] + 1) & 0xFF
        buf[i] ^= ord(challenge[i + 0x0e])

    hex_value = ''.join('%02X' % b for b in buf)

    new_challenge = challenge[0x1c:]
    third = []
    for i in range(6):
        pro = lookup[i] * ord(new_challenge[i])
        rem = pro % 26
        third.append(chr(rem + ord('A')))

    return "%d:%s:%s" % (encrypted_hash, hex_value, ''.join(third))

p = Process()

for i in range(200):
    p.readuntil("CHALLENGE: ")
    line = p.readuntil("\n")
    challenge = line.strip()
    response = solve(challenge)
    p.sendlineafter("RESPONSE: ", response)

p.interactive()