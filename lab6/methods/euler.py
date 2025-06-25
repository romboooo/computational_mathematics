def euler_method(f, x0, y0, xn, n, epsilon):
    print("Метод Эйлера\n")
    max_iterations = 100
    p = 1
    iteration_count = 0
    R = float("inf")

    y_n_history = []

    while R >= epsilon and iteration_count < max_iterations:
        x_arr = [x0]
        y_arr = [y0]

        h = (xn - x0) / n
        for _ in range(n):
            xi = x_arr[-1]
            yi = y_arr[-1]
            next_y = yi + h * f(xi, yi)
            next_x = xi + h
            y_arr.append(next_y)
            x_arr.append(next_x)
        y_n_history.append(y_arr[-1])

        if len(y_n_history) >= 2:
            yh_n, yh2_n = y_arr[len(y_arr) - 2 :]
            R = abs(yh_n - yh2_n) / (2**p - 1)

            if R >= epsilon:
                print(f"Точность не достигнута при n={n}: R = {R:.2e} >= ε ({epsilon})")
                print(f"Удваиваем число шагов: n = {n} -> {2*n}")
            else:
                break
        else:
            print(f"Удваиваем число шагов: n = {n} -> {2*n}")
        n *= 2
        iteration_count += 1

    print("\n" + "=" * 80)
    print("ФИНАЛЬНЫЕ РЕЗУЛЬТАТЫ")
    print(f"Финальное число шагов: n = {n}")
    print(f"Количество удвоений шага: {iteration_count}")

    if R < epsilon:
        print(f"Точность достигнута: R = {R:.2e} < ε = {epsilon}")
    else:
        print(f"Достигнут предел удвоений: R = {R:.2e} >= ε = {epsilon}")

    print("\nРезультат:")
    if len(x_arr) >= 100:
        print("\nРезультаты не выводятся в табличном виде (слишком много точек)")
        print(f"Количество точек: {len(x_arr)} > 100")
        print("\nКлючевые точки:")
        print("x\t\tПриближенное y\t\tТочное y\t")
        print(
            "------------------------------------------------------------------------------------"
        )
        print(f"{x_arr[0]:.6f}\t{y_arr[0]:.12f}\t")

        mid_index = len(x_arr) // 2
        print(f"{x_arr[mid_index]:.6f}\t{y_arr[mid_index]:.12f}\t")

        print(f"{x_arr[-1]:.6f}\t{y_arr[-1]:.12f}\t")
        print("... (пропущены промежуточные точки)")

    else:
        print("x\t\tПриближенное y\t\tТочное y\t")
        print(
            "------------------------------------------------------------------------------------"
        )
        for i in range(len(x_arr)):
            print(f"{x_arr[i]:.6f}\t{y_arr[i]:.12f}\t")

    return x_arr, y_arr
