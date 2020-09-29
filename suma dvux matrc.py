import random

#Рандомно чоздает массив 
def generate_mas(n, m, mas):
    for i in range(n):
        curMas = []
        for j in range(m):
            curMas.insert(j, random.randint(1,10))
        mas.insert(i, curMas)
    return mas

#Ввод вручную 
def input_mas(n, m, mas):
    for i in range(n):
        curMas = []
        print("Строка (", i+1, "/", n, ") [", m, "]: ", end = '', sep = '')
        curMas = input().split()
        if (len(curMas) != m):
            raise SystemExit("Некорректный ввод!!!")
        for j in range(len(curMas)):
            curMas[j] = int(curMas[j])
        mas.insert(i, curMas)
    return mas

#Выводит масив 
def print_mas(mas):
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            print(mas[i][j], end = ' ')
        print()

#Создает новый массив из произведения двух входных
def creat_mas(n, m, k, mas1,mas2):
    newMas = []
    for i in range(n):
        curMas = []
        for j in range(k):
            sum = 0
            for p in range(m):
                sum += mas1[i][p]*mas2[p][j]
            curMas.insert(j, sum)
        newMas.insert(i, curMas)
    return newMas
            
n = int(input('Размер матрицы 1 (строки): '))
"""m = int(input('\nРазмер матрицы 1 (столбцы): '))
if (m != int(input('\nРазмер матрицы 2 (строки): '))):
    raise SystemExit("Некорректный ввод!!!")
k = int(input('\nРазмер матрицы 2 (столбцы): '))"""
m = k = n
mas1 = []
mas2 = []
if (str(input('\nВвод вручную? (y/n): ')) == 'n'):
    mas1 = generate_mas(n, m, mas1)
    mas2 = generate_mas(m, k, mas2)
else:
    mas1 = input_mas(n, m, mas1)
    mas2 = input_mas(m, k, mas2)
    
print('\nmas1:')
print_mas(mas1)
print('\nmas2:')
print_mas(mas2)
newMas = []
newMas = creat_mas(n, m, k, mas1,mas2)
print('\nnew mas3:')
print_mas(newMas)
