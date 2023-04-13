print("введите натуральное число, задающее предел чисел степени числа 2")
n = int(input())
k = 1
while k <= n:
    if k == n:
        break
    k = k + 1
else:
    print("block")

print(pow(2, k))
