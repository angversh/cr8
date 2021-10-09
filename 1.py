def  dyadic(x): #задаем функцию для двоичной системы счисления
    a = ''
    while x != 0: 
        a = str(x%2) + a 
        x //= 2 
    return a
def  octal(x): #задаем функцию для восьмеричной системы счисления
    a = ''
    while x != 0:
        a = str(x%8) + a
        x //= 8
    return a
x = int(input('Input a decimal number:')) #ввод десятичного числа
x0 = x
while 1:
    try:
        y = int(input('Input a numeric base:')) #ввод двоичной или восьмеричной системы
        if y == 2 or y == 8:
            break
        else:
            print('Error. Input a numeric base equivalent to 2 or 8')
            continue
    except:
        print('Error')
        continue
if y == 2:
    print(x0, '->', dyadic(x)) #выводим число в двоичной системе
else:
    print(x0, '->', octal(x)) #выводим число в восьмеричной системе
    