from random import *
from tkinter import *

digits = [str(i) for i in range(10)]
alpha_low = [chr(i) for i in range(97, 123)]
alpha_upp = [chr(i) for i in range(65, 91)]
punctuation = list('!#$%&*+-=?@^_')
chars = ''.join(digits + alpha_upp + alpha_low + punctuation)
root = Tk()

root.title('Генератор паролей')
root.resizable(False, False)
root.geometry('300x260')

welcome = Label(text='Введите число - \nдлинну генерируемого пароля. \nДлина пароля должна быть \nот 8 до 13 символов\n', font='50')
welcome.pack()


def gen_password():
    num = enter_lengthPass.get()
    number = int(num)
    password = ''
    if 13 >= number >= 8:
        for char in range(number):
            password += choice(chars)
        result.insert(0.0, password, CENTER)
    else:
        result.insert(0.0, 'Error', CENTER)


def clear_all():
    enter_lengthPass.delete(0, END)
    result.delete(0.0, END)


enter_lengthPass = Entry(root, font='50', justify=CENTER, bd=3)
enter_lengthPass.pack()
btnGen = Button(root, height=1, width=15, text='Сгенерировать',  command=gen_password)
btnClean = Button(root, height=1, width=10, text='Очистить', command=clear_all)
btnGen.pack(pady=5, padx=5)
text = Label(text='Ваш пароль:', font='35')
text.pack()
result = Text(root, font='50', fg='red', height='1', width=15, bd='3')
result.tag_config(CENTER, justify=CENTER)
result.tag_add(CENTER, 1.0, END)
result.pack()
btnClean.pack(padx=3)

root.mainloop()
