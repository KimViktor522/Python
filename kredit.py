import math
n = list(map(float, input().split()))
M = (n[0]*(n[1]/100)*pow(1+(n[1]/100),n[2]))/(12*(pow((1+(n[1]/100)),n[2])-1))
S = (M*12)*n[2]
print(round(M, 2),round(S, 2))
