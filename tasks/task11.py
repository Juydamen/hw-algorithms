'''Условие задачи "Клумбы":
Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам. На схеме земельного участка клумбы обозначаются
просто горизонтальными отрезками, лежащими на одной прямой. Для ландшафтных работ было нанято n садовников.
Каждый из них обрабатывал какой-то отрезок на схеме. Процесс был организован не очень хорошо, иногда один и тот же отрезок или его
часть могли быть обработаны сразу несколькими садовниками. Таким образом, отрезки, обрабатываемые двумя разными садовниками, сливаются в один.
Непрерывный обработанный отрезок затем станет клумбой. Нужно определить границы будущих клумб.

Рассмотрим пример:
Отрезки
[2,3], [3,4] и [3,4] сольются в один отрезок [2,4]. Отрезок [5,6] ни с кем не объединяется, добавляем его в ответ.
'''

'''Формат ввода:
В строке через пробел записаны координаты клумб в формате: start end, где start — координата начала, end — координата конца.
Оба числа целые, неотрицательные. start строго меньше, чем end.
'''

'''Формат вывода:
Нужно вывести координаты каждой из получившихся клумб в отдельных строках.
Данные должны выводится в отсортированном порядке — сначала клумбы с меньшими координатами, затем — с бОльшими.
'''

# Пример ввода -> вывода:
inputs = [
    [
        '7 8', '7 8', '2 3', '6 10'  # -> '2 3' '6 10'
    ],
    [
        '2 3', '5 6', '3 4', '3 4'  # -> '2 4' '5 6'
    ],
    [
        '1 3', '3 5', '4 6', '5 6', '2 4', '7 10'  # -> '1 6' '7 10'
    ]
]

# тут ваше решение:


# def clumba(n):
#     e = []
#     for j in n:
#         e.append([int(i) for i in j.split(" ")])
#     q = [e[i] for i in range(len(e)) if e[i] not in e[i + 1:]]
#     print(q)
#     i = 0
#     while 1:
#         if 

# print(clumba(['2 3', '3 4', '5 6', '3 4']))

#Example 1
# def sort_key(array):
#     return array[1]


# for input in inputs:
#     n = len(input)
#     coordinates_string = [num.split() for num in input]
#     coordinates = []
#     for coordinate in coordinates_string:
#         coordinate = list(map(int, coordinate))
#         coordinates.append(coordinate)
#     coordinates = sorted(coordinates, key=sort_key)

#     k = n - 1
#     while k > 0:
#         if coordinates[k][0] >= coordinates[k - 1][0] \
#                 and coordinates[k][1] >= coordinates[k - 1][1] \
#                 and coordinates[k][0] <= coordinates[k - 1][1]:
#             coordinates[k][0] = coordinates[k - 1][0]
#             coordinates.pop(k - 1)
#         elif coordinates[k][0] <= coordinates[k - 1][0] \
#                 and coordinates[k][1] >= coordinates[k - 1][1]:
#             coordinates.pop(k - 1)
#         elif coordinates[k][0] >= coordinates[k - 1][0] \
#                 and coordinates[k][1] <= coordinates[k - 1][1]:
#             coordinates.pop(k)
#         k -= 1

#     for coordinate in coordinates:
#         print((' '.join(list(map(str, coordinate)))))
#     print()

#Example 2
def merge_intervals(intervals):
    intervals = sorted(intervals)
    result = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= result[-1][1]:
            result[-1] = (result[-1][0], max(result[-1][1], interval[1]))
        else:
            result.append(interval)
    return result


for ints in inputs:
    intervals = [list(map(int, n.split())) for n in ints]
    intervals = merge_intervals(intervals)
    for interval in intervals:
        print(interval[0], interval[1])