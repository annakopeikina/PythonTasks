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
