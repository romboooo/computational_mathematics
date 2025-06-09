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

def isRootExists(a, b, choice) -> bool:
    return func(a, choice) * func(b, choice) < 0

def xicount(a,b,choice):
    return (a * func(b,choice) - b * func(a,choice))/(func(b,choice) - func(a,choice))

def method(a, b, choice, epsilon):
   

    print("\n| Итерация |   a      |   b      |    x     |   f(a)   |   f(b)   |   f(x)   |")
    print("|----------|----------|----------|----------|----------|----------|----------|")
    iteration = 1
    while True:
        xi = xicount(a,b,choice)
        fx = func(xi, choice)

        if func(a,choice) * func(xi,choice) < 0:
            b = xi
        elif func(b,choice) * func(xi,choice) < 0:
            a = xi

        print(f"| {iteration:8d} | {a:8.5f} | {b:8.5f} | {xi:8.5f} | {func(a,choice):8.5f} | {func(b,choice):9.5f} | {fx:.5f} | ")

        if abs(fx) < epsilon:
            break

        iteration += 1
        if iteration > 100:
            print("Достигнут лимит итераций!")
            break

    print("\nРезультат:")
    print(f"Найденный корень: x = {xi:.5f}")
    print(f"Значение функции в заданной точке: f(x) = {func(xi,choice):.15f}")

    print(f"Количество итераций: {iteration}")

def choose_equation():
    while True:
        print("\nВыберите уравнение:")
        print("1: 2.74x³ - 1.93x² - 15.28x - 3.72 = 0")
        print("2: x³ - x + 4 = 0")
        print("3: sin(x) - e⁻ˣ = 0")
        choice = input("Введите номер уравнения (1-3): ")
        if choice in {'1', '2', '3'}:
            return int(choice)
        print("Ошибка: введите число от 1 до 3.")

def count_roots(a, b, choice, steps=1_000):
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

def premain(choice):
    try:
        a, b = map(float, input("a b: ").split())
    except Exception:
        print("введите a и b корректно")
        premain(choice)
        return
    if a > b:
        temp = a
        a = b 
        b = temp
        print(f"введено а, большее b. границы изменены: а = {a}, b = {b}")
    if a == b:
        print("a = b, введите корректные данные")
    if count_roots(a,b,choice) == 0:
        print("\nНа данном интервале нет корней.")
        premain(choice)
    elif count_roots(a,b,choice) == 1:
        epsilon = float(input("Введите точность ε: "))
        method(a, b, choice, epsilon)
        return
    elif count_roots(a,b,choice) > 0:
        print("\nНа данном интервале больше одного корня. Введите интервал поменьше")
        premain(choice)     


def main():
    choice = choose_equation()
    print("\nВведите интервал изоляции корня [a, b]:")
    premain(choice)


if __name__ == "__main__":
    main()