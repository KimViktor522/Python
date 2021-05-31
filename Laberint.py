# -1 - это стена
# 0 - проход
# -5 - начало
# -10 - выход

n = int(input())
start = list(map(int, input().split()))
finish = list(map(int, input().split()))
lab = []
for i in range(n):
    lab.append(list(map(int, input().split())))
Copy_lab = lab

def find_way(i, j, position):
    prov = 1
    if (i + 1 < n) and (Copy_lab[i + 1][j] == 0):
        Copy_lab[i + 1][j] = position + 1
        prov = 0
        if (find_finish(i + 1,j) == 0):
            print("YES")
            exit()
    if (i - 1 >= 0) and (Copy_lab[i - 1][j] == 0):
        Copy_lab[i - 1][j] = position + 1
        prov = 0
        if (find_finish(i - 1,j) == 0):
            print("YES")
            exit()
    if (j + 1 < n) and (Copy_lab[i][j + 1] == 0):
        Copy_lab[i][j + 1] = position + 1
        prov = 0
        if (find_finish(i,j + 1) == 0):
            print("YES")
            exit()
    if (j - 1 >= 0) and (Copy_lab[i][j - 1] == 0):
        Copy_lab[i][j - 1] = position + 1
        prov = 0
        if (find_finish(i,j - 1) == 0):
            print("YES")
            exit()
    return prov

def find_finish(i, j):
    prov = 1
    if (i + 1 < n) and (Copy_lab[i + 1][j] == -10):
        prov = 0
    if (i - 1 >= 0) and (Copy_lab[i - 1][j] == -10):
        prov = 0
    if (j + 1 < n) and (Copy_lab[i][j + 1] == -10):
        prov = 0
    if (j - 1 >= 0) and (Copy_lab[i][j - 1] == -10):
        prov = 0
    return prov


for i in range(n):
    for j in range(n):
        if (Copy_lab[i][j] == 1):
            Copy_lab[i][j] = -1
#Если в стене
if (Copy_lab[start[0]-1][start[1]-1] == -1) or (Copy_lab[finish[0]-1][finish[1]-1] == -1):
    print("NO")
    exit()
Copy_lab[start[0]-1][start[1]-1] = -5
Copy_lab[finish[0]-1][finish[1]-1] = -10
сheck = 0
position = -5
while (сheck == 0):
    for i in range(n):
        for j in range(n):
            if (position == Copy_lab[i][j]):
                if (position == -5):
                    position = 0
                if (сheck == 0):
                    сheck = find_way(i, j, position)
                else:
                    find_way(i, j, position)
                if (Copy_lab[i][j] == -5):
                    position = Copy_lab[i][j]
            print(lab,i,j,position)
            input()
    if (position == -5):
        position = 0
    position += 1
print("NO")
