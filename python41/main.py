# Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит
# сами элементы множеств.
print("Введите количество элементов первого множества: ")
n = int(input())
print("Введите количество элементов второго множества: ")
m = int(input())
print("Заполните первое множество неупорядоченными целыми числами через пробел (может быть, с повторениями)")
set1 = set(map(int, input().split()))
print("Сделайте то же для второго множества: ")

set2 = set(map(int, input().split()))
set_1 = set(set1)
set_2 = set(set2)
result = set()

for x in set_1:
    if x in set_2:
        result.add(x)
print(*sorted(result))


# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#    set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#    set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#    print(i, end=' ')
