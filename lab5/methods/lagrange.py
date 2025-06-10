def lagrange(x,y,x_):
    length = len(x)
    result = 0
    for i in range(length):
        term = y[i]  
        for j in range(length):
            if i != j:
                if x[i] == x[j]:
                    raise ValueError("Узлы интерполяции должны быть различными")
                term *= (x_ - x[j]) / (x[i] - x[j])
        
        result += term  
    
    return result