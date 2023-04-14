import random
print("введите количество чисел в масиве: ")
n = int(input())
list = [random.randint(1, n) for _ in range(n)]
print(list)
print("введите искомое число для поиска его повторений: ")
x = int(input())
count = list.count(int(x))
print(count)
