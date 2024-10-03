import numpy as np
from math import cos

"""Numpy — это библиотека для работы с массивами и матрицами в Python. 
Она предоставляет эффективные инструменты для численных расчетов, линейной алгебры, 
многомерного анализа данных и научных вычислений.
Некоторые из возможностей библиотеки:
1) Ввысокая производительность
2) Богатая функциональность
3) Легкость использования
4) Параллелизация и распределенные вычисления
5) Портабельность
6) Мощные возможности визуализации"""

b = np.array([[1, 2, 3], [4, 5, 6]]) #Создаем двумерный массив
print(b.ndim) # Функция ndim считает количество измерений массива, у меня двумерный
print(b.shape) # Фукция shape считает количсетво строк и столбцов
print(b.dtype) # Функци dtupe позволяет узнать тип элемента, у меня int64, массив содержит 64-битные целые числа

'''Массивы из NumPy поддерживают все стандартные арифметические операции —
 например, сложение, деление, вычитание. Работает это поэлементно'''

a = np.array([1, 2, 3, 4])
print(a + 3) #К Каждому элементу массива добавили 3

a = np.array([[1, 2], [3, 4]])
b = np.array([[2, 2], [2, 2]])
print(a + b) # В данной операции к каждому элементу массива а добавляется элемент массива b

a = np.array([[1, 2], [3, 4]])
print(np.cos(a)) # Вычисляем косинус

a = np.ones((2, 3)) #Создаем двумерный массив, заподненный единицами
b = np.full((3, 2), 2) #Создаем трехмерный массив, заполненный одним и тем же элементом "2"
print(np.matmul(a, b)) #Перемножаем массивы правилами линейной алгебры 