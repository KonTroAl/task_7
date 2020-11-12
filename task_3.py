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

origin_lst = [3, 4, 3, 3, 5, 3, 3]

# m = int(input("Введи размер массива: "))

# origin_lst = [random.randint(0, 100) for _ in range(2*m + 1)]

right = []
left = []


def my_func(lst):
    n = 0
    my_median = origin_lst[n]
    while True:
        if
        for i in range(len(origin_lst)-1):
            if my_median < origin_lst[i + 1]:
                left.append(origin_lst[i + 1])
            elif my_median >= origin_lst[i + 1]:
                right.append(origin_lst[i + 1])

        return left, right


print(origin_lst)
print(median(origin_lst))
print(my_func(origin_lst))