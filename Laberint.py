n = int(input())
start = []
start.append(list(map(int, input().split())))
finish = []
finish.append(list(map(int, input().split())))
lab = []
for i in range(n):
    lab.append(list(map(int, input().split())))
n = 4
start = [['4', '1']]
finish = [['1', '4']]
lab = [[1, 1, 0, 0],
       [0, 0, 1, 0],
       [1, 0, 0, 0],
       [0, 0, 1, 0]]


print(start)
print(finish)
print(lab)
