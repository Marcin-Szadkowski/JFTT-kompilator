from sly import Lexer


class CompLexer(Lexer):
    # Set of token names.   This is always required
    literals = { '(', ')', ';', ':', ','}

    tokens = { PIDENTIFIER, NUMBER, PLUS, MINUS, TIMES,
               DIVIDE, ASSIGN,
               DECLARE, BEGIN, END, IF, THEN,
               ELSE, ENDIF, WHILE, DO, ENDWHILE,
               REPEAT, UNTIL, FOR, FROM, TO, DOWNTO,
               ENDFOR, READ, WRITE, MOD, EQ,
               NEQ, LE, GE, LEQ, GEQ }

    # String containing ignored characters between tokens
    ignore = ' \t'
    ignore_comment = r'\[([^\]]*)\]'
    # ignore_newline = r'\n+'
    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')
    # Regular expression rules for tokens

    PIDENTIFIER = r'[_a-z]+'
    NUMBER = r'[0-9]+'
    DECLARE = r'DECLARE'
    BEGIN = r'BEGIN'
    ENDWHILE = r'ENDWHILE'
    ENDFOR = r'ENDFOR'
    ENDIF = r'ENDIF'
    END = r'END'
    IF = r'IF'
    THEN = r'THEN'
    ELSE = r'ELSE'
    WHILE = r'WHILE'
    DOWNTO = r'DOWNTO'
    DO = r'DO'
    REPEAT = r'REPEAT'
    UNTIL = r'UNTIL'
    FOR = r'FOR'
    FROM = r'FROM'
    TO = r'TO'
    READ = r'READ'
    WRITE = r'WRITE'

    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    MOD = r'%'

    ASSIGN = r':='

    EQ = r'='
    NEQ = r'!='
    LEQ = r'<='
    GEQ = r'>='
    LE = r'<'
    GE = r'>'

    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
        return t
