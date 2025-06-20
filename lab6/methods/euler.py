def euler_method(f, x0, y0, xn, n, epsilon, exact_y):
    print("Метод Эйлера \n")
    h = (xn - x0) / n  
    x_arr = [x0]  
    y_arr = [y0] 
    
    x0_init = x0
    y0_init = y0

    for i in range(n):
        xi = x_arr[-1]
        yi = y_arr[-1]
        
        next_y = yi + h * f(xi, yi)
        next_x = xi + h
        
        x_arr.append(next_x)
        y_arr.append(next_y)

    print("\nРезультат метода Эйлера:")
    print("x\t\tПриближенное y\t\tТочное y\t\tПогрешность")
    print("------------------------------------------------------------------------------------")
    for i in range(len(x_arr)):
        exact = exact_y(x_arr[i], x0_init, y0_init)
        error = abs(y_arr[i] - exact)
        print(f"{x_arr[i]:.6f}\t{y_arr[i]:.12f}\t\t{exact:.12f}\t\t{error:.2e}")
    
    final_error = abs(y_arr[-1] - exact_y(xn, x0_init, y0_init))
    if final_error < epsilon:
        print(f"\nТочность достигнута: |y_прибл - y_точн| = {final_error:.2e} < ε = {epsilon}")
    else:
        print(f"\nТочность НЕ достигнута: |y_прибл - y_точн| = {final_error:.2e} >= ε = {epsilon}")

    return x_arr, y_arr