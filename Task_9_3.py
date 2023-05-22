f = open("text.txt", 'r', encoding = 'utf-8')
s = f.readlines()
d=''
for i in s:
    d += str(i).lower()
print(d)
f.close()

import collections
a = collections.Counter(d)
b = dict(a)
f = (sorted(b.items(), key = lambda x: (-x[1], x[0]))[:10])
print(f)
for k,v in f:
    print(f'{k} - {v}')
