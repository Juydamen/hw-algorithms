'''Условие задачи "Лишняя буква":
Васе очень нравятся задачи про строки, поэтому он придумал свою.
Есть 2 строки s и t, состоящие только из строчных букв.
Строка t получена перемешиванием букв строки s и добавлением 1 буквы в случайную позицию.
Нужно найти добавленную букву.
'''

'''Формат ввода:
На вход подается кортеж, содержащий строки s и t.
'''

'''Формат вывода:
Выведите лишнюю букву.
'''

# Пример ввода -> вывода:
inputs = [
    ('abcd', 'abcde'),   # -> e
    ('go', 'ogg'),       # -> g
    ('xtkpx', 'xkctpx')  # -> c
]

# тут ваше решение:


#Example1
# for i in inputs:
#     s, t = i[0], i[1]
#     for j in t:
#         if t.count(j) > 1 and s.count(j) == 1:
#             print(j)
#             break
#         elif s.count(j) == 0:
#             print(j)



#Example2


# def find_char(first_string, second_string):
#     print(list(zip(first_string, second_string)))
#     for first_char, second_char in zip(first_string, second_string):
#         if first_char != second_char:
#             return second_char
#     return second_string[-1]


# for input in inputs:
#     first_string = list(input[0])
#     second_string = list(input[1])
#     first_string.sort()
#     second_string.sort()
#     print(find_char(first_string, second_string=second_string))



#Example3


def find_extra_letter(t1, t2):
    sum_s = sum(ord(ch) for ch in t1)
    sum_t = sum(ord(ch) for ch in t2)
    return chr(sum_t - sum_s)


for t1, t2 in inputs:
    print(find_extra_letter(t1, t2))  # e g c