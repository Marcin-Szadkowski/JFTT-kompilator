from sly import Parser

from AST.commands.assign import Assign
from AST.commands.for_from_downto import ForFromDownto
from AST.commands.for_from_to import ForFromTo
from AST.commands.if_then import IfThen
from AST.commands.if_then_else import IfThenElse
from AST.commands.read import Read
from AST.commands.write import Write
from AST.commands.repeat_until import RepeatUntil
from AST.commands.while_do import WhileDo
from AST.conditions.cond_eq import CondEQ
from AST.conditions.cond_ge import CondGE
from AST.conditions.cond_geq import CondGEQ
from AST.conditions.cond_le import CondLE
from AST.conditions.cond_leq import CondLEQ
from AST.conditions.cond_neq import CondNEQ
from AST.declarations.array import Array
from AST.expressions.divide_exp import DivideExp
from AST.expressions.minus_exp import MinusExp
from AST.expressions.mod_exp import ModExp
from AST.expressions.plus_exp import PlusExp
from AST.expressions.times_exp import TimesExp
from AST.identifiers.array_number import ArrayNumber
from AST.identifiers.array_pid import ArrayPid
from AST.identifiers.identifier import Identifier
from AST.values.number import Number
from AST.values.value_identifier import ValueIdentifier
from compiler.lexer import CompLexer
from AST.declarations.variable import Variable
from AST.program import Program


class CompParser(Parser):
    # debugfile = 'parser.out'
    tokens = CompLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE, MOD),
    )

    # program
    @_('DECLARE declarations BEGIN commands END')
    def program(self, p):
        return Program(p.commands, p.declarations)

    @_('BEGIN commands END')
    def program(self, p):
        return Program(p.commands)

    # declarations
    @_('declarations "," PIDENTIFIER')
    def declarations(self, p):
        decl = Variable(p.PIDENTIFIER, line=p.lineno)
        return p.declarations + [decl]

    @_('declarations "," PIDENTIFIER "(" NUMBER ":" NUMBER ")"')
    def declarations(self, p):
        decl = Array(p.PIDENTIFIER, p.NUMBER0, p.NUMBER1, line=p.lineno)
        return p.declarations + [decl]

    @_('PIDENTIFIER')
    def declarations(self, p):
        decl = Variable(p.PIDENTIFIER, line=p.lineno)
        return [decl]

    @_('PIDENTIFIER "(" NUMBER ":" NUMBER ")"')
    def declarations(self, p):
        return [Array(p.PIDENTIFIER, p.NUMBER0, p.NUMBER1, line=p.lineno)]

    # commands
    @_('commands command')
    def commands(self, p):
        return p.commands + [p.command]

    @_('command')
    def commands(self, p):
        return [p.command]

    # command
    @_('identifier ASSIGN expression ";"')
    def command(self, p):
        return Assign(p.identifier, p.expression, line=p.lineno)

    @_('IF condition THEN commands ELSE commands ENDIF')
    def command(self, p):
        return IfThenElse(p.condition, p.commands0, p.commands1)

    @_('IF condition THEN commands ENDIF')
    def command(self, p):
        return IfThen(p.condition, p.commands)

    @_('WHILE condition DO commands ENDWHILE')
    def command(self, p):
        return WhileDo(p.condition, p.commands)

    @_('REPEAT commands UNTIL condition ";"')
    def command(self, p):
        return RepeatUntil(p.commands, p.condition)

    @_('FOR PIDENTIFIER FROM value DOWNTO value DO commands ENDFOR')
    def command(self, p):
        return ForFromDownto(p[1], p[3], p[5], p[7])

    @_('FOR PIDENTIFIER FROM value TO value DO commands ENDFOR')
    def command(self, p):
        return ForFromTo(p.PIDENTIFIER, p.value0, p.value1, p.commands, p.lineno)

    @_('READ identifier ";"')
    def command(self, p):
        return Read(p.identifier)

    @_('WRITE value ";"')
    def command(self, p):
        return Write(p.value)

    # expression
    @_('value')
    def expression(self, p):
        return p.value

    @_('value PLUS value')
    def expression(self, p):
        return PlusExp(p.value0, p.PLUS, p.value1)

    @_('value MINUS value')
    def expression(self, p):
        return MinusExp(p.value0, p.MINUS, p.value1)

    @_('value TIMES value')
    def expression(self, p):
        return TimesExp(p.value0, p.TIMES, p.value1)

    @_('value DIVIDE value')
    def expression(self, p):
        return DivideExp(p.value0, p.DIVIDE, p.value1)

    @_('value MOD value')
    def expression(self, p):
        return ModExp(p.value0, p.MOD, p.value1)

    # condition
    @_('value EQ value')
    def condition(self, p):
        return CondEQ(p.value0, p.EQ, p.value1)

    @_('value NEQ value')
    def condition(self, p):
        return CondNEQ(p.value0, p.NEQ, p.value1)

    @_('value LE value')
    def condition(self, p):
        return CondLE(p.value0, p.LE, p.value1)

    @_('value GE value')
    def condition(self, p):
        return CondGE(p.value0, p.GE, p.value1)

    @_('value LEQ value')
    def condition(self, p):
        return CondLEQ(p.value0, p.LEQ, p.value1)

    @_('value GEQ value')
    def condition(self, p):
        return CondGEQ(p.value0, p.GEQ, p.value1)

    # value
    @_('NUMBER')
    def value(self, p):
        return Number(p.NUMBER)

    @_('identifier')
    def value(self, p):
        return ValueIdentifier(p.identifier)

    # identifier
    @_('PIDENTIFIER')
    def identifier(self, p):
        return Identifier(p.PIDENTIFIER, line=p.lineno)

    @_('PIDENTIFIER "(" PIDENTIFIER ")"')
    def identifier(self, p):
        return ArrayPid(p.PIDENTIFIER0, p.PIDENTIFIER1, line=p.lineno)

    @_('PIDENTIFIER "(" NUMBER ")"')
    def identifier(self, p):
        return ArrayNumber(p.PIDENTIFIER, p.NUMBER, line=p.lineno)

    def error(self, p):
        raise Exception(" Błąd w linii {}: nierozpoznany napis {} ".format(p.lineno, p.value))
