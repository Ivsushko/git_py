def func_upper():
    '''
    Принимает на вход строку, возвращает ее
    со всеми заглавными буквами
    '''
    s = input("Введите предложение: ")
    print(s.upper())
    print(func_upper.__doc__)

func_upper()
