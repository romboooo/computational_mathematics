import numpy as np

from helpers.interpretationR import interpretR

NAME = 1


def cubeApprox(x, y) -> dict[str, float]:
    print("")
    print("--- Кубическая ---")
    n = len(x)
    sumX = sum(x)
    sumY = sum(y)
    sumX2 = sum(X**2 for X in x)
    sumX3 = sum(X**3 for X in x)
    sumX4 = sum(X**4 for X in x)
    sumX5 = sum(X**5 for X in x)
    sumX6 = sum(X**6 for X in x)
    sumXY = sum(X * Y for X, Y in zip(x, y))
    sumX2Y = sum(X**2 * Y for X, Y in zip(x, y))
    sumX3Y = sum(X**3 * Y for X, Y in zip(x, y))

    A = [
        [n, sumX, sumX2, sumX3],
        [sumX, sumX2, sumX3, sumX4],
        [sumX2, sumX3, sumX4, sumX5],
        [sumX3, sumX4, sumX5, sumX6],
    ]
    B = [sumY, sumXY, sumX2Y, sumX3Y]

    try:
        solution = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        print("Система уравнений вырождена, решение не существует")
        return None
    if solution is not None:
        a0, a1, a2, a3 = solution
    else:
        print("ошибка в вычислении матрицы")

    def polinomModel(x):
        return a0 + a1 * x + a2 * x**2 + a3 * x**3

    fi = []
    ei = []
    S = 0
    fiAverage = 0
    for i in range(n):
        fi.append(polinomModel(x[i]))
        ei.append(fi[i] - y[i])
        S += ei[i] ** 2
        fiAverage += fi[i]

    delta = np.sqrt(S / n)

    fiAverage = 1 / n * sum(fi)

    ss_total = sum((yi - fiAverage) ** 2 for yi in y)

    R2 = 1 - (S / ss_total)

    print(f"Формула: y = {a3:.6f}x³ + {a2:.6f}x² + {a1:.6f}x + {a0:.6f}")
    print(f"Мера отклонения: S = {S:.6f}")
    print(f"Среднеквадратичное отклонение: 𝜹 = {delta:.6f}")
    print(f"Достоверность аппроксимации: R² = {R2:.6f}")

    interpretR(R2)
    return {
        "a0": a0,
        "a1": a1,
        "a2": a2,
        "S": S,
        "delta": round(delta, 10),
        "R2": R2,
        "name": NAME,
        "model": polinomModel,
    }
