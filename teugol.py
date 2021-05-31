a = int(input())
b = int(input())
c = int(input())
if (a >= 100 or b >= 100 or c >= 100 or a + b > c or b + c > a or c + a > b):
    print("NO")
elif (b == c and a == c):
        print("RVS")
elif (b == c or a == c or a == c):
        print("RVB")
else:
    print("RZS")
