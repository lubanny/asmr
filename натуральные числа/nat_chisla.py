'''
Входные данные
Входной файл INPUT.TXT содержит два натуральных числа M и N, разделенных пробелом (2 ≤ M ≤ N ≤ 106)

Выходные данные
В выходной файл OUTPUT.TXT выведите все простые числа от M до N в порядке возрастания, по одному в строке. Если таковых чисел нет, то следует вывести «Absent».


я запуталась...
'''
inp = open('input.txt', 'r')
out = open('output.txt', 'w')
lst = inp.readlines()
def fn(n1, n2):
    answer = []
    if n1 == n2 : print('Asbent')
    for i in range(n1, n2 + 1):
        for j in range(n1, i):
            if i % j == 0:
                break
            else:
                answer.append(i)
                print(i)
            break
    return lst

for ls in range(1, len(lst)):
    n1 = lst[1]
    n2 = lst[2]
    answer1 = str(fn(n1, n2))
    print(fn(n1, n2))
    out.write(answer1)