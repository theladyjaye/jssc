states = (
   ('parsing','exclusive'),
   ('comments', 'exclusive')
)

tokens = (
   'START',
   'IMPORT',
   'DOT',
   'VALUE',
   'CODE',
   'MULTICOMMENT_START',
   'MULTICOMMENT_END',
   'COMMENT',
   'END'
)

t_CODE                = r'[^\n]+'
t_parsing_DOT         = r'\.'
t_parsing_VALUE       = r'[a-zA-Z0-9_-]+'
t_parsing_ignore      = ' \t'
t_comments_COMMENT    = r'[^\n]+'


def t_START(t):
    r'//\s*@'
    t.lexer.begin('parsing')


# defined as a function for ordering purposes
# see http://www.dabeaz.com/ply/ply.html#ply_nn6
# 4.3 Specification of tokens
def t_parsing_IMPORT(t):
    r'import'
    return t

def t_parsing_END(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.lexer.begin('INITIAL')
    return t

def t_parsing_error(t):
    t.lexer.skip(1)

def t_MULTICOMMENT_START(t):
    r'\/\*+'
    t.lexer.begin('comments')
    return t

def t_COMMENT(t):
    r'[ \t]*\/\/[^\n]+'
    return t

def t_comments_MULTICOMMENT_END(t):
    r'\s\*+\/'
    t.lexer.begin('INITIAL')
    return t

def t_comments_error(t):
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    t.lexer.skip(1)