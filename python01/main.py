print("Введите трехзначное число: ")
m = (input())
m = [int(digit) for digit in m]
sum = sum(m)
print("Сумма всех чисел в строке равна: ", sum)
