def func_upper():
    s = input("Введите предложение: ")
    print(s.upper())

def func_first_upper():
    '''
    Принимает на вход строку, возвращает ее
    с заглавными первыми буквами каждого слова
    '''
    s = input("Введите предложение: ")
    print(s.title())
    print(func_upper.__doc__)

def func_first_word():
    '''
    Принимает на вход строку, возвращает ее
    с заглавной  буквой первого слова
    '''
    s = input("Введите предложение: ")
    print(s.capitalize())
    print(func_upper.__doc__)

