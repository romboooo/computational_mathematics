import numpy as np


def func(x):
    return 12 * x / (x**4 + 1)


def readData():
    with open("input.txt", "r") as file:
        x = np.array(list(map(float, file.readline().split())))
        y = np.array(list(map(float, file.readline().split())))
    return x, y


def squareApprox(x, y) -> dict[str,float]:
    print("")
    print("--- Квадратичная ---")
    n = len(x)
    sumX = sum(x)
    sumY = sum(y)
    sumX2 = sum(X**2 for X in x)
    sumXY = sum(X * Y for X, Y in zip(x, y))
    sumX3 = sum(X**3 for X in x)
    sumX2Y = sum(X**2 * Y for X, Y in zip(x, y))
    sumX4 = sum(X**4 for X in x)
    A = np.array([[n, sumX, sumX2], [sumX, sumX2, sumX3], [sumX2, sumX3, sumX4]])
    B = np.array([sumY, sumXY, sumX2Y])

    try:
        solution = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        print("Система уравнений вырождена, решение не существует")
        return None
    if solution is not None:
        a0, a1, a2 = solution
    else:
        print("ошибка в вычислении матрицы")

    def polinomModel(a0, a1, a2, x):
        return a0 + a1 * x + a2 * x**2

    fi = []
    ei = []
    S = 0
    fiAverage = 0
    for i in range(n):
        fi.append(polinomModel(a0, a1, a2, x[i]))
        ei.append(fi[i] - y[i])
        S += ei[i] ** 2
        fiAverage += fi[i]

    delta = np.sqrt(S / n)
    fiAverage = 1 / n * sum(fi)
    ss_total = sum((yi - fiAverage)**2 for yi in y)
    R2 = 1 - (S / ss_total)


    print(f"Формула: y = {a0:.6f}x² + {a1:.6f}x + {a2:.6f}")
    print(f"Мера отклонения: S = {S:.6f}")
    print(f"Среднеквадратичное отклонение: 𝜹 = {delta:.6f}")
    print(f"Достоверность аппроксимации: R² = {R2:.6f}")
    if R2 >= 0.95:
        print("R2 >= 0.95 -> Высокая точность аппроксимации, модель хорошо описывает явление")
    elif 0.75 <= R2 < 0.95:
        print("0.75 <= R2 < 0.95 -> Удовлетворительная аппроксимация, модель в целом адекватно описывает явление")
    elif 0.5 <= R2 < 0.75:
        print("0.5 <= R2 < 0.75 -> Слабая аппроксимация, модель слабо описывает явление")
    elif 0.5 > R2:
        print("0.5 > R2 -> Точность аппроксимации недостаточна и модель требует изменения")

    return {
        "a0": a0,
        "a1": a1,
        "a2": a2,
        "S": S,
        "delta": delta,
        "R2": R2
    }

def exponentialApprox(x,y):
    print("")
    print("--- Экспоненциальная ---")
    n = len(x)
    sumX = sum(x)
    sumY = sum(y)
    

def linealApprox(x,y) -> dict[str,float]:
    print("")
    print("--- Линейная ---")
    n = len(x)
    sumX = sum(x)
    sumY = sum(y)
    sumX2 = sum(X**2 for X in x)
    sumXY = sum(X * Y for X, Y in zip(x, y))
    A = np.array([[sumX2, sumX], [sumX, n]])
    B = np.array([sumXY, sumY])
    try:
        solution = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        print("Система уравнений вырождена, решение не существует")
        return None
    if solution is not None:
        a0, a1 = solution
    else:
        print("ошибка в вычислении матрицы")

    def polinomModel(a0, a1, x):
        return a0*x + a1
    
    fi = []
    ei = []
    S = 0
    fiAverage = 0
    for i in range(n):
        fi.append(polinomModel(a0, a1, x[i]))
        ei.append(fi[i] - y[i])
        S += ei[i] ** 2
        fiAverage += fi[i]
    delta = np.sqrt(S / n)
    fiAverage = 1 / n * sum(fi)
    ss_total = sum((yi - fiAverage)**2 for yi in y)
    R2 = 1 - (S / ss_total)
    x_mean = sumX / n
    y_mean = sumY / n
    numerator = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))
    denominator = np.sqrt(sum((xi - x_mean)**2 for xi in x) * sum((yi - y_mean)**2 for yi in y))
    r = numerator / denominator

    print(f"Формула: y = {a0:.6f}x + {a1:.6f}")
    print(f"Мера отклонения: S = {S:.6f}")
    print(f"Среднеквадратичное отклонение: 𝜹 = {delta:.6f}")
    print(f"Достоверность аппроксимации: R² = {R2:.6f}")
    print(f"Коэффицент корреляции: r = {r:.6f}")

    if R2 >= 0.95:
        print("R2 >= 0.95 -> Высокая точность аппроксимации, модель хорошо описывает явление")
    elif 0.75 <= R2 < 0.95:
        print("0.75 <= R2 < 0.95 -> Удовлетворительная аппроксимация, модель в целом адекватно описывает явление")
    elif 0.5 <= R2 < 0.75:
        print("0.5 <= R2 < 0.75 -> Слабая аппроксимация, модель слабо описывает явление")
    elif 0.5 > R2:
        print("0.5 > R2 -> Точность аппроксимации недостаточна и модель требует изменения")

    if r == 0:
        print("r = 0 -> Cвязь между переменными отсутствует")
    elif abs(r) < 0.3:
        print("|r| < 0.3 -> Cвязь между переменными слабая")
    elif 0.5 > abs(r) >= 0.3:
        print("0.5 > |r| >= 0.3 -> Cвязь между переменными умеренная")
    elif 0.7 > abs(r) >= 0.5:
        print("0.7 > |r| >= 0.5 -> Cвязь между переменными заметная")
    elif 0.9 > abs(r) >= 0.7:
        print("0.9 > |r| >= 0.5 -> Cвязь между переменными высокая")
    elif 1 > abs(r) >= 0.9:
        print("1 > |r| >= 0.9 -> Cвязь между переменными весьма высокая")
    elif abs(r) == 1:
        print("r = +-1 -> Cтрогая линейная функциональная зависимость в зависимости от знака коэффициента a")
    return {
        "a0": a0,
        "a1": a1,
        "S": S,
        "delta": delta,
        "R2": R2,
        "r": r
    }

def cubeApprox(x,y) -> dict[str,float]:
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

    def polinomModel(a0, a1, a2, a3, x):
        return a0 + a1 * x + a2 * x**2 + a3*x**3
    
    fi = []
    ei = []
    S = 0
    fiAverage = 0
    for i in range(n):
        fi.append(polinomModel(a0, a1,a2,a3, x[i]))
        ei.append(fi[i] - y[i])
        S += ei[i] ** 2
        fiAverage += fi[i]
    delta = np.sqrt(S / n)
    fiAverage = 1 / n * sum(fi)
    ss_total = sum((yi - fiAverage)**2 for yi in y)
    R2 = 1 - (S / ss_total)

    print(f"Формула: y = {a0:.6f}x³ + {a1:.6f}x² + {a2:.6f}x + {a3:.6f}")
    print(f"Мера отклонения: S = {S:.6f}")
    print(f"Среднеквадратичное отклонение: 𝜹 = {delta:.6f}")
    print(f"Достоверность аппроксимации: R² = {R2:.6f}")

    if R2 >= 0.95:
        print("R2 >= 0.95 -> Высокая точность аппроксимации, модель хорошо описывает явление")
    elif 0.75 <= R2 < 0.95:
        print("0.75 <= R2 < 0.95 -> Удовлетворительная аппроксимация, модель в целом адекватно описывает явление")
    elif 0.5 <= R2 < 0.75:
        print("0.5 <= R2 < 0.75 -> Слабая аппроксимация, модель слабо описывает явление")
    elif 0.5 > R2:
        print("0.5 > R2 -> Точность аппроксимации недостаточна и модель требует изменения")

    return {
        "a0": a0,
        "a1": a1,
        "a2": a2,
        "S": S,
        "delta": delta,
        "R2": R2,
    }

def powerApprox(x,y) -> dict[str,float]:
    print("")
    print("--- Степенная ---")

    if any(val <= 0 for val in x) or any(val <= 0 for val in y):
        raise ValueError("Все значения x и y должны быть положительными для степенной аппроксимации.")

    ln_x = [np.log(X) for X in x]
    ln_y = [np.log(Y) for Y in y]
    n = len(x)
    sum_ln_x = sum(ln_x)
    sum_ln_y = sum(ln_y)
    sum_ln_x2 = sum(lx ** 2 for lx in ln_x)
    sum_ln_x_ln_y = sum(lx * ly for lx, ly in zip(ln_x, ln_y))


    A = np.array([
        [sum_ln_x2, sum_ln_x],
        [sum_ln_x, n]
    ])
    B = np.array([sum_ln_x_ln_y, sum_ln_y])

    try:
        solution = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        print("Система уравнений вырождена, решение не существует")
        return None

    b, ln_a = solution
    a = np.exp(ln_a)


    def polinomModel(x):
        return a + x ** b
    
    fi = [polinomModel(xi) for xi in x]
    ei = [yi - fi_i for yi, fi_i in zip(y, fi)]
    S = sum(e ** 2 for e in ei)
    delta = np.sqrt(S / n)

    y_mean = sum(y) / n
    ss_total = sum((yi - y_mean) ** 2 for yi in y)
    R2 = 1 - (S / ss_total)

    print(f"Формула: y = {a:.6f} * x^{b:.6f}")
    print(f"Мера отклонения: S = {S:.6f}")
    print(f"Среднеквадратичное отклонение: 𝜹 = {delta:.6f}")
    print(f"Достоверность аппроксимации: R² = {R2:.6f}")

    if R2 >= 0.95:
        print("R2 >= 0.95 -> Высокая точность аппроксимации, модель хорошо описывает явление")
    elif 0.75 <= R2 < 0.95:
        print("0.75 <= R2 < 0.95 -> Удовлетворительная аппроксимация, модель в целом адекватно описывает явление")
    elif 0.5 <= R2 < 0.75:
        print("0.5 <= R2 < 0.75 -> Слабая аппроксимация, модель слабо описывает явление")
    elif 0.5 > R2:
        print("0.5 > R2 -> Точность аппроксимации недостаточна и модель требует изменения")

    return {
        "a0": a,
        "a1": b,
        "S": S,
        "delta": delta,
        "R2": R2,
    }


def main():
    x,y = readData()
    if len(x) != len(y):
        print("ошибка ввода точек")
        return
    print("--- Вычисления ---")
    squareData = squareApprox(x, y)
    linearData = linealApprox(x,y)
    cubeData = cubeApprox(x,y)
    powerData = powerApprox(x,y)

if __name__ == "__main__":
    main()
