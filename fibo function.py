def fibo(n,k,num1,num2):
    if n == 0:
        return num1
    elif n == 1:
        return num2
    elif n == k:
        return num2
    else:
        k += 1
        #print(num1,num2,"\n",k)
        num1,num2 = num2,num1+num2
        return fibo(n,k,num1,num2)
n = int(input("number fibo: "))
print(fibo(n,1,0,1))
        
        
