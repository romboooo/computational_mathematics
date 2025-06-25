import matplotlib.pyplot as plt
import numpy as np


def lagrange(x, y, x_, plot=True):
    print("Многочлен Лагранжа:\n")
    n = len(x)
    result = 0.0
    terms = []

    for i in range(n):
        term = y[i]
        num_parts = []
        den_parts = []

        for j in range(n):
            if i != j:
                num_val = x_ - x[j]
                den_val = x[i] - x[j]
                term *= num_val / den_val
                num_parts.append(f"({x_:.2f}-{x[j]:.2f})")
                den_parts.append(f"({x[i]:.2f}-{x[j]:.2f})")

        num_str = "*".join(num_parts)
        den_str = "*".join(den_parts)

        result += term
        terms.append(term)

        print(f"Слагаемое l_{i}(x) = [{y[i]}] * [{num_str}] / [{den_str}]")
        print(f"          = {term:.6f}")

    print("\nL(x) = " + " + ".join([f"{t:.6f}" for t in terms]) + f" = {result:.6f}\n")

    # draw_graph(plot,n,x,x_,result,y)
    return result


def draw_graph(plot, n, x, x_, result, y):
    if plot:

        def lagrange_func(x_point):
            total = 0.0
            for i in range(n):
                term = y[i]
                for j in range(n):
                    if i != j:
                        term *= (x_point - x[j]) / (x[i] - x[j])
                total += term
            return total

        x_min, x_max = min(x), max(x)
        padding = 0.1 * (x_max - x_min)
        x_range = np.linspace(x_min - padding, x_max + padding, 500)
        y_range = [lagrange_func(xi) for xi in x_range]

        plt.figure(figsize=(10, 6))

        plt.plot(
            x_range,
            y_range,
            "b-",
            linewidth=2,
            label="Интерполяционный многочлен Лагранжа",
        )

        plt.scatter(x, y, color="red", s=80, zorder=5, label="Исходные данные")

        plt.scatter(
            [x_],
            [result],
            color="green",
            s=100,
            zorder=5,
            label=f"Точка интерполяции (x={x_}, y={result:.4f})",
        )

        plt.title("Интерполяция методом Лагранжа", fontsize=14)
        plt.xlabel("x", fontsize=12)
        plt.ylabel("y", fontsize=12)
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.legend(loc="best", fontsize=10)
        plt.tight_layout()

        plt.figtext(0.5, 0.01, f"Полином {n-1}-го порядка", ha="center", fontsize=10)

        plt.savefig("lagrange_interpolation.png", dpi=300)
        # plt.show()
