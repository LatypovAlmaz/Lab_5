alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456789,.!?;:\'\"-/()[]'
choice = int(input('Выберите режим работы 1 - зашифровать, 2 - расшифровать: '))
def match(text, alphabet=set('abcdefghijklmnopqrstuvwxyz')):
    return not alphabet.isdisjoint(text.lower())
if choice == 1:
    text = input('Введите строку для расшифровки: ')
    while match(text) is False:
        print('Ошибка!!! Попробуйте снова')
        text = input('Введите строку для расшифровки: ')
    step = int(input('Введите шаг сдвига (не больше 26): '))
    while step > 26:
        print('Ошибка!!! Попробуйте заново')
        step = int(input('Введите шаг сдвига (не больше 26): '))
    textf = ''
    for i in text:
        pos = alpha.find(i.lower())  # Приведение символа к нижнему регистру
        npos = pos + step
        if i.isupper():  # Проверка, является ли символ заглавным
            if pos <= 51:
                if i.lower() in alpha:
                    textf = textf + alpha[npos].upper()  # Заглавная буква остается заглавной после шифрования
                else:
                    textf = textf + i
            else:
                textf = textf + alpha[pos].upper()  # Заглавная буква остается заглавной, если символ не находится в алфавите
        else:
            if pos <= 51:
                if i.lower() in alpha:
                    textf = textf + alpha[npos]
                else:
                    textf = textf + i
            else:
                textf = textf + alpha[pos]
    print(textf)
elif choice == 2:
    text = input('Введите строку для расшифровки: ')
    step = int(input('Введите шаг сдвига (не больше 26): '))
    textf = ''
    for i in text:
        pos = alpha.find(i.lower())  # Приведение символа к нижнему регистру
        npos = pos - step
        if i.isupper():  # Проверка, является ли символ заглавным
            if pos <= 51:
                if i.lower() in alpha:
                    textf = textf + alpha[npos].upper()  # Заглавная буква остается заглавной после шифрования
                else:
                    textf = textf + i
            else:
                textf = textf - alpha[
                    pos].upper()  # Заглавная буква остается заглавной, если символ не находится в алфавите
        else:
            if pos <= 51:
                if i.lower() in alpha:
                    textf = textf + alpha[npos]
                else:
                    textf = textf + i
            else:
                textf = textf + alpha[pos]
    print(textf)