from jssc.environment import env
from .base_node import BaseNode

class ImportNode(BaseNode):
    def __init__(self, lexer):
        token = lexer.token()
        kind = token.type
        path = ""
        
        while kind != "END":
            if kind == "VALUE":
                path = path + token.value
            elif kind == "DOT":
                path = path + "/"
            candidate = lexer.token()
            if candidate:
                token = candidate
                kind = token.type
            else:
                break;

        self.path = env["base_dir"] + '/' + path + '.jss'

    def __str__(self):
        return self.path

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash(self.path)