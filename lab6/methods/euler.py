def euler_method(f, x0, y0, xn, n, epsilon):
    print("Метод эйлера: ")
    h = (xn - x0) / n
    x_arr = [x0]
    y_arr = [y0]
    
    for i in range(n):
        xi = x_arr[-1]
        yi = y_arr[-1]
        next_y = yi + h * f(xi, yi)
        next_x = xi + h
        x_arr.append(next_x)
        y_arr.append(next_y)
    
    n2 = 2 * n
    h2 = (xn - x0) / n2
    x_arr2 = [x0]
    y_arr2 = [y0]
    
    for i in range(n2):
        xi = x_arr2[-1]
        yi = y_arr2[-1]
        next_y = yi + h2 * f(xi, yi)
        next_x = xi + h2
        x_arr2.append(next_x)
        y_arr2.append(next_y)
    
    R = abs(y_arr[-1] - y_arr2[-1]) / (2**1 - 1)
    
    print("\nРезультат метода Эйлера:")
    print("x\t\tПриближенное y")
    print("-------------------------------")
    
    for i in range(len(x_arr)):
        print(f"{x_arr[i]:.6f}\t{y_arr[i]:.12f}")
    
    print(f"\nОценка погрешности по правилу Рунге: R = {R:.12f}")
    
    if R < epsilon:
        print(f"Точность достигнута: R = {R:.2e} < ε = {epsilon}")
    else:
        print(f"Точность НЕ достигнута: R = {R:.2e} >= ε = {epsilon}")
    
    return x_arr, y_arr, R


def runge_rule(method, f, x0, y0, xn, n, p, epsilon):
    _, y_h, _ = method(f, x0, y0, xn, n, 0)
    yh_final = y_h[-1]
    
    _, y_h2, _ = method(f, x0, y0, xn, 2*n, 0)
    yh2_final = y_h2[-1]
    
    R = abs(yh_final - yh2_final) / (2**p - 1)
    
    is_accurate = R < epsilon
    
    print(f"Оценка погрешности по правилу Рунге: R = {R:.12f}")
    if is_accurate:
        print(f"Точность достигнута: R = {R:.2e} < ε = {epsilon}")
    else:
        print(f"Точность НЕ достигнута: R = {R:.2e} >= ε = {epsilon}")
    
    return R, is_accurate