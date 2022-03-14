# Generated from /Users/aldoponce/8vo/Compiladores/marzo/marzo.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("?\4\2\t\2\4\3\t\3\4\4\t\4\3\2\7\2\n\n\2\f\2\16\2\r\13")
        buf.write("\2\3\2\7\2\20\n\2\f\2\16\2\23\13\2\3\3\3\3\3\3\5\3\30")
        buf.write("\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7")
        buf.write("\3&\n\3\f\3\16\3)\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4=\n\4\3\4")
        buf.write("\2\3\4\5\2\4\6\2\2\2E\2\13\3\2\2\2\4\27\3\2\2\2\6<\3\2")
        buf.write("\2\2\b\n\5\4\3\2\t\b\3\2\2\2\n\r\3\2\2\2\13\t\3\2\2\2")
        buf.write("\13\f\3\2\2\2\f\21\3\2\2\2\r\13\3\2\2\2\16\20\5\6\4\2")
        buf.write("\17\16\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2")
        buf.write("\2\22\3\3\2\2\2\23\21\3\2\2\2\24\25\b\3\1\2\25\30\7\f")
        buf.write("\2\2\26\30\7\r\2\2\27\24\3\2\2\2\27\26\3\2\2\2\30\'\3")
        buf.write("\2\2\2\31\32\f\b\2\2\32\33\7\3\2\2\33&\5\4\3\t\34\35\f")
        buf.write("\6\2\2\35\36\7\4\2\2\36&\5\4\3\7\37 \f\4\2\2 !\7\5\2\2")
        buf.write("!&\5\4\3\5\"#\f\3\2\2#$\7\6\2\2$&\5\4\3\4%\31\3\2\2\2")
        buf.write("%\34\3\2\2\2%\37\3\2\2\2%\"\3\2\2\2&)\3\2\2\2\'%\3\2\2")
        buf.write("\2\'(\3\2\2\2(\5\3\2\2\2)\'\3\2\2\2*+\7\7\2\2+,\5\4\3")
        buf.write("\2,-\7\b\2\2-.\5\6\4\2.=\3\2\2\2/\60\7\7\2\2\60\61\5\4")
        buf.write("\3\2\61\62\7\b\2\2\62\63\5\6\4\2\63\64\7\t\2\2\64\65\5")
        buf.write("\6\4\2\65=\3\2\2\2\66\67\7\n\2\2\67=\7\r\2\289\7\13\2")
        buf.write("\29:\5\4\3\2:;\7\b\2\2;=\3\2\2\2<*\3\2\2\2</\3\2\2\2<")
        buf.write("\66\3\2\2\2<8\3\2\2\2=\7\3\2\2\2\b\13\21\27%\'<")
        return buf.getvalue()


class marzoParser ( Parser ):

    grammarFileName = "marzo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'='", "'<'", "'>'", "'if ('", 
                     "')'", "'else'", "'int'", "'print('" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "Numero", "Letra", "Todo", 
                      "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_statement = 2

    ruleNames =  [ "program", "expression", "statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    Numero=10
    Letra=11
    Todo=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.StatementContext)
            else:
                return self.getTypedRuleContext(marzoParser.StatementContext,i)


        def getRuleIndex(self):
            return marzoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = marzoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==marzoParser.Numero or _la==marzoParser.Letra:
                self.state = 6
                self.expression(0)
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << marzoParser.T__4) | (1 << marzoParser.T__7) | (1 << marzoParser.T__8))) != 0):
                self.state = 12
                self.statement()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuma" ):
                listener.enterSuma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuma" ):
                listener.exitSuma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class AsignacionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)


    class MayorContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMayor" ):
                listener.enterMayor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMayor" ):
                listener.exitMayor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMayor" ):
                return visitor.visitMayor(self)
            else:
                return visitor.visitChildren(self)


    class MenorContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(marzoParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMenor" ):
                listener.enterMenor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMenor" ):
                listener.exitMenor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMenor" ):
                return visitor.visitMenor(self)
            else:
                return visitor.visitChildren(self)


    class PrimariaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Numero(self):
            return self.getToken(marzoParser.Numero, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaria" ):
                listener.enterPrimaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaria" ):
                listener.exitPrimaria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaria" ):
                return visitor.visitPrimaria(self)
            else:
                return visitor.visitChildren(self)


    class SecundariaContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Letra(self):
            return self.getToken(marzoParser.Letra, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSecundaria" ):
                listener.enterSecundaria(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSecundaria" ):
                listener.exitSecundaria(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSecundaria" ):
                return visitor.visitSecundaria(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = marzoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [marzoParser.Numero]:
                localctx = marzoParser.PrimariaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 19
                self.match(marzoParser.Numero)
                pass
            elif token in [marzoParser.Letra]:
                localctx = marzoParser.SecundariaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.match(marzoParser.Letra)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 35
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = marzoParser.SumaContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 23
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 24
                        self.match(marzoParser.T__0)
                        self.state = 25
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = marzoParser.AsignacionContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 26
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 27
                        self.match(marzoParser.T__1)
                        self.state = 28
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = marzoParser.MenorContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 29
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 30
                        self.match(marzoParser.T__2)
                        self.state = 31
                        self.expression(3)
                        pass

                    elif la_ == 4:
                        localctx = marzoParser.MayorContext(self, marzoParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 32
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 33
                        self.match(marzoParser.T__3)
                        self.state = 34
                        self.expression(2)
                        pass

             
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return marzoParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfnoelseContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)

        def statement(self):
            return self.getTypedRuleContext(marzoParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfnoelse" ):
                listener.enterIfnoelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfnoelse" ):
                listener.exitIfnoelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfnoelse" ):
                return visitor.visitIfnoelse(self)
            else:
                return visitor.visitChildren(self)


    class PrintContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class DeclaracionContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Letra(self):
            return self.getToken(marzoParser.Letra, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a marzoParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(marzoParser.ExpressionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(marzoParser.StatementContext)
            else:
                return self.getTypedRuleContext(marzoParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = marzoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = marzoParser.IfnoelseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(marzoParser.T__4)
                self.state = 41
                self.expression(0)
                self.state = 42
                self.match(marzoParser.T__5)
                self.state = 43
                self.statement()
                pass

            elif la_ == 2:
                localctx = marzoParser.IfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(marzoParser.T__4)
                self.state = 46
                self.expression(0)
                self.state = 47
                self.match(marzoParser.T__5)
                self.state = 48
                self.statement()
                self.state = 49
                self.match(marzoParser.T__6)
                self.state = 50
                self.statement()
                pass

            elif la_ == 3:
                localctx = marzoParser.DeclaracionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.match(marzoParser.T__7)
                self.state = 53
                self.match(marzoParser.Letra)
                pass

            elif la_ == 4:
                localctx = marzoParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.match(marzoParser.T__8)
                self.state = 55
                self.expression(0)
                self.state = 56
                self.match(marzoParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




