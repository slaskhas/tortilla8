#!/usr/bin/python3

import os
import argparse
from tortilla8.jalapeno import jalapeno

parser = argparse.ArgumentParser(description=
'''
Scan your CHIP-8 source code for pre-processor directives, apply them as
needed, and produce a flattend source file.
Respected Directives:
    'ifdef', 'ifndef', 'elif', 'elseif', 'elifdef',
    'elseifdef', 'endif', 'else', 'equ', '='

No mode modifers ('option', 'align' etc) are currently respected.
''')
parser.add_argument('input', help='File to assemble')
parser.add_argument('-d','--define',nargs='+',help='Strings to define as true for evaluation of pre-processor directives.')
parser.add_argument('-o','--output',help='File to store processed source to, by default INPUT.jala is used.')
opts = parser.parse_args()

if not os.path.isfile(opts.input):
    raise OSError("File '" + opts.input + "' does not exist.")

if not opts.output:
    opts.output  = '.'.join(opts.input.split('.')[0:-1]) if opts.input.find('.') != -1 else opts.input
    opts.output += '.jala'

with open(opts.input) as fh:
    pp = jalapeno(fh, opts.define)

with open(opts.output, 'w+') as fh:
    pp.print_processed_source(fh)
