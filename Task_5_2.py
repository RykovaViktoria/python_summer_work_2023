n = int(input())
f=[]
for i in range(1, n+1):
    if n % i ==0:
        f.append(i)
    else: None
print(f)
# m=max(f)
# print(m)
# s=[]
# for i in (2,m+1):
#     c=0
#     if f[c]%i ==0:
#         c += 1
#     else:
#         s.append(f[c])
#         c += 1
# print(s)




