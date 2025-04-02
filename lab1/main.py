class Values:
    def __init__(self, coefMatrix, svobodChlenMatrix, epsilon):
        self.coefMatrix = coefMatrix
        self.svobodChlenMatrix = svobodChlenMatrix
        self.epsilon = epsilon

    coefMatrix = []
    svobodChlenMatrix = []
    epsilon = 0


def inputValues():
    while True:
        try:
            n = int(input("Введите количество уравнений (и переменных) системы: "))
            if n <= 0:
                print("Число уравнений должно быть положительным.")
                continue
            break
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите целое число.")

    coefMatrix = []
    svobodChlenMatrix = []

    for i in range(n):
        while True:
            try:
                row = list(
                    map(
                        int,
                        input(
                            f"Введите коэффициенты {i+1}-го уравнения через пробел: "
                        ).split(),
                    )
                )
                if len(row) != n:
                    print(f"Ошибка: должно быть {n} коэффициентов.")
                    continue
                coefMatrix.append(row)
                break
            except ValueError:
                print("Ошибка ввода. Пожалуйста, введите только целые числа.")

    while True:
        try:
            svobodChlenMatrix = list(
                map(
                    int, input("Введите свободные члены системы через пробел: ").split()
                )
            )
            if len(svobodChlenMatrix) != n:
                print(f"Ошибка: должно быть {n} свободных членов.")
                continue
            break
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите только целые числа.")
    while True:
        try:
            print("введите ε")
            epsilon = float(input())
            break
        except ValueError:
            print("Ошибка ввода.")

    print("\nМатрица коэффициентов:")
    for row in coefMatrix:
        print(row)
    print("\nВектор свободных членов:", svobodChlenMatrix)
    print("ε: ", epsilon)
    print("данные введены верно? 1/0")
    if int(input()) == 0:
        inputValues(
            coefMatrix=coefMatrix, svobodChlenMatrix=svobodChlenMatrix, epsilon=epsilon
        )
    else:
        return Values(
            coefMatrix=coefMatrix, svobodChlenMatrix=svobodChlenMatrix, epsilon=epsilon
        )


def is_diagonally_dominant(matrix):
    n = len(matrix)
    for i in range(n):
        diag = abs(matrix[i][i])
        sum_rest = sum(abs(matrix[i][j]) for j in range(n) if j != i)
        if diag < sum_rest:
            return False
    return True


def rearrange_matrix(matrix):
    n = len(matrix)
    if n == 0:
        return matrix, []

    unique_rows = []
    for row in matrix:
        if row not in unique_rows:
            unique_rows.append(row)

    if len(unique_rows) < n:
        print("В матрице есть одинаковые строки. Они будут обработаны как одна.")

    graph = [[] for _ in range(n)]
    for j in range(n):
        for i in range(n):
            dominateDiagElement = abs(matrix[j][i])
            sum_rest = sum(abs(matrix[j][k]) for k in range(n) if k != i)
            if dominateDiagElement >= sum_rest:
                graph[i].append(j)

    # Алгоритм Куна
    match = [-1] * n
    visited = [False] * n

    def dfs(u):
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                if match[v] == -1 or dfs(match[v]):
                    match[v] = u
                    return True
        return False

    for u in range(n):
        visited = [False] * n
        dfs(u)

    perm = [-1] * n
    for j in range(n):
        if match[j] != -1:
            perm[match[j]] = j

    if -1 in perm:
        return None

    return perm

def normaCount(matrix) -> int:
    max = 0
    for i in range(0, len(matrix)):
        summ = sum(abs(matrix[i][j]) for j in range(0, len(matrix)))
        if summ > max:
            max = summ
    return max

def expressVariables(matrix, array):
    for i in range(0, len(matrix)):
        num = matrix[i][i]
        matrix[i][i] = 0
        if num == 0:
            print(f"нельзя выразить х{i+1} так как он равен нулю")
            return None
        if num == 1:
            for j in range(0, len(matrix)):
                if matrix[i][j] == matrix[i][i]:
                    continue
                matrix[i][j] = -matrix[i][j]
                continue

        if num != 1:
            array[i] = array[i] / num
            for j in range(0, len(matrix)):
                if matrix[i][j] == matrix[i][i]:
                    continue
                matrix[i][j] = -matrix[i][j] / num
                continue
    return matrix, array

def drawSlauSystem(matrix, array):
    print("Выразим диагональные коэффиценты")
    for i in range(0, len(matrix)):
        out = f"x{i+1} = "
        for j in range(0, len(matrix)):
            if matrix[i][j] != 0:
                if matrix[i][j] > 0:
                    out += f"+ {matrix[i][j]}x{j+1} "
                elif matrix[i][j] < 0:
                    out += f"{matrix[i][j]} x{j+1} "
        if array[i] != 0:
            if array[i] > 0:
                out += f"+ {array[i]} "
            elif array[i] < 0:
                out += f"{array[i]} "
        print(out)


def drawCMatrix(C):
    print("матрица C:")
    for row in C:
        print(row)
    print(" ")


def drawdMatrix(d):
    print("Матрица d:\n")
    print("[")
    for row in d:
        print(row)
    print("]\n")


def convergenceСondition(num):
    if num < 1:
        print(f"норма: {num} < 1 => условие сходимости выполняется, всё ок")
    else:
        print(f"норма: {num} !< 1 => условие сходимости не выполняется НО! продолжаем считать")


def absoluteDeviationCriterion(x_prev, x_current, epsilon):
    max_diff = max(abs(x_current[i] - x_prev[i]) for i in range(len(x_prev)))
    print(f"Максимальное отклонение: {max_diff}")
    if max_diff < epsilon:
        print(f"{max_diff} < {epsilon} → Критерий выполнен")
        return True, max_diff
    else:
        print(f"{max_diff} >= {epsilon} → Критерий не выполнен")
        return False, max_diff


def simpleIterations(C, d, epsilon):
    max_iterations = 100
    iteration = 0
    x_prev = d.copy()
    x_current = [0.0] * len(d)

    while iteration < max_iterations:
        print(f"\nИтерация {iteration + 1}:")
        for i in range(len(C)):
            x_current[i] = sum(C[i][j] * x_prev[j] for j in range(len(C))) + d[i]
            print(f"x_{i+1} = {x_current[i]:.4f}")

        is_stop, max_diff = absoluteDeviationCriterion(x_prev, x_current, epsilon)
        if is_stop:
            break

        x_prev = x_current.copy()
        iteration += 1

    return x_current


inputValues = inputValues()

if is_diagonally_dominant(inputValues.coefMatrix):
    print("Матрица уже обладает диагональным преобладанием.")
    print("Свободные члены:", inputValues.svobodChlenMatrix)

perm = rearrange_matrix(inputValues.coefMatrix)
if perm is not None:
    new_matrix = [inputValues.coefMatrix[i].copy() for i in perm]
    new_svobod = [inputValues.svobodChlenMatrix[i] for i in perm]

    print("Преобразованная матрица:")
    for row in new_matrix:
        print(row)
    print("Преобразованные свободные члены:", new_svobod)
    C, d = expressVariables(new_matrix, new_svobod)
    drawSlauSystem(new_matrix, new_svobod)

    drawCMatrix(C)
    drawdMatrix(d)

    normaCount(C)

    convergenceСondition(normaCount(C)) 
    simpleIterations(C, d, inputValues.epsilon)
else:
    print("Невозможно преобразовать матрицу.")
    drawSlauSystem(inputValues.coefMatrix, inputValues.svobodChlenMatrix)
    C, d = expressVariables(inputValues.coefMatrix, inputValues.svobodChlenMatrix)
    drawCMatrix(C)
    drawdMatrix(d)

    normaCount(C)

    convergenceСondition(normaCount(C))  
    simpleIterations(C, d, inputValues.epsilon)
