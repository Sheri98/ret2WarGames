import interact 

# Creating PIPE
p = interact.Process()

# Recieving till the end of Name
# Name can be retrieved by following address in data
# for Serial Number we need to decodeFunction for name
rec_data = p.readuntil('name:')
p.sendline('Bob')
data = p.readuntil('number:')
p.sendline('134032')
p.interactive()

'''
def decode_function():
    name = 'Bob' #(replace the name here)
    result = 16705
    for i in range(1280):
        result+=ord(name[i%len(name)])
    print(result)

'''

