import matplotlib.pyplot as plt
import numpy as np


def build_difference_table(x, y):
    n = len(x)
    diff_table = [[0] * n for _ in range(n)]
    for i in range(n):
        diff_table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]
    return diff_table


def print_difference_table(x, diff_table):
    n = len(x)
    print("\nТаблица конечных разностей:")
    print("x".ljust(10), end="")
    for i in range(n):
        print(f"Δ^{i}y".ljust(15), end="")
    print()
    for i in range(n):
        print(f"{x[i]:<10.4f}", end="")
        for j in range(n - i):
            print(f"{diff_table[i][j]:<15.6f}", end="")
        print()


def calculate_newton_forward(x, y, x_, diff_table):
    n = len(x)
    h = x[1] - x[0]
    t = (x_ - x[0]) / h

    result = diff_table[0][0]
    term = t
    factorial = 1
    print("Конечные разности, задающие многочлен")
    print(result)
    for i in range(1, n):
        delta = diff_table[0][i]
        result += term * delta / factorial
        term *= t - i
        factorial *= i + 1
        print(delta)

    return result, t


def calculate_newton_backward(x, y, x_, diff_table):
    n = len(x)
    h = x[1] - x[0]
    t = (x_ - x[-1]) / h

    diff_table_rev = []
    for k in range(n):
        i = n - 1 - k
        if k < len(diff_table[i]):
            diff_table_rev.append(diff_table[i][k])

    result = diff_table_rev[0]
    term = 1
    factorial_val = 1
    print("Конечные разности, задающие многочлен")
    print(result)
    for i in range(1, len(diff_table_rev)):
        term = term * (t + i - 1)
        factorial_val *= i
        delta = diff_table_rev[i]
        result += term * delta / factorial_val
        print(delta)

    return result, t


def newtonWithFiniteDifferences(x, y, x_):
    if len(x) != len(y):
        raise ValueError("Ошибка: массивы x и y должны иметь одинаковую длину")

    h = x[1] - x[0]
    for i in range(1, len(x) - 1):
        if abs((x[i + 1] - x[i]) - h) > 1e-6:
            raise ValueError("Ошибка: сетка должна быть равномерной")

    diff_table = build_difference_table(x, y)
    print_difference_table(x, diff_table)

    mid_point = (x[0] + x[-1]) / 2

    print(f"\nx0 = {x_}")
    if x_ <= mid_point:
        print("\nПрименена формула Ньютона ВПЕРЁД")
        result, t_val = calculate_newton_forward(x, y, x_, diff_table)
        base = x[0]
    else:
        print("\nПрименена формула Ньютона НАЗАД")
        result, t_val = calculate_newton_backward(x, y, x_, diff_table)
        base = x[-1]

    print(
        f"t = (x - {'x0' if x_ <= mid_point else 'xn'})/h = ({x_} - {base})/{h} = {t_val:.6f}"
    )
    print(f"\nФинальный результат: N({x_}) = {result:.6f}")

    # draw_graph(x, y, result,mid_point, diff_table,x_)

    return result


def draw_graph(x, y, result, mid_point, diff_table, x_):
    plt.figure(figsize=(10, 6))

    plt.scatter(x, y, color="red", zorder=5, label="Исходные данные")

    plt.scatter(
        [x_],
        [result],
        color="green",
        zorder=5,
        label=f"Точка интерполяции (x={x_}, y={result:.4f})",
    )

    x_min, x_max = min(x), max(x)
    x_range = np.linspace(x_min, x_max, 1000)
    y_range = []

    for point in x_range:
        if point <= mid_point:
            y_val, _ = calculate_newton_forward(x, y, point, diff_table)
        else:
            y_val, _ = calculate_newton_backward(x, y, point, diff_table)
        y_range.append(y_val)

    plt.plot(x_range, y_range, label="Интерполяционный многочлен Ньютона", color="blue")

    plt.title("Интерполяция методом Ньютона")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()

    plt.savefig("newton_interpolation.png", dpi=300)
    # plt.show()
