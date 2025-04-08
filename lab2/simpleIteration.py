import math
import sys

def cube_root(x):
    return math.copysign(abs(x) ** (1/3), x)

def func(x, choice):
    if choice == 1:
        return 2.74 * x ** 3 - 1.93 * x ** 2 - 15.28 * x - 3.72
    if choice == 2:
        return x**3 - x + 4
    if choice == 3:
        return math.sin(x) - math.exp(-x)

def fi(x, choice):
    if choice == 1:
        return (2.74 * x**3 - 1.93 * x**2 - 3.72) / 15.28
    if choice == 2:
        return cube_root(x - 4)
    if choice == 3:
        return math.asin(math.exp(-x))

def diffFi(x, choice):
    if choice == 1:
        return (8.22 * x**2 - 3.86 * x) / 15.28
    if choice == 2:
        return (1/3) * (x - 4) ** (-2/3)
    if choice == 3:
        return -math.exp(-x) / math.sqrt(1 - math.exp(-2*x))

def convergenceCondition(a, b, choice):
    max_deriv = max(abs(diffFi(a, choice)), abs(diffFi(b, choice)))
    if max_deriv >= 1:
        print("Итерационная последовательность может не сходиться.")
    elif math.isclose(max_deriv, 1, abs_tol=0.1):
        print("Скорость сходимости низкая.")
    else:
        print("Условие сходимости выполняется.")

def count(a, b, epsilon, choice):
    xi = (a + b) / 2
    i = 1
    while True:
        print(f"итерация номер {i}")

        try:
            xi1 = fi(xi, choice)
        except ValueError as e:
            print(f"Ошибка вычисления: {e}. Итерации прерваны.")
            return
        fxi1 = func(xi1, choice)
        try:
            fixi1 = fi(xi1, choice)
        except ValueError:
            fixi1 = float('nan')
            
        mod = abs(xi1 - xi)
        print("|--xi--|--x+i--|--𝝋(xi+1)--|--f(x(i+1))--|--|Xi+1 - Xi|--|")
        print(f"{xi:7.5f} {xi1:7.5f} {fixi1:7.5f} {fxi1:7.5f} {mod:7.5f}")
        if abs(xi1 - xi) < epsilon or abs(fxi1) < epsilon:
            break
        i += 1
        if i > 15:
            print("Превышен предел итераций.")
            break
        xi = xi1

def get_choice():
    while True:
        print("Выберите уравнение:")
        print("1: 2.74x^3 - 1.93x^2 - 15.28x - 3.72 = 0")
        print("2: x^3 - x + 4 = 0")
        print("3: sin(x) - exp(-x) = 0")
        try:
            choice = int(input())
            if choice in (1, 2, 3):
                return choice
            else:
                print("Нет такого варианта. Введите 1, 2 или 3.")
        except ValueError:
            print("Введите целое число.")

def get_interval(choice):
    while True:
        print("Введите интервал изоляции корня (два числа через пробел a b): ")
        try:
            a, b = map(float, input().split())
            if a > b:
                a, b = b, a
            if choice == 3 and (a < 0 or b < 0):
                print("Для уравнения 3 интервал должен быть неотрицательным.")
                continue
            return a, b
        except ValueError:
            print("Ошибка ввода. Введите два числа через пробел.")
def isRootExists(a,b,choice)->bool:
    return func(a,choice)*func(b,choice) < 0

choice = get_choice()
a, b = get_interval(choice)
if(not isRootExists(a,b,choice)):
    print("корней нет")
    sys.exit(0)
epsilon = float(input("Введите точность: "))
convergenceCondition(a, b, choice)
count(a, b, epsilon, choice)