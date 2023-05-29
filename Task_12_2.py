lst = [[i]*i for i in range(1,11)]
s = ''
for i in lst:
    for j in i:
        s+=str(j)
        s += ', '
print(s)

