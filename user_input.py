def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


def clean_data(text):

    new_text = ''
    for letter in text:
        if letter not in ('!', '?', ' ', '.', ','):
            new_text += letter.lower()
    return new_text


while True:
    print(30*'*')
    print('Для выхода нажмите "Ctrl + C"')
    user_input = input('Введите текст: ')
    print(clean_data(user_input))
    if is_palindrome(clean_data(user_input)):
        print('Да, это палиндром!')
    else:
        print('Нет, это не палиндром!')
