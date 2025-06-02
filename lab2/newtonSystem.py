import math
import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


def func1(x, y, choice):
    if choice == 1:
        return np.sin(x + 1) - y - 1.2
    elif choice == 2:
        return np.sin(x - 1) + y - 1.5  
    elif choice == 3:
        return 2*x - np.sin(y-0.5) -1

def func2(x, y, choice):
    if choice == 1:
        return 2 * x + np.cos(y) - 2
    elif choice == 2:
        return x - np.sin(y + 1) - 1    
    elif choice == 3:
        return y + np.cos(x) - 1.5
 

def diffFunc1ForX(x, y, choice):
    if choice == 1:
        return np.cos(x + 1)
    elif choice == 2:
        return np.cos(x - 1)  
    elif choice == 3:
        return 2
        

def diffFunc1ForY(x, y, choice):
    if choice == 1:
        return -1
    elif choice == 2:
        return 1  # df1/dy
    elif choice == 3:
        return - np.cos(y - 0.5) 

def diffFunc2ForX(x, y, choice):
    if choice == 1:
        return 2
    elif choice == 2:
        return 1  # df2/dx
    elif choice == 3:
        return -np.sin(x)

def diffFunc2ForY(x, y, choice):
    if choice == 1:
        return -np.sin(y)
    elif choice == 2:
        return -np.cos(y + 1)  # df2/dy 
    elif choice == 3:
        return 1
    

def newton_system(x0, y0, epsilon,choice):
    x, y = x0, y0
    i = 1
    while True:
        J = np.array([
            [diffFunc1ForX(x, y,choice), diffFunc1ForY(x, y,choice)],  # Строка для f1
            [diffFunc2ForX(x, y,choice), diffFunc2ForY(x, y,choice)]   # Строка для f2
        ])
        
        f1 = func1(x, y,choice)
        f2 = func2(x, y,choice)
        F = np.array([f1, f2])
        
        print(f"\nИтерация {i}:")
        print(f"x = {x:.6f}, y = {y:.6f}")
        print(f"F = [{f1:.6f}, {f2:.6f}]")
        
        if np.linalg.norm(F) < epsilon:
            print(f"Условие сходимости достигнуто (||F|| = {np.linalg.norm(F):.6f} < {epsilon})")
            break
        
        try:
            delta = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError:
            print("Ошибка: матрица Якоби вырождена!")
            break
        
        x_prev, y_prev = x, y
        
        x += delta[0]
        y += delta[1]
        
        print(f"Δx = {delta[0]:.6f}, Δy = {delta[1]:.6f}")
        print(f"Новые значения: x = {x:.6f}, y = {y:.6f}")
        
        if abs(x - x_prev) < epsilon and abs(y - y_prev) < epsilon:
            print("Изменения меньше epsilon")
            break
        
        if i >= 15:
            print("Достигнут лимит итераций")
            break
        
        i += 1
    
    return x, y

def choice():
    print(f"выберите систему уравнений:")
    print("1:")
    print("{sin(x+1)-y = 1.2")
    print("{2x + cosy = 2")
    print("2:")
    print("{sin(x-1) + y = 1.5")
    print("{x - sin(y + 1) = 1")
    print("3:")
    print("{2x - sin(y-0.5)=1")
    print("{y + cosx = 1.5")
    choice = int(input())
    if(choice == 1):
        return choice
    elif(choice == 2):
        return choice
    elif(choice == 3):
        return choice
    else:
        print("такого варианта нет")
        choice()

choice = choice()

print("Введите начальное приближение (два числа через пробел):")

a, b = map(float, input().split()) 
epsilon = float(input("Введите точность: "))

solution_x, solution_y = newton_system(a, b, epsilon,choice)

print("\nРезультат:")
print(f"x ≈ {solution_x:.6f}")
print(f"y ≈ {solution_y:.6f}")
