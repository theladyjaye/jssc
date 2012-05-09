import io
from jssc.environment import env
from .base_node import BaseNode
from .import_node import ImportNode
from .define_node import DefineNode

class FileNode(BaseNode):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path

    def __call__(self):
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
            
            # we actually need the define's first
            # and the imports second
            # someone may want to ifdef an import
            # based on a define
            for token in lexer:
                print token
                if token.type == 'IMPORT':
                    import_node = ImportNode(lexer)
                    file_node = FileNode(str(import_node))
                    file_node()
                elif token.type == 'DEFINE':
                    DefineNode(lexer)
                else:
                    env['tokens'].append(token)

                #     if debug_info and token.lineno % debug_info_every == 1:
                #         out.write(u"/* [jssc] {} @ line {} */\n".format(self.path, token.lineno))
                
                # if token.type == "IMPORT":
                #     out.write(u"{}\n".format(token.value))

        except IOError as e:
            raise e
