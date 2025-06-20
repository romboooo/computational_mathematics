import math

def choose_odu():
    print("Выберете ОДУ:")
    print("1. x + y")
    print("2. sin(x) - y")
    print("3. y / x")

    while True:
        try:
            input_func = int(input('> Выберите ОДУ [1/2/3]: '))
            if input_func == 1:
                f = lambda x, y: x + y
                exact_y = lambda x, x0, y0: math.exp(x - x0) * (y0 + x0 + 1) - x - 1
                break
            elif input_func == 2:
                f = lambda x, y: math.sin(x) - y
                exact_y = lambda x, x0, y0: (2*math.exp(x0)* y0-math.exp(x0)*math.sin(x0)+math.exp(x0)*math.cos(x0)) / (2*math.exp(x)) + (math.sin(x)) / 2 - (math.cos(x)) / 2
                break
            elif input_func == 3:
                f = lambda x, y: y / x
                exact_y = lambda x, x0, y0: (x*y0) / x0
                break
            else:
                print("Некоррентный ввод! Попробуйте еще")

        except:
            print("Некоррентный ввод! Попробуйте еще")
    return f, exact_y

def read_data():
    while True:
        try:
            x0 = float(input("Введите первый элемент интервала x0: "))
            xn = float(input("Введите последний элемент интервала xn: "))
            n = int(input("Введите количество элементов в интервале n: "))
            y0 = float(input("Введите y0: "))
            epsilon = float(input("Введите точность epsilon: "))
            break
        except:
            print("Некорректный ввод, попробуем еще раз!")
    return x0, xn, n, y0, epsilon