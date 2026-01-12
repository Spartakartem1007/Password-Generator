import random
print("Select a language/Выберите язык")
a = input('Eng=2/Рус=1:')
if a == '1':
    while True:
        c = input('Выберите размер пароля. 12 и 8 символов.')
        if c == '8':
                print('Сейчас для вас будет создан пароль из 8 символов')
                b = [
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                    '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
                    ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
                    '`', '~']
                print(random.choice(b),random.choice(b),random.choice(b),random.choice(b),random.choice(b),random.choice(b),random.choice(b),random.choice(b), sep ="")
                input("Для получения нового пароля нажмите Enter")
        if c == '12':
                print('Сейчас для вас будет создан пароль из 12 символов')
                b = [
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                    '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
                    ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
                    '`', '~']
                print(random.choice(b), random.choice(b), random.choice(b), random.choice(b), random.choice(b),random.choice(b), random.choice(b), random.choice(b),random.choice(b), random.choice(b), random.choice(b), random.choice(b), random.choice(b),random.choice(b), random.choice(b), random.choice(b), sep = "" )
                input("Для получения нового пароля нажмите Enter")
if a == '2':
    while True:
        c = input('Select the password size. 12 and 8 characters.')
        if c == '8':
            print('An 8-character password will be created for you now')
            b = [
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
                ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
                '`', '~']
            print(random.choice(b), random.choice(b), random.choice(b), random.choice(b), random.choice(b),random.choice(b), random.choice(b), random.choice(b), sep="")
            input("To get a new password, press Enter")
        if c == '12':
            print('A 12-character password will be created for you now')
            b = [
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
                ';', ':', "'", '"', ',', '.', '<', '>', '/', '?',
                '`', '~']
            print(random.choice(b), random.choice(b), random.choice(b), random.choice(b), random.choice(b),random.choice(b), random.choice(b), random.choice(b), random.choice(b), random.choice(b),random.choice(b), random.choice(b), random.choice(b), random.choice(b), random.choice(b),random.choice(b), sep="")
            input("To get a new password, press Enter")

else:
    print('ERROR')
