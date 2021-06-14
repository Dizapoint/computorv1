#-*-coding: utf-8 -*-
import helpFunction as h, printer

def findClean(left, flag):
    s = ''
    i = 0
    res = ''
    sign = 0
    while i < len(left):
        if left[i] != '+' and left[i] != '-' and i < len(left):
            s += left[i]
        elif i < len(left):
            if not 'x' in s and flag == 0:
                if sign != 0:
                    res += left[i]
                res += s
                sign += 1
            elif flag == 1 and 'x' in s:
                if sign != 0:
                    res += left[i]
                res += s
                sign += 1
            s = ''
        i += 1
    if res[len(res) - 1] == '+' or res[len(res) - 1] == '-':
        res = res[0:len(res) - 1]
    return res

def redusedXtwo(exp):
        numz = '0123456789'
        priory = '*^.,'
        right = ''
        right_buf = ''
        left = ''
        buffer = ''
        one = ''
        two = ''
        count = 0
        deliver = 0
        # слева должны остаться все выражения с x
        if not 'x' in exp.left and not 'X' in exp.left:
            right = float(h.calc(exp.left)) * (-1)
        else:
            while 'x' in exp.left:
                place = exp.left.index('x')
                if place != 0 and exp.left[place - 1] in priory:
                    go_start = place - 2
                    if go_start < 0:
                        printer.printErr(exp, 2)
                    while go_start >= 0 and (exp.left[go_start] in numz or exp.left[go_start] in priory):
                        one += exp.left[go_start]
                        go_start -= 1
                    if go_start >= 0 and exp.left[go_start] == '-':
                        one += exp.left[go_start]
                    one = h.reverse(one)
                    if count > 0 and one[0] != '-':
                        buffer += '+'+ one + exp.left[exp.left.index('x') - 1] + exp.left[exp.left.index('x')]
                    elif count > 0 and one[0] == '-':
                        buffer += one + exp.left[exp.left.index('x') - 1] + exp.left[exp.left.index('x')]
                    elif len(one) != 0:
                        buffer += one + exp.left[exp.left.index('x') - 1] + exp.left[exp.left.index('x')]
                    else:
                        buffer += one
                    if go_start > 0:
                        left = exp.left[0:go_start]
                else:
                    if place > 0 and exp.left[place - 1] == '-':
                        one += exp.left[place - 1]
                    one += 'x'
                    if place != 0:
                        left = exp.left[0:place]
                    buffer += one
                if place + 1 < len(exp.left) and exp.left[place + 1] in priory:
                    go_end = place + 2
                    if go_end >= len(exp.left):
                        printer.printErr(exp, 2)
                    while go_end < len(exp.left) and (exp.left[go_end] in numz or exp.left[go_end] in priory):
                        two += exp.left[go_end]
                        go_end += 1
                    buffer += exp.left[place + 1] + two
                    if go_end < len(exp.left):
                        left += exp.left[go_end:]
                else:
                    go_end = place
                    if place + 1 != len(exp.left):
                        left += exp.left[place + 1:]
                if len(left) == 0:
                    left = '0'
                exp.left = left
                left = ''
                two = ''
                one = ''
                count += 1
            if exp.left[len(exp.left) - 1] == '+' or exp.left[len(exp.left) - 1] == '-':
                exp.left = exp.left[0:len(exp.left) - 1]
            if len(exp.left) != 0 and exp.left[0] == '-':
                exp.left = exp.left[1:len(exp.left)]
            if len(exp.left) != 0 and exp.left[0] == '+':
                exp.left = '-' + exp.left[1:len(exp.left)]
            if len(exp.left) != 0 and exp.left[len(exp.left) - 1] == '/':
                exp.left = exp.left[0:len(exp.left) - 1]
                deliver = 1
            elif len(exp.left) != 0 and exp.left[0] == '/':
                exp.left = exp.left[1:len(exp.left)]
                deliver = 2
            if len(exp.left) != 0 and not 'x' in exp.left:
                right = h.calc(exp.left) * -1
            exp.left = buffer
        if len(exp.right) != 0 and not 'x' in exp.right:
            if deliver == 0:
                if (exp.right[0] != '-'):
                    exp.right = str(h.calc(str(right) + '+' + exp.right))
                else:
                    exp.right = str(h.calc(str(right) + exp.right))
            elif deliver == 1:
                exp.right = str(h.calc(str(right) + '/' + exp.right) * -1)
            elif deliver == 2:
                exp.right = str(h.calc(exp.right + '/' + str(right)) * -1)
        else:
            if len(str(right)) == 0:
                right = '0'
            while 'x' in exp.right:
                place = exp.right.index('x')
                if place != 0 and exp.right[place - 1] in priory:
                    go_start = place - 2
                    if go_start < 0:
                        printer.printErr(exp, 2)
                    while go_start >= 0 and (exp.right[go_start] in numz or exp.right[go_start] in priory):
                        one += exp.right[go_start]
                        go_start -= 1
                    if place == 0 or (place > 0 and exp.right[place - 1] != '-'):
                        one += '-'
                    one = h.reverse(one)
                    if count > 0 and one[0] != '-':
                        buffer += '+' + one + exp.right[exp.right.index('x') - 1] + exp.right[exp.right.index('x')]
                    elif count > 0 and one[0] == '-':
                        buffer += one + exp.right[exp.right.index('x') - 1] + exp.right[exp.right.index('x')]
                    else:
                        buffer += one
                    if go_start > 0:
                        right_buf = exp.right[0:go_start]
                    else:
                        right_buf = '0'
                else:
                    if place == 0 or (place > 0 and exp.right[place - 1] != '-'):
                        one += '-'
                    one += 'x'
                    if place != 0:
                        right_buf = exp.right[0:place - 1]
                    buffer += one
                if place + 1 < len(exp.right) and exp.right[place + 1] in priory:
                    go_end = place + 2
                    buffer += exp.right[place + 1] + 'x'  # test
                    if go_end >= len(exp.right):
                        printer.printErr(exp, 2)
                    while go_end < len(exp.right) and (exp.right[go_end] in numz or exp.right[go_end] in priory):
                        two += exp.right[go_end]
                        go_end += 1
                    buffer += exp.right[place - 1] + two
                    if go_end < len(exp.right):
                        right_buf += exp.right[go_end:]
                else:
                    if place + 1 < len(exp.right) and exp.right[place + 1] in priory:
                        buffer += exp.right[place - 1] + exp.right[place]
                    go_end = place
                    if place + 1 != len(exp.right):
                        right_buf += exp.right[place + 1:]
                exp.right = right_buf
                right_buf = ''
                two = ''
                one = ''
                if exp.right[0] != '-' and not 'x' in exp.right and not 'X' in exp.right and deliver == 0:
                    exp.right = str(h.calc(str(right) + '+' + exp.right))
                elif not 'x' in exp.right and deliver == 0:
                    exp.right = str(h.calc(str(right) + exp.right))
                elif not 'x' in exp.right and deliver == 1:
                    exp.right = str(h.calc(str(right) + '/' + exp.right) * -1)
                elif not 'x' in exp.right and deliver == 2:
                    exp.right = str(h.calc(exp.right + '/' + str(right)) * -1)
            exp.left = buffer
        if exp.right != '0':
            if exp.right[0] == '-':
                exp.all = exp.left + '+' + exp.right[1:len(exp.right)] + '=0'
            else:
                exp.all = exp.left + '-' + exp.right + '=0'
        else:
            exp.all = exp.left + '=' + exp.right
        exp.left = exp.all[0:exp.all.index('=')]
        exp.right = '0'
        return exp

def findSolution(exp):
    numz = '0123456789'
    s = ''
    clean = ''
    a = 0
    b = 0
    c = 0
    d = 0
    is_sign = 0
    buf = ''
    buf1= ''
    buf3 = 0
    i = 0
    while i < len(exp.left):
        if i == 0 or (exp.left[i] != '+' and exp.left[i] != '-'):
            s += exp.left[i]
        else:
            is_sign += 1
            if 'x' not in s:
                clean += s + exp.left[i]
                c = float(s)
            elif '^' in s and s[s.index('^') + 1] == '2':
                if s.index('^')-3 >= 0 and s[s.index('^')-2] == '*' and s[s.index('^')-3] in numz:
                    k = s.index('^')-3
                    while k >= 0:
                        if not s[k] in numz and s[k] != '-':
                            break
                        buf += s[k]
                        k -= 1
                    buf = h.reverse(buf)
                    k = s.index('^') + 2
                    while k < len(s):
                        if not s[k] in numz:
                            break
                        buf1 += s[k]
                        k += 1
                    if len(buf) == 0:
                        buf = '1'
                    if len(buf1) == 0:
                        buf1 = '1'
                        a = float(buf) * float(buf1)
                else:
                    a = 1
                clean += s + exp.left[i]
            elif 'x' in s:
                if s.index('x') - 2 >= 0 and s[s.index('x') - 1] == '*' and s[s.index('x') - 2] in numz:
                    k = s.index('x') - 2
                    while k >= 0:
                        if not s[k] in numz and s[k] != '-':
                            break
                        buf += s[k]
                        k -= 1
                    if len(clean) != 0 and clean[len(clean)-1] == '-':
                        buf += '-'
                    buf = h.reverse(buf)
                    k = s.index('x') + 2
                    while k < len(s):
                        if not s[k] in numz:
                            break
                        buf1 += s[k]
                        k += 1
                    if len(buf) == 0:
                        buf = '1'
                    if len(buf1) == 0:
                        buf1 = '1'
                    if float(buf) != 0 and float(buf1) != '0':
                        b += float(buf) * float(buf1)
                        # a += buf
                        # buf == 0
                        clean += s + exp.left[i]
                    else:
                        clean = clean[0:len(clean) - 1] + exp.left[i]
                else:
                    b = 1
                    clean += s + exp.left[i]
            s = ''
            buf = ''
            buf1 = ''
        i += 1
    if 'x' not in s:
        clean += s
        c = float(s)
    elif '^' in s and s[s.index('^') + 1] == 2:
        if s.index('^') - 3 >= 0 and s[s.index('^') - 2] == '*' and s[s.index('^') - 3] in numz:
            k = s.index('^') - 3
            while k >= 0:
                if not s[k] in numz and s[k] != '-':
                    break
                buf += s[k]
                k -= 1
            buf = h.reverse(buf)
            k = s.index('^') + 2
            while k < len(s):
                if not s[k] in numz:
                    break
                buf1 += s[k]
                k += 1
            if len(buf) == 0:
                buf = '1'
            if len(buf1) == 0:
                buf1 = '1'
                a = float(buf) * float(buf1)
        else:
            a = 1
        clean += s
    elif 'x' in s:
        if s.index('x') - 2 >= 0 and s[s.index('x') - 1] == '*' and s[s.index('x') - 2] in numz:
            k = s.index('x') - 2
            while k >= 0:
                if not s[k] in numz and s[k] != '-':
                    break
                buf += s[k]
                k -= 1
            if len(clean) != 0 and clean[len(clean) - 1] == '-':
                buf += '-'
            buf = h.reverse(buf)
            k = s.index('x') + 2
            while k < len(s):
                if not s[k] in numz:
                    break
                buf1 += s[k]
                k += 1
            if len(buf) == 0:
                buf = '1'
            if len(buf1) == 0:
                buf1 = '1'
                if float(buf) != 0 and float(buf1) != 0:
                    b += float(buf) * float(buf1)
                    clean += s
        else:
            b = 1
            clean += s
    if b != 0:
        d = b ** 2 - 4 * a * c
        exp.left = clean
        exp.all = exp.left + '=' + exp.right
        if exp.flags % 10 == 2:
            printer.printFull(exp, "a=" + str(a), 2)
            printer.printFull(exp, "b=" + str(a), 2)
            printer.printFull(exp, "c=" + str(a), 2)
            printer.printFull(exp, "Discriminant=" + str(d), 2)
            printer.printFull(exp, exp.all, 1)
        if d > 0:
            printer.printInfo(exp, 6)
            x1 = (-b + d**0.5) / (2 * a)
            x2 = (-b - d**0.5) / (2 * a)
            print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        elif d == 0:
            printer.printInfo(exp, 7)
            x = -b / (2 * a)
            print("x = %.2f" % x)
        else:
            printer.printInfo(exp, 8)
    else:
        s = exp.all
        s = s.replace("^2", '')
        exp.all = s
        exp.left = s[0:s.index('=')]
        exp.right = s[s.index('=') + 1:]
        if exp.flags % 10 == 2:
            printer.printFull(exp, exp.all, 1)
        answer = findAnswers(exp, a)
        x1 = float(answer)
        if x1 != 0:
            printer.printInfo(exp, 9)
            x2 = answer * -1
            print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        else:
            print("There is one solution: ")
            print("x1 = %.2f" % (x1))
    return exp

def findAnswers(exp, a):
    i = 0
    left = ''
    s = ''
    while i < len(exp.left):
        if i == 0 or (exp.left[i] != '+' and exp.left[i] != '-'):
            s += exp.left[i]
        else:
            if not 'x' in s:
               left += s + exp.left[i]
            elif i == len(s) and exp.left[i] == '-':
                left += exp.left[i]
            elif i > 0:
                left += exp.left[i]
            s = ''
        i += 1
    if not 'x' in s:
        left += s
    k = h.calc(left)
    if k < 0:
        k *= -1
    squre = k / a
    if exp.flags % 10 == 2:
        printer.printFull(exp, "squre of " + str(squre), 2)
    squre = squre**0.5
    return squre