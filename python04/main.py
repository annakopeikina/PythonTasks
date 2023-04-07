print("Введите размер длины шоколадки в дольках: ")
h = int(input())
print("Введите размер ширины шоколадки в дольках: ")
w = int(input())
print("Введите, сколько долек отломить: ")
k = int(input())
if k < h*w and (k % h == 0 or k % w == 0):
    print("Можно")
else:

    print("Нельзя")
