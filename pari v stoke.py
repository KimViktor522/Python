for i in range(5):
    print(i)
    for j in range(5):
        print(j, end = '')
        if (j==2):
            break
    print()


sum = 0
def proces_str(str):
    for i in range(len(str)):
        check = 0
        for j in range(i+1,len(str)):
            if (str[i] == str[j]):
                check = 1
                str.replace(str[i],"")
                str.replace(str[j],"")
                break
        print(str, str[i])
        if (check == 1):
            str.replace(str[i],"")
            sum += 1
    return str
#str = str(input())
str = 'abbcddk'
str = proces_str(str)
if (str == ''):
    print('Мин нужно удалить :',sum)
else:
    print('Ошибка!!!')

