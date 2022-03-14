from marzo.marzoListener import marzoListener
from marzo.marzoParser import marzoParser

class GenCode(marzoListener):



    def __init__(self):
        self.var = 0
        self.ifCounter = 0
        self.queue = []
        self.stack = []
        self.isIf = False
    
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        print(".text")

    def exitPrimaria(self, ctx:marzoParser.PrimariaContext):
        self.var+=1
        self.ifCounter+=1
        self.queue.append(self.var)
        self.stack.append(self.var)
        if(self.ifCounter > 3 and self.isIf):
            print("ELSE:")
        print("li $v" + str(self.var) + ", " + ctx.Numero().getText())

    def exitSecundaria(self, ctx:marzoParser.PrimariaContext):
        self.var+=1
        self.ifCounter+=1
        self.queue.append(self.var)
        self.stack.append(self.var)
        if(self.ifCounter > 3 and self.isIf):
            print("ELSE:")
        print("lw $v" + str(self.var) + ", " + ctx.Letra().getText())


    def exitSuma(self, ctx:marzoParser.SumaContext):
        if(self.ifCounter > 3 and self.isIf):
            print("ELSE:")
        print("ADD $v" + str((self.var)) +", " + "$v" + str(self.stack.pop()) + ", " + "$v" + str(self.stack.pop()))
    
    def exitAsignacion(self, ctx:marzoParser.AsignacionContext):
        if(self.ifCounter > 3):
            print("ELSE:")
        print("li $v" + str((self.var)) +", " + "$v" + str(self.stack.pop()) + ", " + "$v" + str(self.stack.pop()))

    def exitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        self.var+=1
        self.ifCounter+=1
        self.queue.append(self.var)
        self.stack.append(self.var)
        if(self.ifCounter > 3 and self.isIf):
            print("ELSE:")
        print("sw $v" + str(self.var) + ", " + ctx.Letra().getText())

    def exitMayor(self, ctx:marzoParser.MayorContext):
        print("stg $v" + str((self.var)) +", " + "$v" + str(self.stack.pop(1)) + ", " + "$v" + str(self.stack.pop()))

    def exitMenor(self, ctx:marzoParser.MenorContext):
        print("slt $v" + str((self.var)) +", " + "$v" + str(self.stack.pop(1)) + ", " + "$v" + str(self.stack.pop()))
    
    def exitPrint(self, ctx:marzoParser.PrintContext):
        print("syscall")

    def exitIf(self, ctx:marzoParser.IfContext):
        print("beq $v" + str(self.queue.pop(0)) +", $v" + str(self.queue.pop(0)) + ", ELSE")
        self.isIf = False
        self.ifCounter = 0

    def enterIf(self, ctx:marzoParser.IfContext):
        self.isIf = True
        self.ifCounter = 0
    

