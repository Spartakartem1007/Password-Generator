import random
print("Select a language/Выберите язык")
a = input('Eng=2/Рус=1:')
if a == '1':
    while True:
        c = int(input('Напишите количество символов для пароля: '))
        for i in range(c):
            b = [
                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                        '-', '_', '=', '+', '[', ']', '{', '}', '|',
                        ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
                        '`', '~']
            print(random.choice(b),end='')
        print(' Для ввода нового количества символов пароля нажмите Enter', sep=' ')
        input()
if a == '2':
    while True:
        c = int(input('Write the number of characters for the password: '))
        for i in range(c):
            b = [
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                '-', '_', '=', '+', '[', ']', '{', '}', '|',
                ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
                '`', '~']
            print(random.choice(b), end='')
        print(' To enter a new password length, press Enter', sep=' ')
        input()
else:
    print('ERROR')
