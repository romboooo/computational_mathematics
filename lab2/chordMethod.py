import math

def func(x,choice):
    if choice == 1:
        return 2.74 * x ** 3 - 1.93 * x ** 2 - 15.28 * x - 3.72
    if choice == 2:
        return x**3 - x + 4
    if choice == 3:
        return math.sin(x) - math.exp(-x)
def diffFunc(x,choice):
    if choice == 1:
        return 8.22 * x**2 - 3.86 * x - 15.28  
    if choice == 2:
        return 3*x**2 - 1
    if choice == 3:
        return math.cos(x) + math.exp(-x)
def doubleDiffFunc(x,choice):
    if choice == 1:
        return 16.44 * x - 3.86 
    if choice == 2:
        return 6*x
    if choice == 3:
        return -math.sin(x) - math.exp(-x)
    

def x0count(a,b,choice):
    return (a*func(b,choice) - b*func(a,choice))/(func(b,choice) - func(a,choice))

def isRootExists(a,b,choice) -> bool:
    return func(a,choice) * func(b,choice) < 0

def method(a,b,choice):
    x = x0count(a,b,choice)
    print(x)
    print(func(x,choice))
    i = 1
    xn1 = a+b/2 

    while(abs(func(x,choice)) > epsilon or abs(a - b) < epsilon or abs(x - xn1) < 0 ):
        print(f"итерация номер {i}")

        print("|--a--|--b--|--x--|--f(a)--|--f(b)--|--f(x)--|--|Xi+1 - Xi|--|")
        print(f"{a:.4f},{b:.4f},{x:.4f},{func(a,choice):.4f}, {func(b,choice):.4f}, {func(x,choice):.4f}, {abs(x - xn1):.4f}")
        x = x0count(a,b,choice)

        if(func(a,choice) * func(x,choice) < 0):
            b = x
        if(func(x,choice) * func(b,choice) < 0):
            a = x
        i+=1

        if i == 100: 
            print("превышен лимит итераций")
            break
def choice():
    print(f"выберите уравнениe:")
    print("1:")
    print("2.74x^3 - 1.93x^2 - 15.28x - 3.72 = 0")
    print("2:")
    print("x^3 - x + 4 = 0")
    print("3:")
    print("sin(x) - exp^-x = 0")
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
print("введите интервал изоляции корня. Два числа через пробел a0 b0 ")
a, b = map(int, input().split())
epsilon = float(input("введите точность \n"))

if(isRootExists(a,b,choice)):
    print("корень на этом отрезке существует")
else: 
    print("корня на этом отрезке не существует")


method(a,b,choice)



