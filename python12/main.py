from math import sqrt
import random
x = random.randint(1, 10)
y = random.randint(1, 10)
print("Катя, сумма задуманных Петей чисел равна",
      (x + y), "а их произведение равно", (x * y))
n = int(x + y)
m = int(x * y)  # выражаем x через систему уравнений
# x=m-y; (m-y)*y=m; ny-y**=m
# y**2-ny+m=0; D=n**2 + 4m
# if D < 0 -корней нет
# if D = 0, то y=n/2, x=n-y=n/2
# if D > 0, тогда два корня
# y1=(n+rootdisc):(2*1)
# y2=(n-rootdisc):(2*1)
disc = n ** - 4*m
root = sqrt(disc)
if disc < 0:
    print("уравнение не имеет решения")
elif disc == 0:
    print("x=", n/2, "y=", n/2)
elif disc > 0:
    if (n - root) <= 0:
        print("уравнение не имеет решения")
    else:
        print("Y=", y, "X=", n-y)
