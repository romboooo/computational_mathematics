import math
import numpy as np

def func(x, choice):
    if choice == 1:
        return 2.74 * x ** 3 - 1.93 * x ** 2 - 15.28 * x - 3.72
    if choice == 2:
        return x**3 - x + 4
    if choice == 3:
        return math.sin(x) - math.exp(-x)

def diffFunc(x, choice):
    if choice == 1:
        return 8.22 * x**2 - 3.86 * x - 15.28  
    if choice == 2:
        return 3*x**2 - 1
    if choice == 3:
        return math.cos(x) + math.exp(-x)

def doubleDiffFunc(x, choice):
    if choice == 1:
        return 16.44 * x - 3.86 
    if choice == 2:
        return 6*x
    if choice == 3:
        return -math.sin(x) - math.exp(-x)

def convergenceCondition(a, b, choice):
    return countRootsForDiff(a,b,choice) == 0 == countRootsForDoubleDiff(a,b,choice)


def xiCount(x, choice):
    return x - (func(x, choice)/diffFunc(x, choice))

def x0Count(a, b, choice): 
    x0 = (a + b) / 2
    fa = func(a, choice)
    dda = doubleDiffFunc(a, choice)
    fb = func(b, choice)
    ddb = doubleDiffFunc(b, choice)
    
    if fa * dda > 0:
        x0 = a
    elif fb * ddb > 0:
        x0 = b
    
    if func(x0, choice) * doubleDiffFunc(x0, choice) > 0:
        print("𝑓(𝑥0)∙ 𝑓′′(𝑥0) > 0 выполняется => метод обеспечивает быструю сходимость")
    else:
        print("𝑓(𝑥0)∙ 𝑓′′(𝑥0) > 0 не выполняется => метод не обеспечивает быструю сходимость")
    return x0

def newtonMethod(a, b, epsilon, choice):
    i = 1
    x0 = x0Count(a, b, choice)  
    xi = x0

    print("\n|--Итерация--|-----xi-----|----f(xi)-----|---f'(xi)-----|----x(i+1)----|--|xi+1 - xi|--|")
    print("|------------|------------|--------------|--------------|--------------|---------------|")
    while True:
        fxi = func(xi, choice)
        fdiffxi = diffFunc(xi, choice)
        xi1 = xiCount(xi, choice)

        print(f"| {i:8d}   | {xi:10.5f} | {fxi:12.5f} | {fdiffxi:12.5f} | {xi1:12.5f} | {abs(xi1 - xi):12.5f}  | ")

        if abs(fxi) < epsilon and abs(xi1 - xi) < epsilon:
            print(f"Найден корень: xi = {xi1:.6f}, f(xi) = {func(xi1, choice):.15f}, итераций: {i}")
            break
        i += 1
        if i > 100:
            print("Достигнут максимальный лимит итераций")
            break

        xi = xi1
        

def countRoots(a, b, choice, steps=1_000):
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

def countRootsForDiff(a, b, choice, steps=1_000):
    xs = np.linspace(a, b, steps)
    values = []
    for x in xs:
        try:
            values.append(diffFunc(x,choice))
        except Exception:
            values.append(np.nan)
    sign_changes = 0
    for i in range(1, len(values)):
        if np.isnan(values[i - 1]) or np.isnan(values[i]):
            continue
        if values[i - 1] * values[i] < 0:
            sign_changes += 1
    return sign_changes

def countRootsForDoubleDiff(a, b, choice, steps=1_000):
    xs = np.linspace(a, b, steps)
    values = []
    for x in xs:
        try:
            values.append(doubleDiffFunc(x,choice))
        except Exception:
            values.append(np.nan)
    sign_changes = 0
    for i in range(1, len(values)):
        if np.isnan(values[i - 1]) or np.isnan(values[i]):
            continue
        if values[i - 1] * values[i] < 0:
            sign_changes += 1
    return sign_changes


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

            changes = countRoots(a, b, choice)
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

def main():
    choice = get_choice()
    a, b = get_interval(choice)
    epsilon = float(input("Введите точность ε: "))
    if convergenceCondition(a, b, choice):
        print("Условия сходимости выполняются, метод Ньютона применим.")
    else:
        print("Условия сходимости не выполняются, метод Ньютона может не сойтись.")

    newtonMethod(a, b, epsilon, choice)
if __name__ == "__main__":
    main()
