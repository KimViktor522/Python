objects = [0, 1, 2, 1, 2, 3, 2, 4, 4]
ans = 0
check = 0
for i in range(len(objects)):
    check = 0
    for j in range(i):
        if objects[j] is objects[i]:
            check = 1
            break
    if check == 0:
        ans += 1
print(ans)
