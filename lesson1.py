# 1)Дан лист:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - найти min число в листе
#   - удалить все дубликаты в листе
#   - заменить каждое четвертое значение на "Х"
# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# 3) вывести табличку умножения с помощью цикла while
# 4) переделать первое задание под меню с помощью цикла
#
# ***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5

# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# print("Smallest element is:", min(list))
# def Remove(list):
#     final_list = []
#     for num in list:
#         if num not in final_list:
#             final_list.append(num)
#     return final_list
#
#
# print(Remove(list))

# list = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 2, 7, 9]
# liat_new = list.copy()
# for i in range(3, len(liat_new), 4):
#     liat_new[i] = 'X'
# print(liat_new)

# i = 1
# size = 10
# while i <= size:
#     j = 1
#     while j <= size:
#         res = i * j
#         if res // 10:
#             print(res, end='  ')
#         else:
#             print(res, end='   ')
#         j += 1
#     print()
#     i += 1
# num = 12
# for i in range(1, 11):
#    print(num, 'x', i, '=', num*i)

# n=int(input('Please enter a positive integer between 1 and 15: '))
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         print(row*col, end="\t")
#     print()

# a = 5
# i = a
# while i >= 1:
#     if i == a or i == 1:
#         j = a
#         while j > 0:
#             print('*', end='')
#             j -= 1
#         print()
#     else:
#         j = a - 2
#         print('*', end='')
#         while j > 0:
#             print(' ', end='')
#             j -= 1
#         print('*')
#     i -= 1


# import turtle
#
# t = turtle.Turtle()
#
# s = int(input("Enter the length of the side of the Square: "))
#
# t.forward(s)
# t.left(90)
#
#
# t.forward(s)
# t.left(90)
#
#
# t.forward(s)
# t.left(90)
#
#
# t.forward(s)
# t.left(90)
# l = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 2, 7, 9]




        # print('List =', l)
        # l.sort()
        # sum = 0
        # for i in l:
        #     sum += i
        # avg = sum / len(l)

