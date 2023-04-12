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
