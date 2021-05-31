#Совершенное число - это такое число, которое равно сумме всех своих делителей, кроме себя самого.
s = ''
n = int(input())
for i in range(2, n):
    sum = 0
    for j in range(1, int(i/2)+1):
        if (i % j == 0):
            sum += j
    if (sum == i):
        s = s + str(i) + ' '
print(s)
