# Generated from /Users/aldoponce/8vo/Compiladores/TareaGeneradorBasico/marzo/marzo.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .marzoParser import marzoParser
else:
    from marzoParser import marzoParser

# This class defines a complete listener for a parse tree produced by marzoParser.
class marzoListener(ParseTreeListener):

    # Enter a parse tree produced by marzoParser#program.
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        pass

    # Exit a parse tree produced by marzoParser#program.
    def exitProgram(self, ctx:marzoParser.ProgramContext):
        pass


    # Enter a parse tree produced by marzoParser#suma.
    def enterSuma(self, ctx:marzoParser.SumaContext):
        pass

    # Exit a parse tree produced by marzoParser#suma.
    def exitSuma(self, ctx:marzoParser.SumaContext):
        pass


    # Enter a parse tree produced by marzoParser#asignacion.
    def enterAsignacion(self, ctx:marzoParser.AsignacionContext):
        pass

    # Exit a parse tree produced by marzoParser#asignacion.
    def exitAsignacion(self, ctx:marzoParser.AsignacionContext):
        pass


    # Enter a parse tree produced by marzoParser#mayor.
    def enterMayor(self, ctx:marzoParser.MayorContext):
        pass

    # Exit a parse tree produced by marzoParser#mayor.
    def exitMayor(self, ctx:marzoParser.MayorContext):
        pass


    # Enter a parse tree produced by marzoParser#menor.
    def enterMenor(self, ctx:marzoParser.MenorContext):
        pass

    # Exit a parse tree produced by marzoParser#menor.
    def exitMenor(self, ctx:marzoParser.MenorContext):
        pass


    # Enter a parse tree produced by marzoParser#primaria.
    def enterPrimaria(self, ctx:marzoParser.PrimariaContext):
        pass

    # Exit a parse tree produced by marzoParser#primaria.
    def exitPrimaria(self, ctx:marzoParser.PrimariaContext):
        pass


    # Enter a parse tree produced by marzoParser#secundaria.
    def enterSecundaria(self, ctx:marzoParser.SecundariaContext):
        pass

    # Exit a parse tree produced by marzoParser#secundaria.
    def exitSecundaria(self, ctx:marzoParser.SecundariaContext):
        pass


    # Enter a parse tree produced by marzoParser#ifnoelse.
    def enterIfnoelse(self, ctx:marzoParser.IfnoelseContext):
        pass

    # Exit a parse tree produced by marzoParser#ifnoelse.
    def exitIfnoelse(self, ctx:marzoParser.IfnoelseContext):
        pass


    # Enter a parse tree produced by marzoParser#if.
    def enterIf(self, ctx:marzoParser.IfContext):
        pass

    # Exit a parse tree produced by marzoParser#if.
    def exitIf(self, ctx:marzoParser.IfContext):
        pass


    # Enter a parse tree produced by marzoParser#declaracion.
    def enterDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by marzoParser#declaracion.
    def exitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by marzoParser#print.
    def enterPrint(self, ctx:marzoParser.PrintContext):
        pass

    # Exit a parse tree produced by marzoParser#print.
    def exitPrint(self, ctx:marzoParser.PrintContext):
        pass



del marzoParser