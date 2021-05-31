n = list(map(float, input().split()))
x = (n[3]-n[1])/(n[2]-n[0])
a = (n[2]*n[1]-n[0]*n[3])/(n[2]-n[0])
if a < 0:
    str = 'y='+str(round(x, 2))+'x+('+str(round(a, 2))+')'
else:
    str = 'y='+str(round(x, 2))+'x+'+str(round(a, 2))
print(str)
