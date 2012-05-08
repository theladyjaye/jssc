import os
import io
import ply.lex as lex
import rules
from .nodes import FileNode
from .environment import env

class Parser(object):
    def __init__(self, input, output):
        self.output = output if output.startswith('/') else "{}/{}".format(os.getcwd(), output)
        self.input = input if input.startswith('/') else "{}/{}".format(os.getcwd(), input)
        self.root = FileNode(self.input)
        env['base_dir'] = os.path.dirname(self.input)
        env['lexer'] = lex.lex(module=rules)

    def render(self):
        raise NotImplementedError


class JavaScriptParser(Parser):

    def render(self):
        print("{} -> {}".format(str(self.root), self.output))

        try:
            out = io.open(self.output, "w")
            self.root(out)
        except IOError as e:
            print(e)
            out.close()
        finally:
            out.close()


