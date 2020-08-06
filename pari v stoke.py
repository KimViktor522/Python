def proces_str(str):
    for i in range(len(str)):
        check = 0
        for j in range(i+1,len(str)):
            if (str[i] == str[j]):
                check = 1
                str = str.replace(str[i], '0', 1)
                str = str.replace(str[j], '0', 1)
                break
    return str

def search_min_sum(str):
    sum = 0
    for i in range(len(str)):
        if (str[i] != '0'):
            sum += 1
    return sum

str = str(input('Введите строку :'))
#str = "abbcddka"
print('Ваша строка: ', str)
str = proces_str(str)
print('Мин нужно удалить :',search_min_sum(str))

