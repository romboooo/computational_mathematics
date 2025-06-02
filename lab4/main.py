import numpy as np

from cubeApprox import cubeApprox
from exponentialApprox import exponentialApprox
from linearApprox import linealApprox
from squareApprox import squareApprox
from powerApprox import powerApprox

def func(x):
    return 12 * x / (x**4 + 1)

def readData():
    with open("input.txt", "r") as file:
        x = np.array(list(map(float, file.readline().split())))
        y = np.array(list(map(float, file.readline().split())))
    return x, y
    
def main():
    x,y = readData()
    if len(x) != len(y):
        print("ошибка ввода точек")
        return
    print("--- Вычисления ---")
    
    squareData = squareApprox(x, y)
    linearData = linealApprox(x,y)
    cubeData = cubeApprox(x,y)
    powerData = powerApprox(x,y)
    expData = exponentialApprox(x,y)

if __name__ == "__main__":
    main()
