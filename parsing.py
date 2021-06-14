#-*-coding: utf-8 -*-
import findX, printer, parsing, helpFunction

def analyze(char):
    numz = "0123456789"
    sign = "^+-=/*"
    priory = "()"
    x = 'хХxX'
    if char in numz:
        return 1
    elif char in sign:
        return 2
    elif char in priory:
        return 3
    elif char in x:
        return 4
    elif char == ',' or char == '.':
        return 5
    else:
        printer.printErr(Parsing, 1)




class Parsing:
    all = ""
    answer = ''
    x_place=[]
    descr = 0
    degree = 0
    a = 0
    b = 0
    c = 0
    redused = ""
    x1 = 0
    x2 = 0
    flags = 111
    left = ""
    right = ""
    expNum = 0

    def parsingFlag(argv, exp):
        i = 1
        numz = '0123456789xX'
        while i < len(argv):
            s = argv[i]
            if len(s) >= 2 and s[0] == '-' and exp.flags != 222:
                b = 0
                if s[b] == '-' and s[b + 1] == '-':
                    if s == '--color' and exp.flags // 100 == 1:
                        exp.flags += 100
                    elif s == '--ru' and exp.flags // 10 % 10 == 1:
                        exp.flags += 10
                    elif s == '--full' and exp.flags % 10 == 1:
                        exp.flags += 1
                    else:
                        printer.printErr(Parsing, 2)
                elif s[b] == '-' and (s[b + 1] == 'c' or s[b + 1] == 'r'
                                        or s[b + 1] == 'f'):
                    if s == '-c' and exp.flags // 100 == 1:
                        exp.flags += 100
                    elif s == '-r' and exp.flags // 10 % 10 == 1:
                        Parsing.flags += 10
                    elif s == '-f' and exp.flags % 10 == 1:
                        exp.flags += 1
                    else:
                        go = 1
                        if (len(s) >= 2):
                            while go < len(s):
                                if s[go] == 'c' and exp.flags // 100 == 1:
                                    exp.flags += 100
                                elif s[go] == 'r' and exp.flags // 10 % 10 == 1:
                                    exp.flags += 10
                                elif s[go] == 'f' and exp.flags % 10 == 1:
                                    exp.flags += 1
                                else:
                                    printer.printErr(exp, 2)
                                go += 1
                elif len(s) > 2 and s[0] == '-' and s[1] in numz:
                    Parsing.expNum = i
            elif Parsing.expNum == 0:
                Parsing.expNum = i
            else:
                printer.printErr(Parsing, 2)
            i += 1
        return exp

    def redusedCheck(argv):
        read = argv[Parsing.expNum]
        if Parsing.expNum != 0:
            Parsing.check_exp(read)

    def get_reduced(exp):
        exp = findX.findDegree(exp)
        d = exp.degree
        if exp.left == 'x' and not 'x' in exp.right:
            printer.printInfo(exp, 2)
            res = helpFunction.calc(exp.right)
            printer.printFull(exp, "x=" + str(res), 2)
        elif exp.right == 'x' and not 'x' in exp.left:
            printer.printInfo(exp, 2)
            res = helpFunction.calc(exp.left)
            printer.printFull(exp, "x=" + str(res), 2)
        elif exp.left == exp.right:
            exp.all = '1=1'
            printer.printInfo(exp, 3)
            printer.printInfo(exp, 4)
        elif d <= 0 and not 'x' in exp.all:
            exp = findX.NoX(exp)
        elif d == 1 or d <= 0:
            exp = findX.OneX(exp)
        elif d == 2:
            exp = findX.TwoX(exp)
        else:
            printer.printErr(Parsing, 3)
        return exp

    def check_exp(strin):
        numz = '0123456789'
        signz = '^+-=/*'
        i = 0
        one_sign = 0
        priory = 0
        is_x = 0
        is_left = 1
        flott = 0
        place = -1
        un = []
        end = 0
        prev = ''
        buf = []
        strin = strin.replace(" ", "")
        if not '=' in strin:
            printer.printErr(parsing.Parsing, 2)
        max_degree = -1
        while i < len(strin):
            test = analyze(strin[i])
            if (test == 1 or test == 4) and prev != 'x':
                one_sign = 0
            elif (test == 1 or test == 4) and prev == 'x':
                printer.printErr(Parsing, 2)
            elif test == 5 and flott == 0:
                flott = 1
            elif test == 5:
                printer.printErr(Parsing, 2)
            elif test == 2 and one_sign == 0 and prev != ',' and prev != '.':
                one_sign += 1
                flott = 0
            elif test == 2:
                printer.printErr(Parsing, 4)
            elif test == 3 and strin[i] == '(' and priory >= 0:
                printer.printErr(Parsing, 5)
                priory += 1
            elif test == 3 and strin[i] == ')' and priory >= 0 and prev != '(':
                printer.printErr(Parsing, 5)
                priory -= 1
            elif test == 3 or test == 0:
                printer.printErr(Parsing, 2)
            if test == 4 and strin[i] != 'x':
                buf.append('x')
            else:
                buf.append(strin[i])
            if prev != '' and test == 4 and (prev == 'x' or prev in numz):
                printer.printErr(Parsing, 2)
            if strin[i] == '=' and is_left == 1:
                if prev != '=' and prev != ',' and prev != '.' and prev != '(' and i+1 != len(strin)\
                        and priory == 0:
                    one_sign = 0
                    is_left = 0
                    flott = 0
                    Parsing.left = strin[0:i]
                    Parsing.right = strin[i+1:]
                else:
                    printer.printErr(Parsing, 2)
            if prev == '^' and strin[i] == 'x':
                printer.printErr(Parsing, 6)
            if is_x == 1 and prev == '^':
                a = int(strin[i])
                if a > max_degree:
                    max_degree = a
                s = str(place) + '~'
                if test == 1 and 0 <= a < 3 and place >= 0:
                    if i + 1 == len(strin):
                        end = 1
                    if end == 0 and analyze(strin[i + 1]):
                        buffer = s + str(a) + "~" + str(is_left)
                        un.append(buffer)
                        is_x = 0
                        place = -1
                    elif end == 1:
                        buffer = s + str(a) + "~" + str(is_left)
                        un.append(buffer)
                        is_x = 0
                        place = -1
            if strin[i] == '^' and (prev == 'x' or prev == 'X'):
                is_x = 1
                place = i - 1
            prev = strin[i]
            i += 1
        if max_degree > 2:
            printer.printErr(Parsing, 3)
        if priory != 0:
            printer.printErr(Parsing, 7)
        Parsing.all = str(buf).replace('\'', '').replace('[', '').replace(']', '').replace(',', '').replace(' ', '')
        if Parsing.all[len(Parsing.all) - 1] in signz:
            printer.printErr(Parsing, 2)
        Parsing.left = Parsing.all[0:Parsing.all.index('=')]
        Parsing.right = Parsing.all[Parsing.all.index('=')+1:]
        if len(Parsing.left) == 0 or len(Parsing.right) == 0 or len(Parsing.all) == 0:
            printer.printErr(Parsing, 2)
        Parsing.x_place = un
        Parsing.degree = max_degree
        if Parsing.flags%10 == 2:
            printer.printFull(Parsing, Parsing.all, 1)