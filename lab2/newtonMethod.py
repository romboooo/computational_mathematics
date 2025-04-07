def func(x):
    return 2.74 * x ** 3 - 1.93 * x ** 2 - 15.28 * x - 3.72
def diffFunc(x):
    return 8.22 * x**2 - 3.86 * x - 15.28  
def doubleDiffFunc(x):
    return 16.44 * x - 3.86 

def is_sign_consistent(func, a, b, num_points=1000):
    if a > b:
        a, b = b, a
    if a == b:
        val = func(a)
        return val != 0
    
    step = (b - a) / (num_points - 1)
    prev_val = func(a)
    if prev_val == 0:
        return False
    prev_sign = 1 if prev_val > 0 else -1
    
    for i in range(1, num_points):
        x = a + i * step
        current_val = func(x)
        if current_val == 0:
            return False
        current_sign = 1 if current_val > 0 else -1
        if current_sign != prev_sign:
            return False
        prev_sign = current_sign
    return True

def convergenceCondition(a, b):
    if not is_sign_consistent(diffFunc, a, b):
        return False
    if not is_sign_consistent(doubleDiffFunc, a, b):
        return False
    return True

def xiCount(x):
    return x - (func(x)/diffFunc(x))

def x0Count(a,b): 
    if(func(a)*doubleDiffFunc(a) > 0):
        x0 = a
    elif(func(b)*doubleDiffFunc(b) > 0):
        x0 = b

    if(func(x0)* doubleDiffFunc(x0) > 0):
        print("𝑓(𝑥0)∙ 𝑓′′(𝑥0) > 0 выполняется => метод обеспечивает быструю сходимость")
    else:
        print("𝑓(𝑥0)∙ 𝑓′′(𝑥0) > 0 не выполняется => метод не обеспечивает быструю сходимость")

    return x0

def newtonMethod(a,b,epsilon):
    i = 1
    x0 = x0Count(a, b)  
    xi = x0
    while(True):
        print(f"итерация номер {i}")
        fxi = func(xi)
        fdiffxi = diffFunc(xi)
        xi1 = xiCount(xi)

        print("|--xi--|--f(xi)--|--f'(xi)--|--x(i+1)--|--|Xi+1 - Xi|--|")
        print(f"{xi:7f} {fxi:7f} {fdiffxi:7f} {xi1:7f} {abs(xi1 - xi):7f}")
        if(abs(xi1 - xi) < epsilon) or (abs(fxi) < epsilon):
            break
        i+=1
        xi = xi1
        if(i > 10):
            print("превышен лимит итераций")
            break


print("введите интервал изоляции корня. Два числа через пробел a0 b0 ")
a, b = map(int, input().split())
epsilon = float(input("введите точность \n"))

if convergenceCondition(a,b):
    print("условие сходимости выполняется, метод ньютона эффективен")
else:
    print("условие сходимости не выполняется, метод ньютона неэффективен")

newtonMethod(a,b,epsilon)
