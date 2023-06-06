def func_upper():
    '''
    Принимает на вход строку, возвращает ее
    со всеми заглавными буквами
    '''
    s = input("Введите предложение: ")
    print(s.upper())
    print(func_upper.__doc__)


def func_first_upper():
    '''
    Принимает на вход строку, возвращает ее
    с заглавными первыми буквами каждого слова
    '''
    s = input("Введите предложение: ")
    print(s.title())
    print(func_upper.__doc__)

    
   
