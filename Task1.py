'''Задача 16: Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. 
Последняя строка содержит число X
5
1 2 3 4 5
3 
-> 1'''

print('Введите кол-во цифр: ')
x = int(input())
c = 0
list = list()
print('Введите числа в массив: ')
for i in range(x):
    
    list.append(int(input()))
    
print(list)

print('Какое число хотите найти?')
n = int(input())

for i in range(x):
    if n == list[i]:
        c += 1

print("Чисел", n, "в массиве -", c)