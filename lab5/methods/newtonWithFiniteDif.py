def newtonWithFiniteDifferences(x,y,x_):
    print("Многочлен ньютона с конечными разностями:\n")
    print("Таблица конечных разностей: \n")
    finiteDifferences(x,y)





def finiteDifferences(x,y):
    n = len(x)
    table = [[x[i]] for i in range(n)]
    for i in range(n):
        table[i].append(y[i])
    
    for order in range(1, n):
        for i in range(n - order):
            diff = table[i+1][order] - table[i][order]
            table[i].append(diff)
    
    headers = ["x_i", "y_i"] + [f"Δ^{k}y_i" for k in range(1, n)]
    
    print("\t".join(headers))
    print("-" * 60)
    
    for i in range(n):
        row = []
        for j in range(len(headers)):
            if j < len(table[i]):
                if isinstance(table[i][j], float):
                    row.append(f"{table[i][j]:.4f}")
                else:
                    row.append(str(table[i][j]))
            else:
                row.append("") 
        
        print("\t".join(row))