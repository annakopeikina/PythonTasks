# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)

import random
print("задайте количество чисел в массиве: ")
n = int(input())
list = [random.randint(1, n) for _ in range(n)]
print(list)

for i in list:  # transform boolean in to digit comparison
    compare = []
    idx = list.index(i)
    for j in range(len(list)):
        if (idx == j):
            continue
        else:
            compare.append(i > list[j])
print(compare)

count = list[0]  # transform find smollest in comparison
for m in list:
    if (count == m):
        continue
    elif (count > m):
        count = m
print(count)
