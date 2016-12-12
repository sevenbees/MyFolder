def add():
        var = a + b
        return

def diff():
        print'(a - b)'
        return

def dadd():
        a * b
        return

def dindd():
        a / b
    #print(d + str(a / b) + '\n')
        return


while True:


    i = input('Посчитаем?(Д/Н)\n')

    if i == 'н' or i == 'Н':
        break

    while True:
        try:
            a = float(input('Введите число a = '))

            b = float(input('Введите число b = '))
            break

        except ValueError:
            print ('\033[0;31mВы ввели некорректное число, попробуйте еще раз!\x1b[0m\n')

    c = input('Введите операцию ')

    d = (str(a) + ' ' + c + ' ' + str(b) + ' ' + ' ' + '=' + ' ')

    if c == '+':
        add()
        print(d + str(add()) + '\n')

    elif c == '-':
        diff()
        print(d + str(diff()) + '\n')

    elif c == '*':
        dadd()
        print(d + str(dadd()) + '\n')

    elif c == '/':
        if b != 0:
            dindd()
            print(d + str(dindd()) + '\n')
        else:
            print('\033[0;31mЧисло на ноль делить нельзя!\x1b[0m\n')
    else:
        print('\033[0;31mВы ввели некорректную операцию!\x1b[0m\n')

