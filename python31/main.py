# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)

import random
print("задайте количество чисел в массиве: ")
n = int(input())
list = [random.randint(1, n) for _ in range(n)]
print(list)
count = 0
for i in range(len(list) - 1):
    if list[i + 1] > list[i]:
        count += 1
    if list[i] < list[i + 1]:
        print(f"{list[i]} < {list[i + 1]}")
print(count)
