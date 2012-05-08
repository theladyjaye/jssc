import sys
import os
import argparse
from .environment import env
from .parsers import JavaScriptParser

def get_args():
    a_parser = argparse.ArgumentParser(description='JSSC Command Line Options')
    a_parser.add_argument('input', metavar='input', type=str, nargs=1,
                   help='target')

    a_parser.add_argument('output', metavar='output', type=str, nargs="?",
                   help='destination')

    a_parser.add_argument('--debug', metavar='debug', type=bool, nargs="?",
                   help='turn on debugging')
    
    return a_parser.parse_args()

def main():
    args = get_args()
    input = args.input[0]
    output = args.output

    if output is None:
        directory = os.path.dirname(input)
        filename  = os.path.basename(input)
        parts = filename.split('.')
        ext_index = len(parts) - 1
        
        if ext_index == 0:
            parts.append('js')
        elif ext_index > 0:
            parts[ext_index] = "js"
        
        filename = ".".join(parts)
        output = "{}/{}".format(directory, filename)

    env['parser'] = JavaScriptParser(input, output)
    env['parser'].render()

if __name__ == '__main__':
    sys.exit(main())