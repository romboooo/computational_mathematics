import numpy as np

from helpers.interpretationR import interpretR

def exponentialApprox(x, y):
    print("")
    print("--- Экспоненциальная ---")
    if any(val <= 0 for val in y):
        raise ValueError("Все значения y должны быть положительными.")
    
    n = len(x)
    x_arr = np.array(x)
    y_arr = np.array(y)
    
    ln_y = np.log(y_arr)
    
    sum_x = np.sum(x_arr)
    sum_ln_y = np.sum(ln_y)
    sum_x_squared = np.sum(x_arr ** 2)
    sum_x_ln_y = np.sum(x_arr * ln_y)
    
    A = np.array([
        [sum_x_squared, sum_x],
        [sum_x, n]
    ])
    B = np.array([sum_x_ln_y, sum_ln_y])
    
    try:
        a0, a1 = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        print("Система уравнений вырождена")
        return {}
    
    def polinomModel(x):
        return np.exp(a0) * np.exp(a1 * x)  # Исправлено: используем exp(a0)
    
    fi = polinomModel(np.array(x))
    ei = y - fi
    S = (ei ** 2).sum()
    delta = np.sqrt(S / n)
    
    y_mean = np.mean(y)
    ss_total = ((y - y_mean) ** 2).sum()
    R2 = 1 - (S / ss_total)
    
    print(f"Формула: y = {np.exp(a0):.6f} * e^{a1:.6f}x")
    print(f"Мера отклонения: S = {S:.6f}")
    print(f"Среднеквадратичное отклонение: δ = {delta:.6f}")
    print(f"Достоверность аппроксимации: R² = {R2:.6f}")
    
    interpretR(R2)
    return {
        "a0": a0,
        "a1": a1,
        "S": S,
        "delta": delta,
        "R2": R2,
    }