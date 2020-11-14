"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
import timeit
import random
from statistics import median

# origin_lst = [3, 4, 3, 3, 5, 3, 3]

m = int(input("Введи размер массива: "))

origin_set = {random.randint(0, 100) for _ in range(2 * m + 1)}
origin_lst = list(origin_set)


def my_func(lst):
    right = []
    left = []
    n = 0
    while len(right) == 0 and len(left) == 0:
        my_median = origin_lst[n]
        for i in range(len(origin_lst)):
            if my_median < origin_lst[i]:
                left.append(origin_lst[i])
            elif my_median > origin_lst[i]:
                right.append(origin_lst[i])
        if len(right) == len(left):
            return origin_lst[n]
        n += 1
        right.clear()
        left.clear()


print(origin_lst)
print(median(origin_lst))
print(my_func(origin_lst))

"""Медианой будет тот элемент при котором получится разделить исходный список на два одинаковых по размеру массива"""
