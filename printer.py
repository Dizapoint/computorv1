#-*-coding: utf-8 -*-

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def printErr(exp, flag):
    color = exp.flags // 100
    ru = exp.flags // 10 % 10
    if ru == 2:
        printRuErr(exp, color, flag)
    else:
        if color == 2:
            print(bcolors.FAIL)
        if flag == 1:
            print("Error: wrong expression")
        elif flag == 2:
            print("Wrong input")
        elif flag == 3:
            print("The polynomial degree is srictly greater than 2, I can`t solve")
        elif flag == 4:
            print("Error: Double sign")
        elif flag == 5:
            print("Error: I don't work with parentheses.")
        elif flag == 6:
            print("I can not solve expression with \'^x\'. Sorry!")
        elif flag == 7:
            print("Wrong parentheses.")
        elif flag == 8:
            print("Error: Double point")
        if color == 2:
            print(bcolors.ENDC)
    exit(flag)

def printInfo(exp, flag):
    color = exp.flags // 100
    ru = exp.flags // 10 % 10
    if ru == 2:
        printInfoRu(exp, color, flag)
    else:
        if color == 2:
            print(bcolors.WARNING)
        if flag == 1:
            print("Usage: python3 computor.py <math expression> [-c|--color|-r|--ru|-f|--full]")
        elif flag == 2:
            print('There is one solution.')
        elif flag == 3:
            print('Reduced form:\n' + exp.all)
        elif flag == 4:
            print("All real numbers are solutions to the equation")
        elif flag == 5:
            print("Equality is impossible. There are no solutions.")
        elif flag == 6:
            print("Discriminant is strictly positive, the two solutions are: ")
        elif flag == 7:
            print("D = 0; The solution is: ")
        elif flag == 8:
            print("D < 0; There is no solution.")
        elif flag == 9:
            print("There are two solution:")
        if color == 2:
            print(bcolors.ENDC)

def printFull(exp, s, flag):
    color = exp.flags // 100
    ru = exp.flags // 10 % 10
    if ru == 2:
        printFullRu(exp, color, flag, s)
    else:
        if color == 2:
            print(bcolors.OKGREEN)
        if flag == 1:
            print("Expression is: " + s)
        elif flag == 2:
            print(s)
        if color == 2:
            print(bcolors.ENDC)

def printInfoRu(exp, color, flag):
    if color == 2:
        print(bcolors.WARNING)
    if flag == 1:
        print("Использование: python3 computor.py <math expression> [-c|--color|-r|--ru|-f|--full]")
    elif flag == 2:
        print('В заданном выражении один корень.')
    elif flag == 3:
        print('Сокращенная форма:\n' + exp.all)
    elif flag == 4:
        print("Все действительные числа являются решением.")
    elif flag == 5:
        print("Равенство невозможно. Решений нет.")
    elif flag == 6:
        print("Дискриминант положительный. Два корня:")
    elif flag == 7:
        print("D = 0; Один корень: ")
    elif flag == 8:
        print("D < 0; Решений нет.")
    elif flag == 9:
        print("Два корня:")
    if color == 2:
        print(bcolors.ENDC)

def printRuErr(exp, color, flag):
    if color == 2:
        print(bcolors.FAIL)
    color = exp.flags // 100
    if flag == 1:
        print("Ошибка: неверное выражение")
    elif flag == 2:
        print("Ошибка при вводе")
    elif flag == 3:
        print("Степень полинома выше, чем 2. Выражение не поддерживается")
    elif flag == 4:
        print("Ошибка: двойной знак")
    elif flag == 5:
        print("Ошибка: работа со скробками не поддерживается")
    elif flag == 6:
        print("Ошибка работа со степенью \'^x\' не поддерживается")
    elif flag == 7:
        print("Неправильно расставлены скобки.")
    if color == 2:
        print(bcolors.ENDC)

def printFullRu(exp, color, flag, s):
    if color == 2:
        print(bcolors.OKBLUE)
    if flag == 1:
        print("Выражение: " + s)
    elif flag == 2:
        print(s)
    if color == 2:
        print(bcolors.ENDC)