from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"


class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInteger", MType(list(), IntegerType()), CName(self.libName)),
                Symbol("printInteger", MType(
                    [IntegerType()], VoidType()), CName(self.libName)),
                Symbol("readFloat", MType(list(), FloatType()),
                       CName(self.libName)),
                Symbol("printFloat", MType(
                    [FloatType()], VoidType()), CName(self.libName)),
                Symbol("readBoolean", MType(
                    list(), BooleanType()), CName(self.libName)),
                Symbol("printBoolean", MType(
                    [BooleanType()], VoidType()), CName(self.libName)),
                Symbol("readString", MType(
                    list(), StringType()), CName(self.libName)),
                Symbol("printString", MType(
                    [StringType()], VoidType()), CName(self.libName)),
                ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value


class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path

    def visitProgram(self, ast, c):
        [self.visit(i, c)for i in ast.decl]
        return c

    # def visitClassDecl(self, ast, c):
    #     self.className = ast.classname.name
    #     self.emit = Emitter(self.path+"/" + self.className + ".j")
    #     self.emit.printout(self.emit.emitPROLOG(
    #         self.className, "java.lang.Object"))
    #     [self.visit(ele, SubBody(None, self.env))
    #      for ele in ast.memlist if type(ele) == MethodDecl]
    #     # generate default constructor
    #     self.genMETHOD(MethodDecl(Instance(), Id("<init>"), list(
    #     ), None, Block([], [])), c, Frame("<init>", VoidType()))
    #     self.emit.emitEPILOG()
    #     return c

    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(
            consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayType(0, StringType())] if isMain else list(
            map(lambda x: x.typ, consdecl.param))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                Id(self.className)), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(
                0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            local = reduce(lambda env, ele: SubBody(
                frame, [self.visit(ele, env)]+env.sym), consdecl.param, SubBody(frame, []))
            glenv = local.sym+glenv

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR(
                "this", ClassType(Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body.stmt))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitVarDecl(self, ast, o): pass
    def visitParamDecl(self, ast, o): pass
    def visitFuncDecl(self, ast, o): pass

    # def visitFuncDecl(self, ast, o):
    #     frame = Frame(ast.name, ast.returnType)
    #     self.genMETHOD(ast, o.sym, frame)
    #     return Symbol(ast.name, MType([x.typ for x in ast.param], ast.returnType), CName(self.className))

    def visitAssignStmt(self, ast, o): pass
    def visitBlockStmt(self, ast, o): pass
    def visitIfStmt(self, ast, o):
        cond, typ = self.visit(ast.cond, Access(o.frame, o.sym, False, False))
        flabel = o.frame.getNewLabel() # False Label
        elabel = o.frame.getNewLabel() # Exit Label
        self.emit.printout(cond)
        self.emit.printout(self.emit.emitIFFALSE(flabel, o.frame))
        self.visit(ast.tstmt, o)
        self.emit.printout(self.emit.emitGOTO(elabel, o.frame))
        self.emit.printout(self.emit.emitLABEL(flabel, o.frame))
        if ast.fstmt is not None:
            self.visit(ast.fstmt, o)
        self.emit.printout(self.emit.emitLABEL(elabel, o.frame))

    def visitForStmt(self, ast, o): pass
    def visitWhileStmt(self, ast, o): pass
    def visitDoWhileStmt(self, ast, o): pass
    def visitBreakStmt(self, ast, o): pass

    def visitContinueStmt(self, ast, o): pass
    def visitReturnStmt(self, ast, o): pass
    def visitCallStmt(self, ast, o): pass
    # def visitCallStmt(self, ast, o):
    #     ctxt = o
    #     frame = ctxt.frame
    #     nenv = ctxt.sym
    #     sym = next(filter(lambda x: ast.method.name == x.name, nenv), None)
    #     cname = sym.value.value
    #     ctype = sym.mtype
    #     in_ = ("", list())
    #     for x in ast.param:
    #         str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
    #         in_ = (in_[0] + str1, in_[1].append(typ1))
    #     self.emit.printout(in_[0])
    #     self.emit.printout(self.emit.emitINVOKESTATIC(
    #         cname + "/" + ast.method.name, ctype, frame))

    # def visitBinaryOp(self, ast, o):
    #     e1c, e1t = self.visit(ast.left, o)
    #     e2c, e2t = self.visit(ast.right, o)
    #     return e1c + e2c + self.emit.emitADDOP(ast.op, e1t, o.frame), e1t

    def visitBinExpr(self, ast, o):
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        if ast.op in ['+', '-']:
            if type(e1t) is IntegerType and type(e2t) is IntegerType:
                return e1c + e2c + self.emit.emitADDOP(ast.op, IntegerType(), o.frame), IntegerType()
            else:
                if type(e1t) is IntegerType:
                    e1c += self.emit.emitI2F(o.frame)
                if type(e2t) is IntegerType:
                    e2c += self.emit.emitI2F(o.frame)
                return e1c + e2c + self.emit.emitADDOP(ast.op, FloatType(), o.frame), FloatType()
        elif ast.op in ['*', '/']:
            if type(e1t) is IntegerType and type(e2t) is IntegerType:
                return e1c + e2c + self.emit.emitMULOP(ast.op, IntegerType(), o.frame), IntegerType()
            else:
                if type(e1t) is IntegerType:
                    e1c += self.emit.emitI2F(o.frame)
                if type(e2t) is IntegerType:
                    e2c += self.emit.emitI2F(o.frame)
                return e1c + e2c + self.emit.emitMULOP(ast.op, FloatType(), o.frame), FloatType()
        elif ast.op in ['%']:
            return e1c + e2c + self.emit.emitMOD(o.frame), IntegerType()
        elif ast.op in ['>', '<', '>=', '<=']:
            if type(e1t) is IntegerType and type(e2t) is IntegerType:
                return e1c + e2c + self.emit.emitREOP(ast.op, IntegerType(), o.frame), BooleanType()
            else:
                if type(e1t) is IntegerType:
                    e1c += self.emit.emitI2F(o.frame)
                if type(e2t) is IntegerType:
                    e2c += self.emit.emitI2F(o.frame)
                return e1c + e2c + self.emit.emitREOP(ast.op, FloatType(), o.frame), BooleanType()
        elif ast.op in ['==', '!=']:
            return e1c + e2c + self.emit.emitREOP(ast.op, IntegerType(), o.frame), BooleanType()
        elif ast.op in ['::']:
            return

    def visitUnExpr(self, ast, o):
        valc, valt = self.visit(ast.val, o)
        if ast.op in ['!']:
            return valc + self.emit.emitNOT(valt, o.frame), valt
        elif ast.op in ['-']:
            return valc + self.emit.emitNEGOP(valt, o.frame), valt
    
    def visitId(self, ast, o):
        if o.isLeft == False:
            for x in o.sym:
                if x.name == ast.name:
                    if type(x.value) is Index:
                        return self.emit.emitREADVAR(x.name, x.mtype, x.value.value, o.frame), x.mtype
                    else:
                        return self.emit.emitGETSTATIC(x.value.value + "." + x.name, x.mtype, o.frame), x.mtype
        else:
            for x in o.sym:
                if x.name == ast.name:
                    if type(x.value) is Index:
                        return self.emit.emitWRITEVAR(x.name, x.mtype, x.value.value, o.frame), x.mtype
                    else:
                        return self.emit.emitPUTSTATIC(x.value.value + "." + x.name, x.mtype, o.frame), x.mtype
    
    def visitArrayCell(self, ast, o): pass

    def visitIntegerLit(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntegerType()

    def visitFloatLit(self, ast, o):
        return self.emit.emitPUSHFCONST(ast.value, o.frame), FloatType()

    def visitStringLit(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()

    def visitBooleanLit(self, ast, o):
        return self.emit.emitPUSHICONST(str(ast.value), o.frame), BooleanType()

    def visitArrayLit(self, ast, o):
        code = list()
        typ = list()
        for ele in ast.explist:
            ecode, etyp = self.visit(ele, Access(o.frame, o.sym, False, False))
            code += list(ecode)
            typ += list(etyp)
        return code, typ

    def visitFuncCall(self, ast, o): pass

    def visitIntegerType(self, ast, o): return ast
    def visitFloatType(self, ast, o): return ast
    def visitBooleanType(self, ast, o): return ast
    def visitStringType(self, ast, o): return ast
    def visitArrayType(self, ast, o): return ast
    def visitAutoType(self, ast, o): return ast
    def visitVoidType(self, ast, o): return ast
