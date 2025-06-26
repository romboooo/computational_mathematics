def adams_method(f, x0, y0, xn, n, epsilon, exact_y):
    print("метод адамса:")

    h = (xn - x0) / n
    x_arr = [x0]
    y_arr = [y0]
    f_arr = []

    x0_init = x0
    y0_init = y0

    for i in range(min(3, n)):
        xi = x_arr[-1]
        yi = y_arr[-1]

        k1 = h * f(xi, yi)
        k2 = h * f(xi + h / 2, yi + k1 / 2)
        k3 = h * f(xi + h / 2, yi + k2 / 2)
        k4 = h * f(xi + h, yi + k3)

        next_y = yi + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        next_x = xi + h

        x_arr.append(next_x)
        y_arr.append(next_y)

    if n <= 3:
        print(
            "\nМетод Адамса требует минимум 4 точки. Использованы результаты Рунге-Кутты."
        )
        print_results(x_arr, y_arr, exact_y, x0_init, y0_init, epsilon)
        return x_arr, y_arr
    for i in range(4):
        f_arr.append(f(x_arr[i], y_arr[i]))

    for i in range(3, n):
        x_next = x_arr[i] + h

        y_pred = y_arr[i] + h/24 * (
            55 * f_arr[i]
            - 59 * f_arr[i-1]
            + 37 * f_arr[i-2]
            -  9 * f_arr[i-3]
        )

        y_old = y_pred
        f_pred = f(x_next, y_old)

        while True:
            y_new = y_arr[i] + h/24 * (
                9 * f_pred
            + 19 * f_arr[i]
            -  5 * f_arr[i-1]
            +      f_arr[i-2]
            )

            print("проверка условия:")

            print("|предиктор - корректор| < epsilon")
            print(f"|{y_new} - {y_old}|< {epsilon}:")
            if abs(y_new - y_old) < epsilon:
                print("True -> xi+1 = xi + h")
                break
            print("False -> предиктор становится корректором\n")
            y_old = y_new
            f_pred = f(x_next, y_old)
        x_arr.append(x_next)
        y_arr.append(y_new)
        f_arr.append(f(x_next, y_new))

    print("\nРезультат метода Адамса (предиктор-корректор):")
    print("x\t\tПриближенное y\t\tТочное y\t\tПогрешность")

    minerr = []
    for i in range(len(x_arr)):
        exact = exact_y(x_arr[i], x0_init, y0_init)
        error = abs(y_arr[i] - exact)
        minerr.append(error)
        print(f"{x_arr[i]:.6f}\t{y_arr[i]:.12f}\t{exact:.12f}\t{error:.2e}")

    maxn = max(minerr)

    print(f"Max error = {maxn}")

    if maxn < epsilon:
        print(f"\nТочность достигнута: |y_прибл - y_точн| = {maxn:.2e} < ε = {epsilon}")
    else:
        print(
            f"\nТочность НЕ достигнута: |y_прибл - y_точн| = {maxn:.2e} >= ε = {epsilon}"
        )

    return x_arr, y_arr


def print_results(x_arr, y_arr, exact_y, x0, y0, epsilon):
    print("x\t\tПриближенное y\t\tТочное y\t\tПогрешность")

    minerr = []
    for i in range(len(x_arr)):
        exact = exact_y(x_arr[i], x0, y0)
        error = abs(y_arr[i] - exact)
        minerr.append(error)
        print(f"{x_arr[i]:.6f}\t{y_arr[i]:.12f}\t{exact:.12f}\t{error:.2e}")

    final_error = abs(y_arr[-1] - exact_y(x_arr[-1], x0, y0))
    if max(minerr) < epsilon:
        print(
            f"\nТочность достигнута: |y_прибл - y_точн| = {max(minerr):.2e} < ε = {epsilon}"
        )
        print(max(minerr))

    else:
        print(
            f"\nТочность НЕ достигнута: |y_прибл - y_точн| = {max(minerr):.2e} >= ε = {epsilon}"
        )
        print(max(minerr))
