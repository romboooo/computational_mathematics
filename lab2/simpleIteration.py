import math
import numpy as np


def func(x, choice):
    if choice == 1:
        return 2.74 * x**3 - 1.93 * x**2 - 15.28 * x - 3.72
    if choice == 2:
        return x**3 - x + 4
    if choice == 3:
        return math.sin(x) - math.exp(-x)


def df(x, choice):
    if choice == 1:
        return 2.74 * 3 * x**2 - 1.93 * 2 * x - 15.28
    elif choice == 2:
        return 3 * x**2 - 1
    elif choice == 3:
        return math.cos(x) + math.exp(-x)


def getLambda(a,b,choice):
    if max(df(a,choice), df(b,choice)) < 0:
        print(f"lamda = {-1 / max(df(a,choice), df(b,choice))}")
        return -1 / max(df(a,choice), df(b,choice))
    else: 
        print(f"lamda = {1 / max(df(a,choice), df(b,choice))}")
        return 1 / max(df(a,choice), df(b,choice))


def convergenceCondition(a, b, choice):
    x = (a + b) / 2
    lam = getLambda(a,b,choice)

    diffFi = lambda x: 1 + lam * df(x,choice)

    try:
        if abs(diffFi(x, choice)) >= 1:
            print("Условие сходимости не выполняется.")
            return False
        else:
            print("Условие сходимости выполняется.")
            return True
    except:
        print("Невозможно проверить условие сходимости.")
        return False


def count(a, b, epsilon, choice):
    xi = (a + b) / 2
    i = 1
    lam = getLambda(a,b,choice)
    
    fi = lambda x, choice: x + lam*func(x,choice)
    diffFi = lambda x,choice: 1 + lam * df(x,choice)

    print(f"значения 𝝋'(a) = {diffFi(a,choice)}, 𝝋'(b) = {diffFi(b,choice)} ")
    print("\n|--Итерация--|-----xi-----|----xi+1-----|---𝝋(xi+1)-----|----f(xi+1)----|--|xi+1 - xi|--|")
    print("|------------|------------|-------------|---------------|--------------|---------------|")

    while True:
        try:
            xi1 = fi(xi, choice)
        except ValueError as e:
            print(f"Ошибка вычисления: {e}. Итерации прерваны.")
            return
        fxi1 = func(xi1, choice)
        try:
            fixi1 = fi(xi1, choice)
        except ValueError:
            fixi1 = float("nan")

        mod = abs(xi1 - xi)
        print(f"| {i:8d}   | {xi:10.5f} |  {xi1:12.5f} | {fixi1:12.5f} | {fxi1:12.5f} | {abs(xi1 - xi):12.5f}  | ")

        if abs(fxi1) < epsilon and abs(xi1 - xi) < epsilon:
            print(f"Найден корень: xi = {xi1:.6f}, f(xi) = {func(xi1, choice):.15f}, итераций: {i}")
            break
        i += 1
        if i > 50:
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
            if choice == 3:
                if a <= 0 or b > math.pi:
                    print("Для уравнения 3 интервал должен быть в (0, π].")
                    continue

            changes = count_roots(a, b, choice)
            if changes == -1:
                print("Ошибка при вычислении знаков функции на интервале.")
                continue
            if changes == 0:
                print("На данном интервале нет корней. Попробуйте другой интервал.")
                continue
            if changes >= 2:
                print(
                    f"Интервал может содержать несколько корней ({changes} изменений знака). Выберите меньший интервал."
                )
                continue

            return a, b
        except ValueError:
            print("Ошибка ввода. Введите два числа через пробел.")

def count_roots(a, b, choice, steps=10000):
    xs = np.linspace(a, b, steps)
    values = []
    for x in xs:
        try:
            values.append(func(x,choice))
        except Exception:
            values.append(np.nan)
    sign_changes = 0
    for i in range(1, len(values)):
        if np.isnan(values[i - 1]) or np.isnan(values[i]):
            continue
        if values[i - 1] * values[i] < 0:
            sign_changes += 1
    return sign_changes

choice = get_choice()
a, b = get_interval(choice)
epsilon = float(input("Введите точность: "))

if convergenceCondition(a, b, choice):
    count(a, b, epsilon, choice)
else:
    print("Метод простых итераций может не сойтись.")
    count(a, b, epsilon, choice)
