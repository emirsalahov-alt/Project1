import random
m='abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+-/*!&$#?=@'
i = int(input('Lenght?'))
pas = ''
for o in range(i):
    pas+=random.choice(m)
print(pas)   