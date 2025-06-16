def build_difference_table(x, y):
    n = len(x)
    diff_table = [[0] * n for _ in range(n)]
    for i in range(n):
        diff_table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i+1][j-1] - diff_table[i][j-1]
    return diff_table

def print_difference_table(x, diff_table):
    n = len(x)
    print("x".ljust(10), end="")
    for i in range(n):
        print(f"Δ^{i}y".ljust(15), end="")
    print()
    for i in range(n):
        print(f"{x[i]:<10.4f}", end="")
        for j in range(n - i):
            print(f"{diff_table[i][j]:<15.6f}", end="")
        print()

def calculate_newton(x, y, x_):
    n = len(x)
    h = x[1] - x[0]
    t = (x_ - x[0]) / h
    diff_table = build_difference_table(x, y)
    
    result = diff_table[0][0]
    term = t
    factorial = 1
    computation_str = f"{diff_table[0][0]:.6f}"
    
    for i in range(1, n):
        delta = diff_table[0][i]
        component = term * delta / factorial
        result += component
        
        bracket_expr = f"[{t:.4f}"
        for j in range(1, i):
            bracket_expr += f"*({t:.4f}-{j})"
        bracket_expr += "]"
        
        operator = "*" if i == 1 else " + "
        
        if i == 1:
            computation_str += f" + {t:.4f} * {delta:.6f} / {factorial}"
        else:
            computation_str += f" + {bracket_expr} * {delta:.6f} / {factorial}"
        
        term *= (t - i)
        factorial *= (i + 1)
    
    return result, computation_str

def newtonWithFiniteDifferences(x, y, x_):
    print("\nМногочлен Ньютона с конечными разностями\n")
    
    if len(x) != len(y):
        raise ValueError("Ошибка: массивы x и y должны иметь одинаковую длину")
    h = x[1] - x[0]
    for i in range(1, len(x)-1):
        if abs((x[i+1] - x[i]) - h) > 1e-6:
            raise ValueError("Ошибка: сетка должна быть равномерной")
    
    diff_table = build_difference_table(x, y)
    print("Таблица конечных разностей:")
    print_difference_table(x, diff_table)
    
    print("\nФормула многочлена Ньютона:")
    print("N(x) = y0 + t*Δy0 + [t(t-1)/2!]*Δ²y0 + [t(t-1)(t-2)/3!]*Δ³y0 + ...")
    
    n = len(x)
    h = x[1] - x[0]
    t = (x_ - x[0]) / h
    print(f"\nВычисление для точки x = {x_}")
    print(f"t = (x - x0)/h = ({x_} - {x[0]})/{h} = {t:.4f}\n")
    
    result, computation_str = calculate_newton(x, y, x_)
    
    symbolic_formula = "N(x_) = y0"
    for i in range(1, n):
        if i == 1:
            symbolic_formula += " + [t] * Δ^1y0 / 1!"
        else:
            deltas = "*".join([f"(t-{j})" for j in range(i-1)])
            symbolic_formula += f" + [t{deltas}] * Δ^{i}y0 / {i}!"
    
    print(f"{symbolic_formula} = ")
    print(computation_str + f" = {result:.6f}")
    
    print(f"\nФинальный результат: N({x_}) = {result:.6f}\n")
    return result