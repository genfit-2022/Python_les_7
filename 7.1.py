#   1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
#   который должен принимать данные (список списков) для формирования матрицы.
#
#   Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#
#   Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

#       31    32         3    5    32        3    5    8    3
#       37    43         2    4    6         8    3    7    1
#       51    86        -1   64   -8
#
#   Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#
#   Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
#   (двух матриц). Результатом сложения должна быть новая матрица.
#
#   Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
#   складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, ls_1, ls_2):
        # self.matr = [ls_1, ls_2]
        self.ls_1 = ls_1
        self.ls_2 = ls_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.ls_1)):

            for j in range(len(self.ls_2[i])):
                matr[i][j] = self.ls_1[i][j] + self.ls_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))



prim = Matrix([
    [23, 76, 12],
    [6, 33, 28],
    [41, 41, 9]
],

    [
    [51, 33, 88],
    [6, 12, 12],
    [29, 6, 8]
    ]
)

print(prim.__add__())