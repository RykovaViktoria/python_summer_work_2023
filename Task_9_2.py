x = list(input('Введите слово -->'))
print(x)
n = int(input('Введите количество слов для сравнения:'))
words = list(map(str, input('Введите слова -->').split(', ')))
print(words)
gl = "ауоыиэяюёе"
place = ''
for i in range(len(x)):
    if x[i] in gl:
        place += str(i)
# print(place)

def check(y):
    place1 = ''
    for i in range(len(y)):
        if y[i] in gl:
            place1 += str(i)
    return place1

lst = []
for i in words:
    s = list(i)
    if check(s) == place:
        r = ''.join(s)
        lst.append(r)

print(', '.join(lst))




