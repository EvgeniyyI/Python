import numpy as np


def task1():
    x = 2.57 * 10 ** 3
    f = 0.873
    y = (np.power(np.sin(np.pi / 8 - f), 2) + np.power((3 + x ** 2), 0.25)) / 2
    return y


def task2():
    matrixX = np.ones((12, 3))
    matrixX[:, 1] = np.random.randint(9, 21, size=12)
    matrixX[:, 2] = np.random.randint(60, 82, size=12)
    print("Матрица Х:\n", matrixX)
    Y = np.random.uniform(13.5, 18.6, size=12).reshape(-1, 1)
    print("Вектор столбец Y:\n", Y)
    A = np.linalg.inv(matrixX.T @ matrixX) @ (matrixX.T @ Y)
    print("Оценки уравнения регрессии:\n", A)


print("Задание 1.1.\n", "y =", task1().round(3))
print("\nЗадание 1.2\n")
task2()
