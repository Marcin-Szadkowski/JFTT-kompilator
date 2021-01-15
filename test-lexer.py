"""
Test odpala lexer dla plikow z folderu testy2020
i wypisuje powstale bledy w dopasowniu
"""
from compiler.lexer import CompLexer


FOLDER = 'testy2020/'
files = {'0-div-mod.imp', '1-numbers.imp', '2-fib.imp',
         '3-fib-factorial.imp', '4-factorial.imp', '5-tab.imp',
         '6-mod-mult.imp', '7-loopiii.imp', '8-for.imp',
         '9-sort.imp', 'program0.imp', 'program1.imp',
         'program2.imp'}


lexer = CompLexer()
f = open(FOLDER + 'program1.imp', "r")
data = f.read()
for tok in lexer.tokenize(data):
    print(tok)

# for fname in files:
#     f = open(FOLDER + fname, "r")
#     data= f.read()
#     for tok in lexer.tokenize(data):
#         if tok.type == "ERROR":
#             print("File: ", fname)
#             print('type=%r, value=%r \n' % (tok.type, tok.value))
