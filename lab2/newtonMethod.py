import math
import sys
import os

def func(x,choice):
    if choice == 1:
        return 2.74 * x ** 3 - 1.93 * x ** 2 - 15.28 * x - 3.72
    if choice == 2:
        return x**3 - x + 4
    if choice == 3:
        return math.sin(x) - math.exp(-x)
def diffFunc(x,choice):
    if choice == 1:
        return 8.22 * x**2 - 3.86 * x - 15.28  
    if choice == 2:
        return 3*x**2 - 1
    if choice == 3:
        return math.cos(x) + math.exp(-x)
def doubleDiffFunc(x,choice):
    if choice == 1:
        return 16.44 * x - 3.86 
    if choice == 2:
        return 6*x
    if choice == 3:
        return -math.sin(x) - math.exp(-x)

def is_sign_consistent(func, a, b, num_points=1000):
    if a > b:
        a, b = b, a
    if a == b:
        val = func(a)
        return val != 0
    
    step = (b - a) / (num_points - 1)
    prev_val = func(a,choice)
    if prev_val == 0:
        return False
    prev_sign = 1 if prev_val > 0 else -1
    
    for i in range(1, num_points):
        x = a + i * step
        current_val = func(x,choice)
        if current_val == 0:
            return False
        current_sign = 1 if current_val > 0 else -1
        if current_sign != prev_sign:
            return False
        prev_sign = current_sign
    return True

def convergenceCondition(a, b):
    if not is_sign_consistent(diffFunc, a, b):
        return False
    if not is_sign_consistent(doubleDiffFunc, a, b):
        return False
    return True

def xiCount(x,choice):
    return x - (func(x,choice)/diffFunc(x,choice))

def x0Count(a,b,choice): 
    x0 = (a+b)/2
    if(func(a,choice)*doubleDiffFunc(a,choice) > 0):
        x0 = a
    elif(func(b,choice)*doubleDiffFunc(b,choice) > 0):
        x0 = b

    if(func(x0, choice) * doubleDiffFunc(x0,choice) > 0):
        print("𝑓(𝑥0)∙ 𝑓′′(𝑥0) > 0 выполняется => метод обеспечивает быструю сходимость")
    else:
        print("𝑓(𝑥0)∙ 𝑓′′(𝑥0) > 0 не выполняется => метод не обеспечивает быструю сходимость")

    return x0

def newtonMethod(a,b,epsilon,choice):
    i = 1
    x0 = x0Count(a, b,choice)  
    xi = x0
    while(True):
        print(f"итерация номер {i}")
        fxi = func(xi,choice)
        fdiffxi = diffFunc(xi,choice)
        xi1 = xiCount(xi,choice)

        print("|--xi--|--f(xi)--|--f'(xi)--|--x(i+1)--|--|Xi+1 - Xi|--|")
        print(f"{xi:7f} {fxi:7f} {fdiffxi:7f} {xi1:7f} {abs(xi1 - xi):7f}")
        if(abs(xi1 - xi) < epsilon) or (abs(fxi) < epsilon):
            break
        i+=1
        xi = xi1
        if(i > 10):
            print("превышен лимит итераций")
            break

def isRootExists(a,b,choice):
    return func(a,choice)*func(b,choice) < 0

def choice():
    print(f"выберите уравнениe:")
    print("1:")
    print("2.74x^3 - 1.93x^2 - 15.28x - 3.72 = 0")
    print("2:")
    print("x^3 - x + 4 = 0")
    print("3:")
    print("sin(x) - exp^-x = 0")
    choice = int(input())
    if(choice in [1, 2, 3]):
        return choice
    else:
        print("такого варианта нет :(")
        choice()

choice = choice()

print("введите интервал изоляции корня. Два числа через пробел a0 b0 ")
a, b = map(int, input().split())
if not isRootExists(a, b,choice):
    print(f"на отрезке [{a},{b}] нет корней либо больше одного (попробуйте сузить интервал)")
    # os.system("sudo shutdown -h now")
    sys.exit(0)
epsilon = float(input("введите точность \n"))

if convergenceCondition(a,b):
    print("условие сходимости выполняется, метод ньютона эффективен")
else:
    print("условие сходимости не выполняется, метод ньютона неэффективен")

newtonMethod(a,b,epsilon,choice)

