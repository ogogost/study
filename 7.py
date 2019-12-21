data = [2, 3, 5, 7, 54]
summa = 0
for number in data:
    print(number)
    summa += number

print(summa)
print(sum(data))

zeros = [0, 0] * 15
print(zeros)
print(zeros + data)


# посчитать кол-во положительных элементов в списке
# [1, -3, 2, -3]  -> 2

data = [1, -3, 2, -3, 2, 1, 67]

positive = 0
for number in data:
    if number > 0:
        positive += 1
print('кол-во положительных элементов:', positive)


#напечатать все четные элементы из списка

for number in data:
    if number % 2 == 0:
        print(number)

#напечатать элементы на четных позициях в списке
for i in range(len(data)):
    if i % 2 != 0:
        print(data[i])

print(data[::2])

#среднее арифметическое элементов массива

#print(sum(data)//)

#напечатать все строки, длина которых больше 5

