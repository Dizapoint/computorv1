#-*-coding: utf-8 -*-
import helpFunction, parsing, findTwoX, printer

def changeSign(read):
    i = 0
    result = ''
    while i < len(read):
        if i == 0 and read[i] == '-':
            i += 1
        elif read[i] == '-':
            result += '+'
            i += 1
        elif read[i] == '+':
            result += '-'
            i += 1
        elif i == 0:
            result += '-'
            result += read[i]
            i += 1
        else:
            result += read[i]
            i += 1
    return result

def getAnswer(left, b):
    i = 0
    oops = 0
    s = ''
    is_sign = 0
    is_x = 0
    count_x = []
    x = 0
    answer = 'x='
    while i < len(left):
        if i == 0 or (left[i] != '+' and left[i] != '-'):
            s += left[i]
            if left[i] == 'x':
                x += 1
        else:
            is_sign += 1
            if 'x' in s:
                is_x += 1
            s = ''
            if len(count_x) > 1:
                oops += 1
            count_x.append(x)
            x = 0
        i += 1
    is_x += 1
    if is_x == is_sign + 1 and oops == 0:
        left = left.replace('x', '1')
        math = helpFunction.calc(left)
        if b != 0 and str(math) != 0:
            math = helpFunction.calc(str(b) + '/' +str(math))
            answer += str(math)
        else:
            answer += '0'
    return answer

def findOneAnswer(exp):
    if exp.flags % 10 == 2:
        printer.printFull(exp, exp.all, 1)
    printer.printInfo(exp, 2)
    if exp.left[0] == '-':
        exp.left = changeSign(exp.left)
        if exp.right != '0':
            exp.right = changeSign(exp.right)
    exp.all = exp.left + '=' + exp.right
    exp.answer = getAnswer(exp.left, float(exp.right))
    return exp

def cleanFunc(exp, char, f):
    places = exp.x_place
    numz = '0123456789'
    read = exp.all
    all = ""
    i = 0
    flag = 0
    if (len(places) > 0):
        ind = 0
        while i < len(read):
            while ind + 1 < len(places) and places[ind][places[ind].index('~') + 1] != str(f):
                ind += 1
            if ind < len(places):
                check = places[ind]
            if 9 >= i == int(check[0]) and ind < len(places) \
                    and not check[1] in numz and check[check.index('~') + 1] == str(f):
                all += char
                i += 3
                ind += 1
            elif i > 9:
                if flag == 0:
                    buff = ''
                    go = 0
                    length = 0
                    while go < len(check):
                        if check[go] in numz:
                            buff += check[go]
                            length += 1
                            go += 1
                        else:
                            break
                    num = int(buff)
                    if i == num and check[check.index('~') + 1] == str(f):
                        all += char
                        i += 3
                        ind += 1
                        flag = 0
                    else:
                        flag += 1
                else:
                    if i == num and check[check.index('~') + 1] == str(f):
                        all += char
                        i += 3
                        ind += 1
                        flag = 0
                    else:
                        all += read[i]
                        i += 1
            else:
                all += read[i]
                i += 1
        exp.all = all
        exp.left = all[0:all.index('=')]
        exp.right = all[all.index('=') + 1:]
    parsing.Parsing.check_exp(exp.all)
    return exp

def count(exp):
    left = exp.left
    right = exp.right
    a = helpFunction.calc(left)
    b = helpFunction.calc(right)
    exp.all = str(a) + '=' + str(b)
    printer.printInfo(exp, 3)
    if a == b:
        printer.printInfo(exp, 4)
    else:
        printer.printInfo(exp, 5)
    return exp

def NoX(exp):
    if (exp.degree != -1):
        count(cleanFunc(exp, '1', 0))
    else:
        exp = count(exp)
    return exp

def OneX(exp):
    exp = cleanFunc(exp, '1', 0)
    exp = cleanFunc(exp, 'x', 1)
    if exp.flags % 10 == 2:
        printer.printFull(exp, exp.all, 1)
    buffer = exp.all
    exp.left = buffer[0:buffer.index('=')]
    exp.right = buffer[buffer.index('=') + 1:]
    if not 'x' in exp.all and exp.left == exp.right:
        printer.printInfo(exp, 4)
        return exp
    elif not 'x'in exp.all :
        left = helpFunction.calc(exp.left)
        right = helpFunction.calc(exp.right)
        if left == right:
            printer.printInfo(exp, 4)
        else:
            printer.printInfo(exp, 5)
        return exp
    exp = helpFunction.oneXcalc(exp)
    exp = findOneAnswer(exp)
    return exp

def TwoX(exp):
    exp = cleanFunc(exp, '1', 0)
    exp = cleanFunc(exp, 'x', 1)
    exp = findTwoX.redusedXtwo(exp)
    printer.printInfo(exp, 3)
    exp = findTwoX.findSolution(exp)
    return exp

def newS(read, degree):
    i = 0
    new = ''
    s = 'x^' + str(degree)
    firstx = 0
    while i < len(read):
        if read[i] == 'x' and firstx == 0 and read[i + 1] == '*':
            new += s
            firstx += 1
            i += 1
            continue
        elif read[i] == 'x':
            i += 1
        elif firstx != 0 and read[i] == '*':
            i += 1
            continue
        if i < len(read):
            new += read[i]
        i += 1
    return new

def findDegree(exp):
    buf = ''
    s = ''
    is_sign = 0
    is_x = 0
    i = 0
    prev = ''
    if 'x' in exp.left:
        while i < len(exp.left):
            if exp.left[i] != '+' and exp.left[i] != '-':
                buf += exp.left[i]
                if exp.left[i] == 'x' and (len(prev) == 0 or prev == '*'):
                    is_x += 1
                elif exp.left[i] == 'x' and prev == '^':
                    printer.printErr(exp, 6)
                prev = exp.left[i]
            else:
                buf += exp.left[i]
                if exp.degree < is_x:
                    exp.degree = is_x
                is_sign += 1
                if is_x > 1:
                    s += newS(buf, is_x)
                else:
                    s += buf
                buf = ''
                is_x = 0
            i += 1
        if is_sign == 0 and is_x > 1:
            if exp.degree < is_x:
                exp.degree = is_x
            s += newS(buf, is_x)
        else:
            s += buf
        exp.left = s
        is_x = 0
        prev = ''
        is_sign = 0
        buf = ''
    if 'x' in exp.right:
        s = ''
        i = 0
        while i < len(exp.right):
            if exp.right[i] != '+' or exp.right[i] != '-':
                buf += exp.right[i]
                if exp.right[i] == 'x' and (len(prev) == 0 or prev == '*'):
                    is_x += 1
                elif exp.right[i] == 'x' and prev == '^':
                    printer.printErr(exp, 6)
                prev = exp.right[i]
            else:
                if exp.degree < is_x:
                    exp.degree = is_x
                is_sign += 1
                if is_x > 1:
                    s += newS(buf, is_x)
                else:
                    s += buf
                buf = ''
                is_x = 0
            i += 1
        if is_sign == 0:
            exp.right = buf
        else:
            exp.right = s
    exp.all = exp.left + '=' + exp.right
    return exp