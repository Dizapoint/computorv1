#-*-coding: utf-8 -*-
import printer, parsing

def is_integer(read):
    i = 0
    numz = '0123456789'
    while i < len(read):
        if i == 0 and (read[i] == '-' or read[i] == '+'):
            i += 1
            continue
        elif not read[i] in numz:
            return False
        i+=1
    return True

def calc(read):
    degree = '^'
    multiply = '*'
    devision = '/'
    add = '+'
    subtract = '-'
    if is_integer(read):
        return float(read)
    while degree in read:
        k = read.index('^')
        read = rewrite(k, read, 1)
    while multiply in read or devision in read:
        k = 1000000
        m = 1000000
        if multiply in read:
            k = read.index('*')
        if devision in read:
            m = read.index('/')
        if k < m and k != 1000000:
            read = rewrite(k, read, 2)
            k = 1000000
        elif m != 1000000:
            read = rewrite(m, read, 3)
            m = 1000000
    while add in read or subtract in read:
        k = 1000000
        m = 1000000
        if add in read:
            k = read.index('+')
        if subtract in read:
            if read.index('-') != 0:
                m = read.index('-')
            elif read.index('-') == 0:
                test = 1
                find = 0
                while test < len(read):
                    if read[test] == "^" or read[test] == "*" or read[test] == "/" \
                            or read[test] == "+" or read[test] == "-":
                        find += 1
                        m = test
                    test += 1
                if find == 0:
                    return float(read)
        if k < m and k != 1000000:
            read = rewrite(k, read, 4)
            k = 1000000
        elif m != 1000000:
            read = rewrite(m, read, 5)
            m = 1000000
    return float(read)

def reverse(read):
    a = len(read) - 1
    result = ''
    while a >= 0:
        result += read[a]
        a -= 1
    return result

def rewrite(ind, read, flag):
    result = ''
    answer = 0
    numz = '0123456789.,-'
    buf1 = ''
    buf = ''
    point = 0
    i = ind
    l = 0
    while i > 0:
        if read[i - 1] in numz:
            if i-1 != 0 and read[i - 1] == '-':
                break
            if point == 1 and (read[i - 1] == '.' or read[i - 1] == ','):
                printer.printErr(parsing.Parsing, 8)
            buf += read[i - 1]
            l += 1
            i -= 1
            if read[i] == '.' or read[i] == ',':
                point += 1
        else:
            break
    point = 0
    i = ind
    while i + 1 < len(read):
        test = read[i + 1]
        if test in numz:
            if test == '-':
                break
            buf1 += test
            i += 1
        else:
            break
    if l > 1:
        buf = reverse(buf)
    if len(buf) == 0:
        buf = '0'
    if len(buf1) == 0:
        buf = '0'
    a = float(buf)
    b = float(buf1)
    if flag == 1:
        if b >= 0 and not '.' in buf1 and not ',' in buf1:
            answer = a**b
        else:
            printer.printErr(parsing.Parsing, 2)
    if flag == 3:
        if b != 0:
            answer = a / b
        else:
            printer.printErr(parsing.Parsing, 2)
    if flag == 2:
        answer = a * b
    if flag == 4:
        answer = a + b
    if flag == 5:
        answer = a - b
    length = len(buf1) + len(buf) + 1
    start = ind - len(buf)
    end = start + length
    if length < len(read):
        i = 0
        while i < len(read):
            if i == start:
                result += str(answer)
                i = end
            else:
                result += read[i]
                i += 1
    else:
        result = str(answer)
    return  result

def findNum(ind, flag, read, is_index):
    numz = '0123456789.,-xX'
    buf1 = ''
    buf = ''
    point = 0
    i = ind
    l = 0
    place = 0
    if flag == 1:
        while i > 0:
            if read[i - 1] in numz:
                if i != 0 and read[i - 1] == '-':
                    break
                if point == 1 and (read[i - 1] == '.' or read[i - 1] == '.'):
                    printer.printErr(parsing.Parsing, 8)
                buf += read[i - 1]
                l += 1
                i -= 1
                place = i
                if read[i - 1] == '.' or read[i - 1] == '.':
                 point += 1
            else:
             break
        if l > 1:
            buf = reverse(buf)
        if (is_index != 1):
            return buf
        else:
            return place
    else:
     while i + 1 < len(read):
            test = read[i + 1]
            if test in numz:
                if test == '.' or test == '.':
                    printer.printErr(parsing.Parsing, 2)
                elif test == '-':
                 break
                buf1 += test
                i += 1
                place = i
            else:
                break
    if (is_index != 1):
        return buf1
    else:
        return place

def redused(exp):
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
    #слева должны остаться все выражения с x
    if not 'x' in exp.left and not 'X' in exp.left:
        right = float(calc(exp.left)) * (-1)
    else:
        while 'x' in exp.left:
            place = exp.left.index('x')
            if place != 0 and exp.left[place - 1] in priory:
                go_start = place - 2
                if go_start < 0:
                    printer.printErr(parsing.Parsing, 2)
                while go_start >= 0 and (exp.left[go_start] in numz or exp.left[go_start] in priory):
                    one += exp.left[go_start]
                    go_start -= 1
                if go_start >= 0 and exp.left[go_start] == '-':
                    one += exp.left[go_start]
                one = reverse(one)
                if count > 0 and exp.left[go_start] != '-':
                    buffer += '+'
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
                    printer.printErr(parsing.Parsing, 2)
                while go_end < len(exp.left) and (exp.left[go_end] in numz or exp.left[go_end] in priory):
                    two += exp.left[go_end]
                    go_end += 1
                buffer += exp.left[place - 1] + two
                if go_end < len(exp.left):
                    left+= exp.left[go_end:]
            else:
                if place != 0 and exp.left[place - 1] in priory:
                    buffer += exp.left[place - 1] + exp.left[place]
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
        if exp.left[0] == '-':
            exp.left = exp.left[1:len(exp.left)]
        if exp.left[0] == '+':
            exp.left = '-' + exp.left[1:len(exp.left)]
        if exp.left[len(exp.left) - 1] == '/':
            exp.left = exp.left[0:len(exp.left) - 1]
            deliver = 1
            right = -1 * calc(exp.left)
        elif exp.left[0] == '/':
            exp.left = exp.left[1:len(exp.left)]
            deliver = 2
            right = -1 * calc(exp.left)
        else:
            right = calc(exp.left)
        exp.left = buffer
    if not 'x' in exp.right:
        if deliver == 0:
          if (exp.right[0] != '-'):
              exp.right = str(calc(str(right) + '+' + exp.right))
          else:
               exp.right = str(calc(str(right) + exp.right))
        elif deliver == 1:
                exp.right = str(calc(str(right) + '/' + exp.right) * -1)
        elif deliver == 2:
            exp.right = str(calc(exp.right + '/' + str(right)) * -1)
    else:
        if 'x' in exp.right and len(exp.right) == 1:
            buffer += '-x'
            exp.right = '0'
        while 'x' in exp.right:
            place = exp.right.index('x')
            if place != 0 and exp.right[place - 1] in priory:
                go_start = place - 2
                if go_start < 0:
                    printer.printErr(parsing.Parsing, 2)
                while go_start >= 0 and (exp.right[go_start] in numz or exp.right[go_start] in priory):
                    one += exp.right[go_start]
                    go_start -= 1
                if place == 0 or (place > 0 and exp.right[place - 1] != '-'):
                    one += '-'
                one = reverse(one)
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
                    right_buf = exp.right[0:place-1]
                buffer += one
            if place + 1 < len(exp.right) and exp.right[place + 1] in priory:
                go_end = place + 2
                buffer += exp.right[place + 1] + 'x' #test
                if go_end >= len(exp.right):
                    printer.printErr(parsing.Parsing, 2)
                while go_end < len(exp.right) and (exp.right[go_end] in numz or exp.right[go_end] in priory):
                    two += exp.right[go_end]
                    go_end += 1
                buffer += exp.right[place - 1] + two
                if go_end < len(exp.right):
                    right_buf += exp.right[go_end:]
            else:
                if place != 0 and exp.right[place - 1] in priory:
                    buffer += exp.right[place - 1] + exp.right[place]
                go_end = place
                if place + 1 != len(exp.right):
                    right_buf += exp.right[place + 1:]
            exp.right = right_buf
            right_buf = ''
            two = ''
            one = ''
            if exp.right[0] != '-' and not 'x' in exp.right and deliver == 0:
                exp.right = str(calc(str(right) + '+' + exp.right))
            elif not 'x' in exp.right and deliver == 0:
                exp.right = str(calc(str(right) + exp.right))
            elif not 'x' in exp.right and deliver == 1:
                exp.right = str(calc(str(right) + '/' + exp.right) * -1)
            elif not 'x' in exp.right and deliver == 2:
                exp.right = str(calc(exp.right + '/' + str(right)) * -1)
        exp.left = buffer
    # вправо переносим все числовые выражения
    return exp

def oneXcalc(exp):
    if not 'x' in exp.left:
        exp.left = str(calc(exp.left))
        exp.all = exp.left + '=' + exp.right
    if not 'x' in exp.right:
        exp.right = str(calc(exp.right))
        exp.all = exp.left + '=' + exp.right
    exp = redused(exp)
    exp.all = exp.left + '=' + exp.right
    return exp

