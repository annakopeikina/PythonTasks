# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)

import random
print("задайте количество чисел в массиве; ")
n = int(input())
list = [random.randint(1, n) for _ in range(n)]
print(list)

for i in list:
    compare = []
    idx = list.index(i)
    for j in range(len(list)):
        if (idx == j):
            continue
        compare.append(i > list[j])
print(compare)

count = list[0]
for m in list:
    if (count < m):
        count = m
print(count)
