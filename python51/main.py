# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#    A = 2; B = 3 -> 8

# import math
# num_A = int(input("Введите число: "))
# num_B = int(
#    input("Введите число равное степени, в которое нужно ввозвести первое число: "))
# n = pow(num_A, num_B)
# print("Число", num_A, "возведенное в степень", num_B, "равно", n)
num_A = int(input("Введите число: "))
num_B = int(input("Введите число степени: "))


def pow(num_A, num_B):
    if num_B == 0:
        return 1
    else:
        return num_A * pow(num_A, num_B - 1)


result = pow(num_A, num_B)
print(result)
