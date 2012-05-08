import sys
import os
import argparse
from .environment import env
from .parsers import JavaScriptParser

def get_args():
    a_parser = argparse.ArgumentParser(description='JSSC Command Line Options')
    a_parser.add_argument('input', metavar='input', type=str,
                   help='Path to target file')

    a_parser.add_argument('output', metavar='output', type=str, nargs="?",
                   help='Path to output file')

    a_parser.add_argument("-q", "--quiet", action="store_true", help='Supress any output messages')
    a_parser.add_argument('-g', '--debug-info', help='Enable debug info in output', action="store_true")
    a_parser.add_argument('--debug-info-every', default=10, type=int,
                   help='If debug info is enable, you can set to display it after N lines. The default is 10')
    
    return a_parser.parse_args()

def main():
    args = get_args()
    
    input = args.input
    output = args.output

    env["debug_info"] = args.debug_info
    env["debug_info_every"] = args.debug_info_every
    env['quiet'] = args.quiet

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