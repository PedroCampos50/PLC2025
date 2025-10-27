import ply.lex as lex

tokens = ('SUM', 'SUB', 'MUL', 'DIV', 'PA', 'PF', 'INT')

t_SUM = r'\+'
t_SUB = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'
t_PA = r'\('
t_PF = r'\)'

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print('Caracter desconhecido: ', t.value[0], 'Linha: ', t.lexer.lineno)
    t.lexer.skip(1)

lexer = lex.lex()