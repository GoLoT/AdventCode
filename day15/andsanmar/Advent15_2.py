a = 883
b = 879
c = 0
for i in range(5*10**6):
    if((a % 2**16) == (b % 2**16)):
        c += 1
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    while(not a % 4 == 0):
        a = (a * 16807) % 2147483647
    while(not b % 8 == 0):
        b = (b * 48271) % 2147483647
print(c)
