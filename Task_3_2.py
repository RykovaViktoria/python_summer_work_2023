n=input('Введите число -->')
for i in range(10):
    a = n.count(str(i))
    print(f'{i} - {a}')