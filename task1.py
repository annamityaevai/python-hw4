# Задача 1. Даны два неупорядоченных набора целых чисел (может быть, с 
# повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами 
# элементы множеств.

n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
n_list = []

for i in range(n):
    numn = int(input('Введите элемент первого множества: '))
    n_list.append(numn)

m_list = []
for j in range(m):
    numm = int(input('Введите элемент второго множества: '))
    m_list.append(numm)

# z_list = []
# for i in n_list:
#     for j in m_list:
#         if i == j:
#             z_list.append(i)
#             break

z_list = list(set(n_list) & set(m_list))

print(*sorted(z_list))