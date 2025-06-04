from typing import Dict
import numpy as np

from methods.cubeApprox import cubeApprox
from methods.exponentialApprox import exponentialApprox
from methods.linearApprox import linealApprox
from methods.squareApprox import squareApprox
from methods.powerApprox import powerApprox
from methods.logApprox import logApprox


names = {
    1: "Кубическая",
    2: "Экспоненциальная",
    3: "Линейная",
    4: "Логарифмическая",
    5: "Степенная",
    6: "Кубическая"
}

def readData():
    with open("input.txt", "r") as file:
        x = np.array(list(map(float, file.readline().split())))
        y = np.array(list(map(float, file.readline().split())))
    return x, y

def countResult(arr):
    print("")
    print("--- Подсчёт результатов ---")
    minDelta = 1000000
    bestModel = None
    for func in arr:
        if func.get('delta') < minDelta:
            bestModel = func
            minDelta = func.get('delta')

    print(f"Лучшая модель: {names.get(bestModel.get('name'))}")
    print(f"Значение СКО: {bestModel.get('delta')}")

    
def main():
    x,y = readData()
    if len(x) != len(y):
        print("ошибка ввода точек")
        return
    print("--- Вычисления ---")
    results = [
        squareApprox(x, y),
        linealApprox(x,y),
        cubeApprox(x,y),
        powerApprox(x,y),
        exponentialApprox(x,y),
        logApprox(x,y)
    ]
    countResult(results)

    # print(""" todo: 
    # 1. доделать експоненциальную аппроксимацию+
    # 2. сделать метод выявления лучшего метода
    # 3. графики
    # """)
if __name__ == "__main__":
    main()
