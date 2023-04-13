print("введите натуральное число, задающее предел чисел степени числа 2")
n = int(input())
k = 1
while (2 ** k) < n:
    print(2 ** k)
    k = k + 1
    if (2 ** k) >= n:
        break

# n = int(input())
# i = 0
# while 2 ** i <= n:
#   print(2 ** i)
#   i += 1
