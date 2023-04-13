import random
print("Введите количество монет ")
m = int(input())
a = random.randint(0, m)  # количество монет с гербом
print(a, "монет(a) с гербом")
if a < m/2:
    if a == 1:
        print("Переверните одну монету")
    elif a < 5:
        print("Переверните", a, " монеты")
    elif a > 5:
        print("Переверните", a, " монет")
elif (m - a) < (m / 2):
    if (m - a) == 1:
        print("Переверните одну монету")
    elif (m - a) < 5:
        print("Переверните", (m - a), " монеты")
    elif (m - a) > 5:
        print("Переверните", (m - a), " монет")
else:
    print("Ничего не нужно переворачивать")

# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
#   x = int(input())
#   if x == 0:
#       count_zero += 1
#   else:
# count_one += 1
# if count_one > count_zero:
#   print(count_zero)
# else:
#   print(count_one)
