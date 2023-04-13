import math
from math import sqrt
import random
x = random.randint(1, 1000)
y = random.randint(1, 1000)
print("Катя, сумма задуманных Петей чисел равна",
      (x + y), "а их произведение равно", (x * y))
n = (x + y)
m = (x * y)  # выражаем x через систему уравнений
# x=m-y; (m-y)*y=m; ny-y**=m
# y**2-ny+m=0; D=n**2 + 4m
# if D < 0 -корней нет
# if D = 0, то y=n/2, x=n-y=n/2
# if D > 0, тогда два корня
# y1=(n+rootdisc):(2*1)
# y2=(n-rootdisc):(2*1)

discr = n ** 2 + 4*m
root = sqrt(discr)
print("Дискриминант D =", discr)
if discr > 0:
    y == (n - math.sqrt(discr))/2
    if n - y == x & x > 0:
        print("Y =", y, "X =", n - y)
    else:
        print("Y =", y == (n + math.sqrt(discr))/2,
              ";X =", n - y)
elif discr == 0:
    y == n / 2
    print("y = ", y, "x = ", y)
elif discr < 0:
    print("уравнение не имеет решения")
