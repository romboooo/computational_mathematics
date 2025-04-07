import math

def func(x):
    return 2.74 * x ** 3 - 1.93 * x ** 2 - 15.28 * x - 3.72
def diffFunc(x):
    return (411*x**2 - 193*x)/764
def doubleDiffFunc(x):
    return (822*x - 193)/764
def x0count(a,b):
    return (a*func(b) - b*func(a))/(func(b) - func(a))

def isRootExists(a,b) -> bool:
    return func(a) * func(b) < 0

def method(a,b):
    x = x0count(a,b)
    print(x)
    print(func(x))
    i = 1
    xn1 = a+b/2 

    while(abs(func(x)) > epsilon or abs(a - b) < epsilon or abs(x - xn1) < 0 ):
        print(f"итерация номер {i}")

        print("|--a--|--b--|--x--|--f(a)--|--f(b)--|--f(x)--|--|Xi+1 - Xi|--|")
        print(f"{a:.4f},{b:.4f},{x:.4f},{func(a):.4f}, {func(b):.4f}, {func(x):.4f}, {abs(x - xn1):.4f}")
        x = x0count(a,b)

        if(func(a) * func(x) < 0):
            b = x
        if(func(x) * func(b) < 0):
            a = x
        i+=1

        if i == 100: 
            print("превышен лимит итераций")
            break

print("введите интервал изоляции корня. Два числа через пробел a0 b0 ")
a, b = map(int, input().split())
epsilon = float(input("введите точность \n"))

if(isRootExists(a,b)):
    print("корень на этом отрезке существует")
else: 
    print("корня на этом отрезке не существует")


method(a,b)



