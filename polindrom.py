n = str(input())
n = n.replace(' ', '')
print(n)
if (n == n[::-1]):
    print("YES")
else:
    print("NO")
