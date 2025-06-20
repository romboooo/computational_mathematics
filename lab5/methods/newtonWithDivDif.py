import matplotlib.pyplot as plt
import numpy as np

def divided_differences(x, y):
    n = len(x)
    table = [y.copy()]
    print("Многочлен ньютона с разделёнными разностями:\n")
    
    first_order = []
    for j in range(n-1):
        num = table[0][j+1] - table[0][j]
        den = x[j+1] - x[j]
        value = num / den
        first_order.append(value)
        print(f"f(x_{j}, x_{j+1}) = (f(x_{j+1}) - f(x_{j}))/(x_{j+1} - x_{j}) = "
              f"({table[0][j+1]:.3f} - {table[0][j]:.3f})/({x[j+1]:.3f} - {x[j]:.3f}) = {value:.3f}")
    table.append(first_order)
    
    for i in range(2, n):
        current = []
        for j in range(n - i):
            num = table[i-1][j+1] - table[i-1][j]
            den = x[j+i] - x[j]
            value = num / den
            current.append(value)
            print(f"f(x_{j},...,x_{j+i}) = (f(x_{j+1},...,x_{j+i}) - f(x_{j},...,x_{j+i-1}))/(x_{j+i} - x_{j}) = "
                  f"({table[i-1][j+1]:.3f} - {table[i-1][j]:.3f})/({x[j+i]:.3f} - {x[j]:.3f}) = {value:.3f}")
        table.append(current)
    return table

def newtonWithDividedDifferences(x, y, x_):
    table = divided_differences(x, y)
    n = len(x)
    res = table[0][0]
    mn = 1
    terms = [f"{res:.3f}"]
    products = ["1"]
    values = [res]
    
    print("\nВычисление значения в точке x =", f"{x_:.3f}")
    for i in range(1, n):
        mn *= (x_ - x[i-1])
        term = table[i][0] * mn
        res += term
        
        prod_expr = "*".join([f"({x_:.3f} - {x[k]:.3f})" for k in range(i)])
        terms.append(f"{table[i][0]:.3f} * {prod_expr}")
        products.append(f"{mn:.3f}")
        values.append(term)
    
    print("Интерполяционный многочлен Ньютона:\n")
    print(f"N_{n-1}(x) = " + " + ".join(terms) + f" = {res:.5f}\n")
    
    print(f"Результат: y({x_:.3f}) ≈ {res:.5f}")


    draw_graph(True,table,n,x,x_,res,y)
    return res


def draw_graph(plot,table,n,x,x_,res,y):
    if plot:
        def newton_poly(x_val):
            result = table[0][0]
            product = 1.0
            for i in range(1, n):
                product *= (x_val - x[i-1])
                result += table[i][0] * product
            return result

        x_min, x_max = min(x), max(x)
        padding = 0.1 * (x_max - x_min)
        x_vals = np.linspace(x_min - padding, x_max + padding, 500)
        y_vals = [newton_poly(xi) for xi in x_vals]

        plt.figure(figsize=(10, 6))
        
        plt.plot(x_vals, y_vals, 'b-', linewidth=2, label='Интерполяционный многочлен Ньютона')
        
        plt.scatter(x, y, color='red', s=80, zorder=5, label='Исходные данные')
        
        plt.scatter([x_], [res], color='green', s=100, zorder=5, 
                   label=f'Точка интерполяции (x={x_}, y={res:.4f})')
        
        plt.title('Интерполяция методом Ньютона с разделенными разностями', fontsize=14)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('y', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend(loc='best', fontsize=10)
        
        plt.figtext(0.5, 0.01, f'Полином {n-1}-го порядка', ha='center', fontsize=10)
        
        plt.tight_layout()
        plt.savefig('newton_divided_diff_interpolation.png', dpi=300)
        # plt.show()