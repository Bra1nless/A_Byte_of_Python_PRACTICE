class ShortInputExceptions(Exception):
    '''Пользовательский класс исключения'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input("Enter something: ")
    if len(text) < 3:
        raise ShortInputExceptions(len(text), 3)
except EOFError:
    print('Unexpected EOF')
except ShortInputExceptions as ex:
    print(f'ShortInputException: длинна введенной строки -- {ex.length}. '
          f'Ожидалось минимум {ex.atleast}')
else:
    print('Не было исключений!')