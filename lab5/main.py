import numpy as np

from methods.lagrange import lagrange
import time

def readData():
    print("каким образом вводим данные?")
    while True:
        print("ответ принимается в формате (f/c)")
        inp = input()   
        inp = inp.lower()
        if inp == "c" or inp == "f":
            break
        print("неверный ввод")

    if inp == "c":
        return readFromConsole()
    return readFromFile()


def readFromConsole():
    print("Введите значения x через пробел:")
    x = np.array(list(map(float, input().split())))
    print("Введите значения y через пробел:")
    y = np.array(list(map(float, input().split())))
    print("Введите значение xi:")
    xi = input().strip()
    return x, y, xi

def dispatchToConsole():
    print("Возникла ошибка, желаете ввести данные с консоли?")
    while True:
        print("(y/n)")
        inp = input()   
        inp = inp.lower()
        if inp == "y" or inp == "n":
            break
        print("неверный ввод")
    if inp == "y":
        return readFromConsole() 
    print("программа завершается")
    time.sleep(2)
    exit()

import numpy as np

def readFromFile():
    try:
        with open("input.txt", "r") as file:
            lines = file.readlines()  
            
            if len(lines) < 3:
                print("Ошибка: файл должен содержать 3 строки")
                return dispatchToConsole()
            
            x = np.array(list(map(float, lines[0].split())))
            y = np.array(list(map(float, lines[1].split())))
            
            xi_str = lines[2].strip()
            
            if not xi_str:
                print("Ошибка: третья строка пустая")
                return dispatchToConsole()
                
            
            try:
                xi = float(xi_str)
            except ValueError:
                print("Ошибка: в третьей строке должно быть одно число")
                return dispatchToConsole()
    
    except FileNotFoundError:
        print("Файл input.txt не найден")
        return dispatchToConsole()
    except (ValueError, TypeError):
        print("Ошибка формата данных: ожидались числа в первых двух строках")
        return dispatchToConsole()
    except Exception as e:
        print(f"Ошибка при чтении файла: {str(e)}")
        return dispatchToConsole()
    
    if len(x) != len(y) or len(x) == 0:
        print("Ошибка: массивы x и y разной длины или пустые")
        return dispatchToConsole()
    return x, y, xi



def main():
    x,y,xi = readData()
    print(lagrange(x,y,xi))

if __name__ == "__main__":
    main()

