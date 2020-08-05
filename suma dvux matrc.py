import random

def generate_mas(mas):
    for i in range(n):
        curMas = []
        for j in range(n):
            curMas.insert(j, random.randint(1,10))
        mas.insert(i, curMas)
    return mas

def print_mas(mas):
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            print(mas[i][j], end = ' ')
        print()

def creat_mas(mas1,mas2):
    newMas = []
    for i in range(n):
        curMas = []
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += mas1[i][k]*mas2[k][j]
            curMas.insert(j, sum)
        newMas.insert(i, curMas)
    return newMas
            
n = int(input('Размер матрицы :'))
mas1 = []
mas2 = []
mas1 = generate_mas(mas1)
mas2 = generate_mas(mas2)
print('\nmas1:')
print_mas(mas1)
print('\nmas2:')
print_mas(mas2)
newMas = []
newMas = creat_mas(mas1,mas2)
print('\nnew mas3:')
print_mas(newMas)
