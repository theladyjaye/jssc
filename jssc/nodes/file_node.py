import io
from jssc.environment import env
from .base_node import BaseNode
from .import_node import ImportNode

class FileNode(BaseNode):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path

    def __call__(self, out):
        path = self.path
        
        if path in env['files']:
            return

        lexer = env['lexer'].clone()

        try:
            with io.open(path) as f:
                env['files'].append(path)
                lexer.input(f.read().encode('utf-8'))
            
            debug_info = env["debug_info"]
            debug_info_every = env["debug_info_every"]
            
            for token in lexer:
                if token.type == 'IMPORT':
                    import_node = ImportNode(lexer)
                    file_node = FileNode(str(import_node))
                    file_node(out)
                elif token.type == 'CODE':
                    if debug_info and token.lineno % debug_info_every == 1:
                        out.write(u"/* [jssc] {} @ line {} */\n".format(self.path, token.lineno))
                
                if token.type != "IMPORT":
                    out.write(u"{}\n".format(token.value))

        except IOError as e:
            raise e
