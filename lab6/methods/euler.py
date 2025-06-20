def euler_method(f, x0, y0, xn, n, epsilon):
    print("Метод Эйлера\n")
    x0_init = x0
    y0_init = y0
    max_iterations = 10  
    p = 1 
    original_n = n
    iteration_count = 0
    R = float('inf') 
    
    while R >= epsilon and iteration_count < max_iterations:
        h = (xn - x0) / n 
        x_arr = [x0]  
        y_arr = [y0]  

        for _ in range(n):
            xi = x_arr[-1]
            yi = y_arr[-1]
            next_y = yi + h * f(xi, yi)
            next_x = xi + h
            y_arr.append(next_y)
            x_arr.append(next_x)
        
        n2 = 2 * n
        h2 = (xn - x0) / n2
        x_arr2 = [x0]  
        y_arr2 = [y0]  

        for _ in range(n2):
            xi = x_arr2[-1]
            yi = y_arr2[-1]
            next_y = yi + h2 * f(xi, yi)
            next_x = xi + h2
            y_arr2.append(next_y)
            x_arr2.append(next_x)

        yh = y_arr[-1]
        yh2 = y_arr2[-1]
        R = abs(yh - yh2) / (2**p - 1)
        
        if R >= epsilon:
            print(f"Точность не достигнута при n={n}: R = {R:.2e} >= ε = {epsilon}")
            print(f"Удваиваем число шагов: n = {n} -> {2*n}")
            n *= 2
            iteration_count += 1
    
    print("\n" + "="*80)
    print("ФИНАЛЬНЫЕ РЕЗУЛЬТАТЫ")
    print(f"Финальное число шагов: n = {n}")
    print(f"Количество удвоений шага: {iteration_count}")
    
    if R < epsilon:
        print(f"Точность достигнута: R = {R:.2e} < ε = {epsilon}")
    else:
        print(f"Достигнут предел удвоений: R = {R:.2e} >= ε = {epsilon}")
    
    print("\nРезультат:")
    if len(x_arr) >= 100:
        print("Таблица получилось слишком большой")
        print(f"{x_arr[-1]:.6f}\t{y_arr[-1]:.12f}\t")

    else:
        print("\nРезультаты не выводятся в табличном виде (слишком много точек)")
        print(f"Количество точек: {len(x_arr)} > 100")
        
        print("\nКлючевые точки:")
        print("x\t\tПриближенное y\t\tТочное y\t")
        print("------------------------------------------------------------------------------------")
        
        print(f"{x_arr[0]:.6f}\t{y_arr[0]:.12f}\t")
        
        mid_index = len(x_arr) // 2
        print(f"{x_arr[mid_index]:.6f}\t{y_arr[mid_index]:.12f}\t")
        
        print(f"{x_arr[-1]:.6f}\t{y_arr[-1]:.12f}\t")
        print("... (пропущены промежуточные точки)")
    
    return x_arr, y_arr