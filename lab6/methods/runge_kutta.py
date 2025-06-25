def runge_kutt(f, x0, y0, xn, n, epsilon):
    print("Метод Рунге-Кутты 4-го порядка с автоматическим выбором шага: \n")
    x0_init = x0
    y0_init = y0
    max_iterations = 10  
    p = 4 
    
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

            k1 = h * f(xi, yi)
            k2 = h * f(xi + h/2, yi + k1/2)
            k3 = h * f(xi + h/2, yi + k2/2)
            k4 = h * f(xi + h, yi + k3)

            next_y = yi + (k1 + 2*k2 + 2*k3 + k4) / 6
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

            k1 = h2 * f(xi, yi)
            k2 = h2 * f(xi + h2/2, yi + k1/2)
            k3 = h2 * f(xi + h2/2, yi + k2/2)
            k4 = h2 * f(xi + h2, yi + k3)

            next_y = yi + (k1 + 2*k2 + 2*k3 + k4) / 6
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
    print(f"Начальное число шагов: n0 = {original_n}")
    print(f"Финальное число шагов: n = {n}")
    print(f"Количество удвоений шага: {iteration_count}")
    
    if R < epsilon:
        print(f"Точность достигнута: R = {R:.2e} < ε = {epsilon}")
    else:
        print(f"Достигнут предел удвоений: R = {R:.2e} >= ε = {epsilon}")
    
    if len(x_arr) <= 100:
        print("\nРезультат:")
        print("x\t\tПриближенное y\t")
        print("------------------------------------------------------------------------------------")
        for i in range(len(x_arr)):
            print(f"{x_arr[i]:.6f}\t{y_arr[i]:.12f}\t")
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