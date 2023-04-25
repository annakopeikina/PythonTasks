# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума
import random
list = [random.randint(2, 22) for _ in range(22)]
print(list)
index = []
for i in range(len(list)):
    if 8 <= list[i] <= 13:
        index.append(i)
print(index)

# import random
# list = [random.randint(1,1000) for _i in range(1000)]
# index = [i for i in range(len(list)) if 220 <= list[i] <=888]
# print(index)

# import random
# list = [random.randint(1,100) for _i in range(100)]
# result = find_indexes(list,19,22)
# print(result)
