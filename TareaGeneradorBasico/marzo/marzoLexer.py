# Generated from /Users/aldoponce/8vo/Compiladores/marzo/marzo.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("O\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\6\13>\n\13\r\13\16\13?\3\f")
        buf.write("\3\f\3\r\6\rE\n\r\r\r\16\rF\3\16\6\16J\n\16\r\16\16\16")
        buf.write("K\3\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\3\2\6\3\2\62;\4\2C\\c|\5")
        buf.write("\2\62;C\\c|\5\2\13\f\17\17\"\"\2Q\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37")
        buf.write("\3\2\2\2\7!\3\2\2\2\t#\3\2\2\2\13%\3\2\2\2\r*\3\2\2\2")
        buf.write("\17,\3\2\2\2\21\61\3\2\2\2\23\65\3\2\2\2\25=\3\2\2\2\27")
        buf.write("A\3\2\2\2\31D\3\2\2\2\33I\3\2\2\2\35\36\7-\2\2\36\4\3")
        buf.write("\2\2\2\37 \7?\2\2 \6\3\2\2\2!\"\7>\2\2\"\b\3\2\2\2#$\7")
        buf.write("@\2\2$\n\3\2\2\2%&\7k\2\2&\'\7h\2\2\'(\7\"\2\2()\7*\2")
        buf.write("\2)\f\3\2\2\2*+\7+\2\2+\16\3\2\2\2,-\7g\2\2-.\7n\2\2.")
        buf.write("/\7u\2\2/\60\7g\2\2\60\20\3\2\2\2\61\62\7k\2\2\62\63\7")
        buf.write("p\2\2\63\64\7v\2\2\64\22\3\2\2\2\65\66\7r\2\2\66\67\7")
        buf.write("t\2\2\678\7k\2\289\7p\2\29:\7v\2\2:;\7*\2\2;\24\3\2\2")
        buf.write("\2<>\t\2\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@")
        buf.write("\26\3\2\2\2AB\t\3\2\2B\30\3\2\2\2CE\t\4\2\2DC\3\2\2\2")
        buf.write("EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\32\3\2\2\2HJ\t\5\2\2I")
        buf.write("H\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\b")
        buf.write("\16\2\2N\34\3\2\2\2\6\2?FK\3\b\2\2")
        return buf.getvalue()


class marzoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    Numero = 10
    Letra = 11
    Todo = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'='", "'<'", "'>'", "'if ('", "')'", "'else'", "'int'", 
            "'print('" ]

    symbolicNames = [ "<INVALID>",
            "Numero", "Letra", "Todo", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "Numero", "Letra", "Todo", "WS" ]

    grammarFileName = "marzo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


