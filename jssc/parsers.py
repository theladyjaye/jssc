import os
import io
import tempfile
import subprocess
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
        if env['quiet'] == False:
            print("{} -> {}".format(str(self.root), self.output))

        if env['minify']:
            self.compile_minify()
        else:
            self.compile()

    def compile_minify(self):
        out = None
        try:
            out = tempfile.NamedTemporaryFile(delete=False)
            self.root(out)
        except IOError as e:
            print(e)
        finally:
            if out:
                out.close()
                command = env['minify_command'].format(infile=out.name, outfile=self.output)
                try:
                    subprocess.call(command.split(' '))
                except OSError as e:
                    print(e)

                os.unlink(out.name)


    def compile(self):
        out = None
        try:
            out = io.open(self.output, "w")
            self.root(out)
        except IOError as e:
            print(e)
        finally:
            if out:
                out.close()


