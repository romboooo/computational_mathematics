def func(x):
    return 2.74 * x ** 3 - 1.93 * x ** 2 - 15.28 * x - 3.72
def func2(xi, xi1):
    return xi - ((xi-xi1)/(func(xi) - func(xi1)))*func(xi)

def fi(x):
    return (2.74*x**3 - 1.93*x**2 - 3.72)/15.28


print(fi(-0.259349))
print(func(fi(-0.259349)))
print(abs(fi(-0.259349) - -0.259349))