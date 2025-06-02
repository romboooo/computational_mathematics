from typing import Dict
import numpy as np

from methods.cubeApprox import cubeApprox
from methods.exponentialApprox import exponentialApprox
from methods.linearApprox import linealApprox
from methods.squareApprox import squareApprox
from methods.powerApprox import powerApprox
from methods.logApprox import logApprox


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
    logData = logApprox(x,y)
   
if __name__ == "__main__":
    main()
