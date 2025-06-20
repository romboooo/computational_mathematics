import matplotlib.pyplot as plt
import numpy as np

def divided_differences(x, y):
    n = len(x)
    table = [y.copy()]  
    
    for order in range(1, n):
        current_order = []
        prev_order = table[order-1]
        for j in range(n - order):
            num = prev_order[j+1] - prev_order[j]
            den = x[j+order] - x[j]
            value = num / den
            current_order.append(value)
        table.append(current_order)
    return table

def print_dd_table(x, y, table):
    n = len(x)
    header = " i |   x_i    |   y_i    |"
    for i in range(1, n):
        header += f"   f[{i}]    |"
    print(header)
    separator = "-" * len(header)
    print(separator)
    
    for i in range(n):
        row = f"{i:2d}  | {x[i]:8.4f}  | {y[i]:8.4f}  |"
        for k in range(1, n - i):
            if i < len(table[k]):
                row += f" {table[k][i]:8.4f}  |"
            else:
                row += " " * 9 + "|"
        print(row)

def newtonWithDividedDifferences(x, y, x_):
    table = divided_differences(x, y)
    n = len(x)
    
    print("Таблица разделённых разностей:")
    print_dd_table(x, y, table)
    print("\n")
    
    res = table[0][0]  
    mn = 1.0  
    
    print("Ньютон (разделённые разности):")
    print(f"f[x0] = {res:.7f}")
    
    for i in range(1, n):
        mn *= (x_ - x[i-1])
        dd = table[i][0]  
        term = dd * mn
        res += term
        print(f"f[x0..x{i}] = {dd:.7f}")
    
    print(f"\nP(x) = {res}")
    # draw_graph(True,table,n,x,x_,res,y)
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