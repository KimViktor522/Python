n = []
for i in range(3):
    n.append(input().split())
if (n[0] >= 100 || n[1] >= 100 || n[2] >= 100 || n[0] + n[1]> n[2] || n[1] + n[2]> n[0]|| n[2] + n[0]> n[1]):
    print("NO")
else: if (n[1] == n[2] && n[0] == n[2])
    print("RVS")
else: if (n[1] == n[2] || n[0] == n[2] || n[0] == n[2])
    print("RVB")
else:
    print("RZS")
