from Visitor import Visitor
from AST import *
from StaticError import *

spec_lst = [
    FuncDecl('readInteger', IntegerType(), [], None, None),
    FuncDecl('printInteger', VoidType(), [IntegerType()], None, None),
    FuncDecl('readFloat', FloatType(), [], None, None),
    FuncDecl('printFloat', VoidType(), [FloatType()], None, None),
    FuncDecl('readBoolean', BooleanType(), [], None, None),
    FuncDecl('printBoolean', VoidType(), [BooleanType()], None, None),
    FuncDecl('readString', StringType(), [], None, None),
    FuncDecl('printString', VoidType(), [StringType()], None, None),
    FuncDecl('super', VoidType(), [], None, None),
    FuncDecl('preventDefault', VoidType(), [], None, None)
]

spec_name_lst = ['readInteger', 'printInteger', 'readFloat', 'printFloat', 'readBoolean', 'printBoolean', 'readString', 'printString', 'super', 'preventDefault']

class Utils:
    def infer(symbol_list, name, typ):
        for symbol in symbol_list:
            for x in symbol:
                if x.name == name:
                    x.typ = typ
                    return typ

    def infer_return_type(symbol_list, name, return_type):
        for symbol in symbol_list:
            for x in symbol:
                if x.name == name:
                    x.return_type = return_type
                    return return_type
    
    def infer_small_loop(symbol, name, typ):
        for i in symbol:
            if i.name == name:
                i.typ = typ
                return
    
    def infer_small_loop_return_type(symbol, name, return_type):
        for i in symbol:
            if i.name == name:
                i.return_type = return_type
                return return_type
    
    def find(symbol_list, name):
        for symbol in symbol_list:
            for x in symbol:
                if x.name == name:
                    return x
        return None
    
    def find_small_loop(symbol_list, name):
        for symbol in symbol_list:
            if symbol.name == name:
                return symbol
        return None
# xong

class GetEnv(Visitor):
    def __init__(self): pass
    
    def visitProgram(self, ast: Program, param):
        param = []
        for decls in ast.decls:
            if isinstance(decls, FuncDecl):
                param = self.visit(decls, param)
        return param

    def visitFuncDecl(self, ast: FuncDecl, param):
        lst = []
        for x in ast.params:
            lst = self.visit(x, lst)

        param += [FuncDecl(ast.name, ast.return_type, lst, ast.inherit, None)]
        return param
    # phai lay param ra truoc
    def visitParamDecl(self, ast: ParamDecl, param):
        param += [ParamDecl(ast.name, ast.typ, ast.out, ast.inherit)]
        return param


class StaticChecker(Visitor):
    def __init__(self, ast):
        self.function = spec_lst
        self.ast = ast
        self.flag = False
        self.curr_name = None
    
    def check(self):
        return self.visit(self.ast, [])

    def __del__(self):
        self.function = []
    # xong
    def visitProgram(self, ast: Program, param):
        is_main = False
        # for i in self.function:
        #     print(i.name)
        get_env = GetEnv().visit(ast, param)
        self.function = self.function + get_env
        # print(self.function)
        param = [[]]
        for decls in ast.decls:
            if isinstance(decls, FuncDecl):
                if decls.name == "main" and len(decls.params) == 0 and isinstance(decls.return_type, VoidType):
                    is_main = True
            param = self.visit(decls, param)

        if is_main == False:  # chekc if main in program
            raise NoEntryPoint() 
    
    ################################################################ Declarations ########################################################
    # xong
    def visitVarDecl(self, ast: VarDecl, param):  # a: integer = 3
        for x in param[0]:
            if x.name == ast.name:
                raise Redeclared(Variable(), ast.name)
        # 1. auto type
        if isinstance(ast.typ, AutoType):
            if ast.init is None:  # a: auto
                raise Invalid(Variable(), ast.name)
            else:  # a: auto = 3 -> VarDecl(a, int)
                init_typ = self.visit(ast.init, param)
                param[0] += [VarDecl(ast.name, init_typ, ast.init)]

        #  2. array type
        elif isinstance(ast.typ, ArrayType):
            if ast.init is None:
                param[0] += [VarDecl(ast.name, ast.typ, None)]
            # a: array[2] of integer = {1,2}
            else:
                if isinstance(ast.init, ArrayLit):
                    dim = 1
                    for x in ast.typ.dimensions:
                        dim *= int(x)
                    
                    if dim != len(ast.init.explist):
                        raise TypeMismatchInVarDecl(ast)
                    # elif ast.typ.typ is not type(ast.init.explist):
                    #     raise TypeMismatchInVarDecl(ast)
                    
                    init_typ = self.visit(ast.init, param)
                    param[0] += [VarDecl(ast.name, init_typ, ast.init)]
                else:  # a: array[2] of intefer = 1
                    raise TypeMismatchInVarDecl(ast)

        # 3. atomic type
        else:
            if ast.init is None:  # a: float
                param[0] += [VarDecl(ast.name, ast.typ, None)]
            else:
                init_typ = self.visit(ast.init, param)
                if isinstance(ast.typ, FloatType) and isinstance(init_typ, IntegerType):  # a: float = 1
                    param[0] += [VarDecl(ast.name, ast.typ, ast.init)]
                
                elif isinstance(init_typ, AutoType):  # a: int = b
                    # id
                    if isinstance(init_typ, Id):
                        Utils.infer(param, ast.init.name, ast.typ)
                    else:  # a: int = foo(1)
                        Utils.infer_return_type(param, ast.init.name, ast.typ)
                        # upd self.function return_typ
                        Utils.infer_small_loop_return_type(self.function, ast.init.name, ast.typ)
                elif type(ast.typ) is not type(init_typ):  # a: int = 3.0
                    raise TypeMismatchInVarDecl(ast)
                else:
                    param[0] += [VarDecl(ast.name, ast.typ, ast.init)]
        return param

    # xong
    def visitParamDecl(self, ast: ParamDecl, param):
        for x in param[0]:
            if x.name == ast.name:
                raise Redeclared(Parameter(), ast.name)
        # invalid param decl
        # typ = self.visit(ast.typ, param)
        # param[0] += [ParamDecl(ast.name, typ, ast.out, ast.inherit)]
        return param

    # chua xong
    def visitFuncDecl(self, ast: FuncDecl, param):
        for x in spec_name_lst:
            if ast.name == x:
                raise Redeclared(Function(), ast.name)
        
        for env in param:
            for x in env:
                if x is not None:
                    if x.name == ast.name:
                        raise Redeclared(Function(), ast.name)
        
        # for x in self.function:
        #     print(x.name)
        func = Utils.find_small_loop(self.function, ast.name)
        # if func.params != ast.params:
        #     func = Utils.find(param, ast.name)
        param[0] += [func]
        
        env = [[]] + param
        parent = None  # function bar(a,b)
        # ast.inherit la ten cua parent function
        # function foo(c,d) inherit bar
        self.curr_name = ast.name
        if ast.inherit is not None:
            parent = Utils.find_small_loop(self.function, ast.inherit)

            if parent is None:
                raise Undeclared(Function(), ast.inherit)
            else:
                inherit_lst = []
                tmp = None
                # invalid
                # param truoc, body sau
                for x in ast.params:  # a, b, c
                    for param in parent.params:  # inherit a, b, c
                        if param.name in spec_name_lst:
                            raise Redeclared(Parameter(), param.name)
                        elif param.name == x.name:
                            raise Invalid(Parameter(), param.name)
                        # elif param.inherit == True:
                        tmp = param
                    inherit_lst += [x]

                    # env = self.visit(x, env)
                first_stmt = None
                for stmt in ast.body.body:
                    if isinstance(stmt, CallStmt):
                        first_stmt = stmt
                        break
                
                if first_stmt is not None:
                    if len(parent.params) != 0:
                        if first_stmt.name != "preventDefault" and first_stmt.name != "super":
                            raise InvalidStatementInFunction(ast.name)
                        elif first_stmt.name == 'preventDefault' and len(first_stmt.args) > 0:
                            raise TypeMismatchInStatement(first_stmt)
                    
                    if first_stmt.name != 'preventDefault':
                        env[0] += [tmp]
                    else:
                        env[0] += inherit_lst
                # for stmt in ast.body.body:
                #     self.visit(stmt, env)
                        
                    # else:
                else:
                    raise InvalidStatementInFunction(ast.name)
        else:
            if len(func.params) != 0:
                for i, x in enumerate(func.params):
                    if x.name in spec_name_lst:
                        raise Redeclared(Parameter(), x.name)
                    
                    for j, y in enumerate(func.params):
                        if y.name == x.name and j != i:
                            # print(x,y)
                            raise Redeclared(Parameter(), x.name)
                    
                    env[0] += [x]
            
            first_stmt = None
            for stmt in ast.body.body:
                if isinstance(stmt, CallStmt):
                    first_stmt = stmt
                    break
            if isinstance(first_stmt, CallStmt):
                if first_stmt.name == 'preventDefault' or first_stmt.name == 'super':
                        raise InvalidStatementInFunction(ast.name)
            
            # for x in ast.body.body:
            #     print(2)
            #     self.visit(x, env)
                
        self.visit(ast.body, env)
        return env

    ################################################################ Statements ##########################################################
    # xong
    def visitAssignStmt(self, ast: AssignStmt, param):
        lhs = self.visit(ast.lhs, param)  # trai truoc, phai sau
        rhs = self.visit(ast.rhs, param)

        # lhs cannot be void or array type
        if isinstance(lhs, VoidType) or isinstance(lhs, ArrayType):
            raise TypeMismatchInStatement(ast)
        # auto type
        elif isinstance(lhs, AutoType):
            Utils.infer(param, ast.lhs.name, rhs)
        elif isinstance(rhs, AutoType):
            Utils.infer(param, ast.rhs.name, lhs)

        elif type(lhs) is not type(rhs):  # diff type lhs and rhs
            raise TypeMismatchInStatement(ast)

    # chua xong
    def visitBlockStmt(self, ast: BlockStmt, param):
        env = [[]] + param
        func = Utils.find_small_loop(self.function, self.curr_name)
        
        if len(ast.body) == 0:
            return
        
        for stmt in ast.body:
            if isinstance(stmt, VarDecl):
                env = self.visit(stmt, env)
            else:
                self.visit(stmt, env)
    # xong
    def visitIfStmt(self, ast: IfStmt, param):
        cond = self.visit(ast.cond, param)
        if isinstance(cond, BooleanType) == False:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.tstmt, param)
        if ast.fstmt is not None:
            self.visit(ast.fstmt, param)

    # xong
    def visitForStmt(self, ast: ForStmt, param):  # for (exp1, exp2, exp3)
        # check loop
        self.flag = True
        exp1 = self.visit(ast.init.lhs, param)
        exp2 = self.visit(ast.cond, param)
        exp3 = self.visit(ast.upd, param)
        if isinstance(exp1, IntegerType) == False or isinstance(exp2, BooleanType) == False or isinstance(exp3, IntegerType) == False:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, param)
        # end loop
        self.flag = False

    # xong
    def visitWhileStmt(self, ast: WhileStmt, param):
        self.flag = True
        cond = self.visit(ast.cond, param)
        if isinstance(cond, BooleanType) == False:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, param)
        # end loop
        self.flag = False

    # xong
    def visitDoWhileStmt(self, ast: DoWhileStmt, param):
        self.flag = True
        cond = self.visit(ast.cond, param)
        if isinstance(cond, BooleanType) == False:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, param)
        # end loop
        self.flag = False

    # xong
    def visitBreakStmt(self, ast: BreakStmt, param):
        if self.flag == False:
            raise MustInLoop(ast)

    # xong
    def visitContinueStmt(self, ast: ContinueStmt, param):
        if self.flag == False:
            raise MustInLoop(ast)

    # xong
    def visitReturnStmt(self, ast: ReturnStmt, param):
        if ast.expr is None:
            typ = VoidType()
        else:
            typ = self.visit(ast.expr, param)
        
        # save current name
        func_typ = None
        for ele in self.function:
            if ele.name == self.curr_name:
                func_typ = ele.return_type
                break
        
        # if isinstance(func_typ, VoidType()) and ast.expr is not None:
        #     raise TypeMismatchInStatement(ast)
        
        if func_typ is None:
            func_typ = VoidType()
        
        if isinstance(func_typ, AutoType):
            Utils.infer_small_loop(self.function, self.curr_name, typ)

        elif isinstance(func_typ, FloatType) and isinstance(typ, IntegerType):
            typ = FloatType()
        
        elif type(func_typ) != type(typ):
            raise TypeMismatchInStatement(ast)
        
        for symbol in param:
            for x in symbol:
                if x.name == self.curr_name:
                    x.return_type = typ

    # xong (giong FuncCall)
    def visitCallStmt(self, ast: CallStmt, param):
        func = Utils.find_small_loop(self.function, ast.name)
        if func is None:
            raise Undeclared(Function(), ast.name)
        elif isinstance(func, FuncDecl) == False:
            raise TypeMismatchInStatement(ast)

        arg_lst = [] # [3.5, 4]
        for x in ast.args:
            arg_lst += [self.visit(x, param)]
        

        param_lst = []
        if func.name == 'super':
            child = Utils.find_small_loop(self.function, self.curr_name)
            parent = Utils.find_small_loop(self.function, child.inherit)
            
            param_lst = parent.params
        else:
            param_lst = func.params
        
        if len(param_lst) != len(arg_lst):
            raise TypeMismatchInStatement(ast)
        else:
            for i in range(len(param_lst)):
                if isinstance(param_lst[i], AutoType):
                    
                    for x in self.function:
                        if x.name == ast.name:
                            
                            Utils.infer_small_loop(x.params, param_lst[i].name, arg_lst[i])
                        
                elif isinstance(arg_lst[i], AutoType):
                    Utils.infer(param, arg_lst[i].name, param_lst[i])
                    for x in self.function:
                        if x.name == ast.name:
                            
                            Utils.infer_small_loop(x.params, arg_lst[i].name, param_lst[i])
                    # Utils.infer_small_loop(self.function, arg_lst[i].name, param_lst[i])

                elif isinstance(param_lst[i], ParamDecl):
                    if isinstance(param_lst[i].typ, AutoType):
                        
                        for x in self.function:
                            if x.name == ast.name:
                                Utils.infer_small_loop(x.params, param_lst[i].name, arg_lst[i])
                        
                    # print(param_lst[i].typ, arg_lst[i])
                    if type(param_lst[i].typ) is not type(arg_lst[i]):
                        raise TypeMismatchInExpression(ast.args[i])
                
                elif param_lst[i] != arg_lst[i]:
                    raise TypeMismatchInExpression(ast.args[i])
        
        
        return

    ################################################################ Expressions #########################################################
    # xong
    def visitBinExpr(self, ast: BinExpr, param):
        arith_op = ['+', '-', '*', '/']
        bool_op = ['&&', '||']
        rela_bool_op = ['==', '!=']
        rela_comp_op = ['<', '>', '<=', '>=']
        ltyp = self.visit(ast.left, param)
        rtyp = self.visit(ast.right, param)
        
        if isinstance(ltyp, AutoType):
            ltyp = rtyp
            Utils.infer_small_loop(self.function, ast.left.name, rtyp)
        elif isinstance(rtyp, AutoType):
            rtyp = ltyp
            Utils.infer_small_loop(self.function, ast.right.name, ltyp)
        
        if ast.op in arith_op:
            if isinstance(ltyp, IntegerType) and isinstance(rtyp, IntegerType):
                return IntegerType()
            elif (isinstance(ltyp, FloatType) and isinstance(rtyp, IntegerType)) or (isinstance(ltyp, IntegerType) and isinstance(rtyp, FloatType)) or (isinstance(ltyp, FloatType) and isinstance(rtyp, FloatType)):
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)

        elif ast.op == '%':
            if isinstance(ltyp, IntegerType) and isinstance(rtyp, IntegerType):
                return IntegerType()
            else:
                raise TypeMismatchInExpression(ast)
        
        elif ast.op in bool_op:
            if (isinstance(ltyp, IntegerType) and isinstance(rtyp, IntegerType)) or (isinstance(ltyp, BooleanType) and isinstance(rtyp, BooleanType)):
                return BooleanType()
            elif (isinstance(ltyp, IntegerType) and isinstance(rtyp, BooleanType)) or (isinstance(ltyp, BooleanType) and isinstance(rtyp, IntegerType)):
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ast)
            
        elif ast.op == '::':
            if isinstance(ltyp, StringType) and isinstance(rtyp, StringType):
                return StringType()
            else:
                raise TypeMismatchInExpression(ast)
        
        elif ast.op in rela_bool_op:
            if (isinstance(ltyp, IntegerType) and isinstance(rtyp, IntegerType)) or (isinstance(ltyp, BooleanType) and isinstance(rtyp, BooleanType)):
                return BooleanType()
            elif (isinstance(ltyp, IntegerType) and isinstance(rtyp, BooleanType)) or (isinstance(ltyp, BooleanType) and isinstance(rtyp, IntegerType)):
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ast)

        elif ast.op in rela_comp_op:
            if isinstance(ltyp, IntegerType) and isinstance(rtyp, IntegerType):
                return BooleanType()
            elif (isinstance(ltyp, FloatType) and isinstance(rtyp, IntegerType)) or (isinstance(ltyp, IntegerType) and isinstance(rtyp, FloatType)) or (isinstance(ltyp, FloatType) and isinstance(rtyp, FloatType)):
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ast)

    # xong
    def visitUnExpr(self, ast: UnExpr, param):
        typ = self.visit(ast.val, param)
        if ast.op == '!':
            if isinstance(typ, BooleanType):
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ast)

        elif ast.op == '-':
            if isinstance(typ, IntegerType):
                return IntegerType()
            elif isinstance(typ, FloatType):
                return FloatType()
            else:
                raise TypeMismatchInExpression(ast)

    # xong
    def visitId(self, ast: Id, param):
        for env in param:
            for x in env:
                if x.name == ast.name:
                    return x.typ
        raise Undeclared(Identifier(), ast.name)

    # xong (chua chac)
    def visitArrayCell(self, ast: ArrayCell, param):
        arr = Utils.find(param, ast.name)
        if arr is None:
            raise Undeclared(Variable(), ast.name)
        
        else:
            if isinstance(arr, ArrayType):
                cell_lst = []
                for x in ast.cell:
                    cell_lst += [self.visit(x, param)]

                for x in cell_lst:
                    if isinstance(x, IntegerType) is False:
                        raise TypeMismatchInExpression(ast)
                
                if len(cell_lst) != len(arr.typ.dimensions):
                    raise TypeMismatchInExpression(ast)
                return arr.typ.typ
            else:
                raise TypeMismatchInExpression(ast)

    def visitIntegerLit(self, ast: IntegerLit, param):
        return IntegerType()
    
    def visitFloatLit(self, ast: FloatLit, param):
        return FloatType()
    
    def visitStringLit(self, ast: StringLit, param):
        return StringType()
    
    def visitBooleanLit(self, ast: BooleanLit, param):
        return BooleanType()
    
    # xong (ch chac)
    def visitArrayLit(self, ast: ArrayLit, param):
        arr_lst = []
        for x in ast.explist:
            arr_lst += [self.visit(x, param)]
        
        # if len(arr_lst) == 0:
        #     raise IllegalArrayLiteral(ast)
        
        # nay laf check r
        for i in range(0, len(arr_lst) - 1):
            # if len(arr_lst[i]) == 0:
            #     raise IllegalArrayLiteral(ast)
            # print(arr_lst[i], arr_lst[i+1])
            if isinstance(arr_lst[i], ArrayType) and isinstance(arr_lst[i + 1], ArrayType):
                # multi dimension
                if (type(arr_lst[i].typ) is not type(arr_lst[i + 1].typ)) or (arr_lst[i].dimensions != arr_lst[i + 1].dimensions):
                    raise IllegalArrayLiteral(ast)
            
            elif type(arr_lst[i]) is not type(arr_lst[i + 1]):
                raise IllegalArrayLiteral(ast)
        
        # setup dimension arr[2][3]
        dim = [len(arr_lst)]
        typ = None
        # chac chan cac list co cung kieu
        if isinstance(arr_lst[0], ArrayType):
            typ = arr_lst[0].typ
            dim += arr_lst[0].dimensions
        
        return ArrayType(dim, typ)

    # xong
    def visitFuncCall(self, ast: FuncCall, param):
        func = Utils.find_small_loop(self.function, ast.name)
        if func is None:
            raise Undeclared(Function(), ast.name)
        
        else:
            if isinstance(func, FuncDecl):
                if isinstance(func.return_type, VoidType):
                    raise TypeMismatchInExpression(ast)
                
                arg_lst = [] # [3.5, 4]
                for x in ast.args:
                    arg_lst += [self.visit(x, param)]
                
                param_lst = func.params
                # [ParamDecl(a, AutoType), ParamDecl(b, IntType)]
                if len(param_lst) != len(arg_lst):
                    raise TypeMismatchInStatement(ast)
                else:
                    # foo(3.5, 4)
                    # foo: function int (a: auto, b: int)
                    for i in range(len(param_lst)):
                        if isinstance(param_lst[i], AutoType):
                            for x in self.function:
                                if x.name == ast.name:
                                    Utils.infer_small_loop(x.params, param_lst[i].name, type(arg_lst[i]))
                        
                        elif isinstance(arg_lst[i], AutoType):
                            Utils.infer(param, arg_lst[i].name, param_lst[i].typ)
                        
                        elif isinstance(param_lst[i], ParamDecl):
                            if param_lst[i].typ != arg_lst[i]:
                                raise TypeMismatchInExpression(ast.args[i])
                        
                        elif param_lst[i] != arg_lst[i]:
                            raise TypeMismatchInExpression(ast.args[i])
            else:
                raise TypeMismatchInStatement(ast)
            
        return func.return_type
            
    ################################################################ Types ###############################################################
    def visitIntegerType(self, ast: IntegerType, param):
        return IntegerType()

    def visitFloatType(self, ast: FloatType, param):
        return FloatType()

    def visitBooleanType(self, ast: BooleanType, param):
        return BooleanType()

    def visitStringType(self, ast: StringType, param):
        return StringType()

    def visitArrayType(self, ast: ArrayType, param):
        return ArrayType(ast.dimensions, ast.typ)

    def visitAutoType(self, ast: AutoType, param):
        return AutoType()

    def visitVoidType(self, ast: VoidType, param):
        return VoidType()
