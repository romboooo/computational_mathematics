import numpy as np

def powerApprox(x: list[float], y: list[float]) -> dict[str, float]:
    print("")
    print("--- Степенная ---")

    n = len(x)

    if any(val <= 0 for val in x) or any(val <= 0 for val in y):
        raise ValueError("Все значения x и y должны быть положительными.")

    ln_x = np.log(x)
    ln_y = np.log(y)

    sum_ln_x = ln_x.sum()
    sum_ln_y = ln_y.sum()
    sum_ln_x2 = (ln_x ** 2).sum()
    sum_ln_x_ln_y = (ln_x * ln_y).sum()

    A = np.array([
        [sum_ln_x2, sum_ln_x],
        [sum_ln_x, n]
    ])
    B = np.array([sum_ln_x_ln_y, sum_ln_y])

    try:
        solution = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        print("Система уравнений вырождена")
        return None

    b, ln_a = solution
    a = np.exp(ln_a)

    def polinomModel(x_val):
        return a * x_val ** b

    fi = polinomModel(np.array(x))
    ei = y - fi
    S = (ei ** 2).sum()
    delta = np.sqrt(S / n)

    y_mean = np.mean(y)
    ss_total = ((y - y_mean) ** 2).sum()
    R2 = 1 - (S / ss_total)

    print(f"Формула: y = {a:.6f} * x^{b:.6f}")
    print(f"Мера отклонения: S = {S:.6f}")
    print(f"Среднеквадратичное отклонение: δ = {delta:.6f}")
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
        "a": a,
        "b": b,
        "S": S,
        "delta": delta,
        "R2": R2,
    }