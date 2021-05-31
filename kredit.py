import math
n = list(map(float, input().split()))
M = (n[0]*(n[2]/100)*pow(1+(n[2]/100),n[1]))/(12*(pow((1+(n[2]/100)),n[1])-1))
S = (M*12)*n[1]
print(round(M, 2),round(S, 2))
