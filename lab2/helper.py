def func(x):
    return 2.74*x**3 - 1.93 * x ** 2 - 15.28 * x -3.72
def func2(xi, xi1):
    return xi - ((xi-xi1)/(func(xi) - func(xi1)))*func(xi)



print(func2(-1.879494,-1.866435))
print(func(func2(-1.879494,-1.866435)))
print(abs(-1.879494- -1.866435))