# Напишите рекурсивную функцию recursive_sum(a, b), возвращающую сумму двух
# целых неотрицательных чисел. Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#    4
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))


def recursive_sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return recursive_sum(a, b-1) + 1


result = recursive_sum(a, b)
print(result)
