# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)
import random
print("задайте количество чисел в массиве; ")
n = int(input())
list = [random.randint(1, n) for _ in range(n)]
print(list)
i = 0
count = 0


for i in range(n + 1):
    a = list[i]
    b = list[i+1]
    if n < (i + 1):
        break
    for count in range(n):
        if a < b:
            count = count + 1
            i += 1
print(count)
