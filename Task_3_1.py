average = []
sum = 0
while True:
    n=int(input("Введите зарплату -->"))
    average.append(n)
    sum += n
    if n > 0:
        continue
    else: break
print('Средняя зарплата =', sum/len(average))
