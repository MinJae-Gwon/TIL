def calc(equation):
    copy_e =equation
    opera=[]
    num=[]
    for no_digit in equation:
        if not no_digit.isdigit():
            opera.append(no_digit)
            equation = equation.replace(no_digit,' ')
    num = equation.split()
    
    res=0
    if copy_e[0] == '+' or copy_e[0] == '-':
        for i in range(len(num)):
            if opera[i]=='+':
                res+=int(num[i])
            else:
                res-=int(num[i])
    else:
        opera = ['+']+opera
        for i in range(len(num)):
            if opera[i]=='+':
                res+=int(num[i])
            else:
                res-=int(num[i])
       
    return res
print(calc('123+2-124'))
print(calc('-12+12-7979+9191'))
print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))