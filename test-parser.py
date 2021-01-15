"""
Test odpala parser dla plikow z folderu testy2020
"""
from compiler.parser import CompParser
from compiler.lexer import CompLexer

FOLDER = 'testy2020/'
files = {'0-div-mod.imp', '1-numbers.imp', '2-fib.imp',
         '3-fib-factorial.imp', '4-factorial.imp', '5-tab.imp',
         '6-mod-mult.imp', '7-loopiii.imp', '8-for.imp',
         '9-sort.imp', 'program0.imp', 'program1.imp',
         'program2.imp'}


parser = CompParser()
lexer = CompLexer()
f = open(FOLDER + "program0.imp", "r")
data= f.read()
result = parser.parse(lexer.tokenize(data))
print(result)

# for fname in files:
#     f = open(FOLDER + fname, "r")
#     data= f.read()
#     result = parser.parse(lexer.tokenize(data))
#     print(result)
