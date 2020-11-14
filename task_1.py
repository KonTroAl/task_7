"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import timeit
import random
import copy

"""First"""


def bubble_sort_rev_1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return f"Отсортированный список: {lst_obj}."


orig_list = [random.randint(-100, 100) for _ in range(10)]

print(f"Оригинальный список: {orig_list}")
print(bubble_sort_rev_1(orig_list))

# замеры 10
print(timeit.timeit("bubble_sort_rev_1(orig_list)", \
                    setup="from __main__ import bubble_sort_rev_1, orig_list", number=1))

"""Second"""


def bubble_sort_rev_2(lst_obj):
    flag = 1
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag += 1
        if flag == 1:
            break
        n += 1
    return f"Отсортированный список: {lst_obj}. Количество проходов по списку: {flag}"


orig_list_copy = copy.deepcopy(orig_list)

print(f"Оригинальный список: {orig_list_copy}")
print(bubble_sort_rev_2(orig_list))

# замеры 10
print(timeit.timeit("bubble_sort_rev_2(orig_list_copy)", \
                    setup="from __main__ import bubble_sort_rev_2, orig_list_copy", number=1))


"""Оптимизация заключалась в проверке исходного списка на сортировку эелементов. Для того чтобы понять дала ли 
оптимизация результат необходимо было поместить тот же самый список в оптимизированную функцию и провести замеры времени.
Результат показала, что когда функция всего один раз проходит по списку, вермя исполнения значительно ниже."""
