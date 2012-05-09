from jssc.environment import env
from .base_node import BaseNode

class DefineNode(BaseNode):
    
    def __init__(self, lexer):
        key = lexer.token().value
        value = lexer.token().value

        # TODO think of a better way to handle this
        # type transform
        # int, bool, str
        try:
            value = int(value)
        except ValueError:
            pass

        try:
            value = True if value.lower() == "true" else value
        except AttributeError:
            # if the int cast above worked, .lower won't exist on value 
            pass

        try:
            value = False if value.lower() == "false" else value
        except AttributeError:
            # if the int or bool cast above worked, .lower won't exist on value 
            pass


        env['define'][key] = value

    def __str__(self):
        return self.value