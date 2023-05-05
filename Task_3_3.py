n=input('Введите фразу -->')
s=n.split()
lst=[]
for i in range(len(s)):
    lst.append(s[i])
a = sorted(lst, key=len)
print(f'Самое длинное слово - {a[-1]}')





