import random
a = random.randint(100000, 999999)
# a = 123123 (check happy version)
print("Билет с номером ", a)
if (a//100000 + a//10000 % 10 + a//1000 % 10) == (a//100 % 10 + a//10 % 10 + a % 10):
    print("СЧАСТЛИВЫЙ!")
else:
    print("несчастливый")
