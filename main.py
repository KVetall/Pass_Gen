from random import *

digits = [str(i) for i in range(10)]
alpha_low = [chr(i) for i in range(97, 123)]
alpha_upp = [chr(i) for i in range(65, 91)]
punctuation = list('!#$%&*+-=?@^_')
chars = ''.join(digits + alpha_upp + alpha_low + punctuation)
len_pass = int(input('Введите число - длинну генерируемого пароля: '))


def gen_password(lenght, symbols):
    password = ''
    if 13 >= lenght >= 8:
        for char in range(lenght):
            password += choice(symbols)
        return password
    else:
        return 'Длинна пароля должна быть от 8 до 13 символов!'


print(gen_password(len_pass, chars))
