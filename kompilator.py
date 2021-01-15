import sys

from compiler.codegenerator import CodeGenerator
from compiler.lexer import CompLexer
from compiler.parser import CompParser


def read_data(f_name):
    with open(f_name, "r") as file:
        return file.read()


def write_code(f_name, data):
    with open(f_name, "w") as file:
        file.write(data)


if __name__ == '__main__':
    filename = sys.argv[1]
    outFile = sys.argv[2]
    data = read_data(filename)
    lexer = CompLexer()
    parser = CompParser()
    # for tok in lexer.tokenize(data):
    #     print('type=%r, value=%r, line=%r' % (tok.type, tok.value, tok.lineno))
    program = parser.parse(lexer.tokenize(data))
    CG = CodeGenerator(program)
    output = CG.get_code()
    write_code(outFile, output)
