# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

import random
print("введите количество чисел в масcиве: ")
n = int(input())
list_A = [random.randint(1, n) for _ in range(n)]
print(list_A)
print("задайте число для сравнения с числами массива: ")
x = int(input())
min = abs(x - list_A[0])
index = 0
for i in range(1, n):
    count = abs(x - list_A[i])
    if count < min:
        min = count
        index = i
print(list_A[i])
