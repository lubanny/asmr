'''
Будем говорить, что число a лучше числа b, если сумма цифр a больше суммы цифр числа b, а в случае равенства сумм их цифр, если число a меньше числа b. Например, число 124 лучше числа 123, так как у первого из них сумма цифр равна семи, а у второго – шести. Также, число 3 лучше числа 111, так как у них равны суммы цифр, но первое из них меньше.

Дано число n. Найдите такой его делитель (само число n и единица считаются делителями числа n), который лучше любого другого делителя числа n.

Входные данные
Первая строка входного файла содержит целое число n (1 ≤ n ≤ 105).

Выходные данные
В выходной файл выведите ответ на задачу.
'''
divs = set()
n = 10
for d in range(1, int(n ** 0.5) + 1):
    if n % d == 0:
        divs.add( d )
        divs.add( n // d )
for dv in divs:
    sm, sm1 = 0, 0
    cnt, cnt1 = 0, 0
    num, num1 = 0, 0
    while dv != 0:
        sm1 += dv % 10
        cnt1 += 1
        dv //= 10
    if sm1 > sm : sm1 == sm and cnt1 == cnt
    if sm1 == sm and cnt1 > cnt : num1 == num
    if sm1 == sm and cnt1 < cnt : num == num1
    cnt1 = 0
    sm1 = 0
    num1 = 0


print( sm )

