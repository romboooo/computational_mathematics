import math
import numpy as np


def func(x, choice):
    if choice == 1:
        return x**3 + 2.28 * x**2 - 1.934 * x - 3.908
    if choice == 2:
        return x**3 - x + 4
    if choice == 3:
        return math.sin(x) - math.exp(-x)


def df(x, choice):
    if choice == 1:
        return 3 * x**2 + 4.56 * x - 1.934
    elif choice == 2:
        return 3 * x**2 - 1
    elif choice == 3:
        return math.cos(x) + math.exp(-x)


def getLambda(a, b, choice):
    # xs = [a + (b - a) * i / 1000 for i in range(1001)]
    xs = np.linspace(
        a, b, 100
    )  # можно не разбивать на 100 кусков просто проверить концы отрезка, мне лень + похуй испралять
    m = max(abs(df(x, choice)) for x in xs)

    maxx = -100000
    for x in xs:
        if (abs(df(x, choice))) > maxx:
            maxx = abs(df(x, choice))
            print(f"x = {x}")

    print(f"max: {maxx}")
    print(f"df(2) = {df(maxx,choice)}")
    print(f"df(2.1) = {df(2.1,choice)}")

    if m == 0:
        raise ValueError("Производная нулевая на всём интервале.")

    all_positive = all(df(x, choice) >= 0 for x in xs)
    all_negative = all(df(x, choice) <= 0 for x in xs)

    if all_positive:
        lam = -1 / m

    elif all_negative:
        lam = 1 / m
    else:
        avg_sign = 1 if (df(a, choice) + df(b, choice)) >= 0 else -1
        lam = -avg_sign / m
        print("Внимание: производная меняет знак. Сходимость не гарантирована.")
    return lam


def convergenceCondition(a, b, choice):
    lam = getLambda(a, b, choice)
    diffFi = lambda x: 1 + lam * df(x, choice)

    try:
        if abs(diffFi(a)) >= 1 and abs(diffFi(b)):
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
    lam = getLambda(a, b, choice)

    fi = lambda x, choice: x + lam * func(x, choice)
    diffFi = lambda x, choice: 1 + lam * df(x, choice)

    print(f"значения 𝝋'(a) = {diffFi(a,choice)}, 𝝋'(b) = {diffFi(b,choice)} ")
    print(
        "\n|--Итерация--|-----xi-----|----xi+1-----|---𝝋(xi+1)-----|----f(xi+1)----|--|xi+1 - xi|--|"
    )
    print(
        "|------------|------------|-------------|---------------|--------------|---------------|"
    )

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

        print(
            f"| {i:8d}   | {xi:10.5f} |  {xi1:12.5f} | {fixi1:12.5f} | {fxi1:12.5f} | {abs(xi1 - xi):12.5f}  | "
        )

        if abs(fxi1) < epsilon and abs(xi1 - xi) < epsilon:
            print(
                f"Найден корень: xi = {xi1:.6f}, f(xi) = {func(xi1, choice):.15f}, итераций: {i}"
            )
            break
        i += 1
        if i > 50:
            print("Превышен предел итераций.")
            break
        xi = xi1


def get_choice():
    while True:
        print("Выберите уравнение:")
        print("1: x^3 + 2.28x^2 - 1.934x - 3.908")
        print("2: x^3 - x + 4")
        print("3: sin(x) - exp(-x)")
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


def count_roots(a, b, choice, steps=1000):
    tol = 1e-8
    fa = func(a, choice)
    fb = func(b, choice)

    if abs(fa) < tol or abs(fb) < tol:
        return 1

    xs = np.linspace(a, b, steps)
    values = []
    for x in xs:
        try:
            values.append(func(x, choice))
        except Exception:
            values.append(np.nan)

    sign_changes = 0
    zero_points = 0

    for i in range(len(values)):
        if not np.isnan(values[i]) and abs(values[i]) < tol:
            zero_points += 1

    for i in range(1, len(values)):
        if np.isnan(values[i - 1]) or np.isnan(values[i]):
            continue
        if values[i - 1] * values[i] < 0:
            sign_changes += 1

    return sign_changes + zero_points


choice = get_choice()
a, b = get_interval(choice)
epsilon = float(input("Введите точность: "))

if convergenceCondition(a, b, choice):
    count(a, b, epsilon, choice)
else:
    print("Метод простых итераций может не сойтись.")
    count(a, b, epsilon, choice)
