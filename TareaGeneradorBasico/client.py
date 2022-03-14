from antlr4 import *
from marzo.marzoParser import marzoParser
from marzo.marzoLexer import marzoLexer
from listeners.gencode import GenCode

import sys
import os




def main():
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, 'input.txt')
    parser = marzoParser(CommonTokenStream(marzoLexer(FileStream(filename))))
    tree = parser.program()

    gencode = GenCode()
    walker = ParseTreeWalker()
    walker.walk(gencode, tree)


if __name__ == '__main__':
    main()