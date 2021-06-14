#-*-coding: utf-8 -*-
import sys, parsing, printer

exp = parsing.Parsing()
if len(sys.argv) >= 2:
    s = sys.argv
    exp = parsing.Parsing.parsingFlag(s, exp)
    parsing.Parsing.redusedCheck(sys.argv)
    exp = parsing.Parsing.get_reduced(exp)
    print(exp.answer)
else:
    printer.printInfo(exp, 1)