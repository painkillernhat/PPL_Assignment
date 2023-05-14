from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *

class ASTGeneration(MT22Visitor):

    def __init__(self):
        self.id_list = []
        self.exp_list = []
    
    ################################################################ Program #############################################################
    # program: program_decl EOF ;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.program_decl()))
    
    # program_decl: program_content program_decl | program_content ;
    def visitProgram_decl(self, ctx: MT22Parser.Program_declContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.program_content()) + self.visit(ctx.program_decl())
        else:
            return self.visit(ctx.program_content())

    # program_content: vardecl | funcdecl ;
    def visitProgram_content(self, ctx: MT22Parser.Program_contentContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        else: # if ctx.funcdecl()
            return self.visit(ctx.funcdecl())
    
    ################################################################ Declarations ########################################################
    # vardecl: (var_decl_short | var_recur) SEMICOLON; // variable declaration
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.var_decl_short():
            return self.visit(ctx.var_decl_short())
        else: # ctx.var_recur()
            return self.visit(ctx.var_recur())
    
    # var_decl_short: idlist COLON (atomic_typ | array_type | AUTO);
    def visitVar_decl_short(self, ctx: MT22Parser.Var_decl_shortContext):
        if ctx.atomic_typ():
            typ = self.visit(ctx.atomic_typ())
        elif ctx.array_type():
            typ = self.visit(ctx.array_type())
        else: # ctx.AUTO()
            typ = AutoType()
        
        idlst = self.visit(ctx.idlist())
        return [VarDecl(id, typ, None) for id in idlst]
    
    # var_recur: IDENTIFIER var_part init_list | IDENTIFIER COMMA var_recur COMMA init_list;
    def visitVar_recur(self, ctx: MT22Parser.Var_recurContext):
        # typ = self.visit(ctx.var_part())
        #global id_list, exp_list
        self.id_list = self.id_list + [ctx.IDENTIFIER().getText()]
        self.exp_list = [self.visit(ctx.init_list())] + self.exp_list
        if ctx.var_part():
            typ = self.visit(ctx.var_part())
            result = [VarDecl(id, typ, expr) for id, expr in zip(self.id_list, self.exp_list)]
            
        else:
            result = self.visit(ctx.var_recur())
        
        self.id_list = []
        self.exp_list = []
        return result

    # var_part: COLON (atomic_typ | AUTO | array_type) ASSIGN;
    def visitVar_part(self, ctx: MT22Parser.Var_partContext):
        if ctx.atomic_typ():
            return self.visit(ctx.atomic_typ())
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        else: # ctx.AUTO()
            return AutoType()
    
    # init_list: arraylit | exp;
    def visitInit_list(self, ctx: MT22Parser.Init_listContext):
        if ctx.arraylit():
            return self.visit(ctx.arraylit())
        else:
            return self.visit(ctx.exp())
    
    # idlist: IDENTIFIER COMMA idlist | IDENTIFIER ;
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFIER().getText()]
        else:
            return [ctx.IDENTIFIER().getText()] + self.visit(ctx.idlist())
    
    # arraylit: LB exp_list RB ;
    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        return ArrayLit(self.visit(ctx.exp_list()))
    
    # array_type: ARRAY dimension OF atomic_typ ;
    def visitArray_type(self, ctx: MT22Parser.Array_typeContext):
        return ArrayType(self.visit(ctx.dimension()), self.visit(ctx.atomic_typ()))

    # dimension: LS int_list RS;
    def visitDimension(self, ctx: MT22Parser.DimensionContext):
        return self.visit(ctx.int_list())

    # int_list: INTLIT COMMA int_list | INTLIT ;
    def visitInt_list(self, ctx: MT22Parser.Int_listContext):
        if ctx.getChildCount() == 1:
            return [ctx.INTLIT().getText()]
        else:
            return [ctx.INTLIT().getText()] + self.visit(ctx.int_list())
    
    # paramdecl: INHERIT? OUT? IDENTIFIER COLON (atomic_typ | AUTO | array_type);
    def visitParamdecl(self, ctx: MT22Parser.ParamdeclContext):
        if ctx.INHERIT():
            inherit_flag = True
        else:
            inherit_flag = False

        if ctx.OUT():
            out_flag = True
        else:
            out_flag = False
        
        if ctx.atomic_typ():
            typ = self.visit(ctx.atomic_typ())
        elif ctx.array_type():
            typ = self.visit(ctx.array_type())
        else: # ctx.AUTO()
            typ = AutoType()
        
        return ParamDecl(ctx.IDENTIFIER().getText(), typ, out_flag, inherit_flag)

    # funcdecl: IDENTIFIER COLON FUNCTION (atomic_typ | VOID| array_type | AUTO) LP param_list RP (INHERIT IDENTIFIER)? block_stmt;
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        if ctx.atomic_typ():
            typ = self.visit(ctx.atomic_typ())
        elif ctx.array_type():
            typ = self.visit(ctx.array_type())
        elif ctx.AUTO(): # ctx.AUTO()
            typ = AutoType()
        else: # ctx.VOID()
            typ = VoidType()

        if ctx.INHERIT():
            inherit_flag = ctx.IDENTIFIER(1).getText()
        else:
            inherit_flag = None
        
        return [FuncDecl(ctx.IDENTIFIER(0).getText(), typ, self.visit(ctx.param_list()), inherit_flag, self.visit(ctx.block_stmt()))]

    # param_list: param_list_prime | ;
    def visitParam_list(self, ctx: MT22Parser.Param_listContext):
        if ctx.param_list_prime():
            return self.visit(ctx.param_list_prime())
        else:
            return []
    
    # param_list_prime: paramdecl COMMA param_list_prime | paramdecl;
    def visitParam_list_prime(self, ctx: MT22Parser.Param_list_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.paramdecl())]
        else:
            return [self.visit(ctx.paramdecl())] + self.visit(ctx.param_list_prime())
        
    ################################################################ Expressions #########################################################
    # relational_op: EQUAL | NOT_EQUAL | LESS_THAN | LESS_EQUAL_THAN | GREATER_THAN | GREATER_EQUAL_THAN ;
    def visitRelational_op(self, ctx: MT22Parser.Relational_opContext):
        if ctx.EQUAL():
            return ctx.EQUAL().getText()
        elif ctx.NOT_EQUAL():
            return ctx.NOT_EQUAL().getText()
        elif ctx.LESS_THAN():
            return ctx.LESS_THAN().getText()
        elif ctx.LESS_EQUAL_THAN():
            return ctx.LESS_EQUAL_THAN().getText()
        elif ctx.GREATER_THAN():
            return ctx.GREATER_THAN().getText()
        else:
            return ctx.GREATER_EQUAL_THAN().getText()
        
    # logical_op: LOG_AND | LOG_OR ;
    def visitLogical_op(self, ctx: MT22Parser.Logical_opContext):
        if ctx.LOG_AND():
            return ctx.LOG_AND().getText()
        else: #if ctx.LOG_OR():
            return ctx.LOG_OR().getText()

    # adding_op: ADDOP | SUBOP ;
    def visitAdding_op(self, ctx: MT22Parser.Adding_opContext):
        if ctx.ADDOP():
            return ctx.ADDOP().getText()
        else: #if ctx.SUBOP():
            return ctx.SUBOP().getText()

    # multiplying_op: MULOP | DIVOP | MODOP ;
    def visitMultiplying_op(self, ctx: MT22Parser.Multiplying_opContext):
        if ctx.MULOP():
            return ctx.MULOP().getText()
        elif ctx.DIVOP():
            return ctx.DIVOP().getText()
        else: #if ctx.MODOP():
            return ctx.MODOP().getText()
    
    # indexop: LS exp_list_prime RS ; // expression-list not nullable
    def visitIndexop(self, ctx: MT22Parser.IndexopContext):
        return self.visit(ctx.exp_list_prime())
    
    # exp_list: exp_list_prime | ;
    def visitExp_list(self, ctx: MT22Parser.Exp_listContext):
        if ctx.exp_list_prime():
            return self.visit(ctx.exp_list_prime())
        else:
            return []
    
    # exp_list_prime: exp COMMA exp_list_prime | exp ;
    def visitExp_list_prime(self, ctx: MT22Parser.Exp_list_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.exp())]
        else:
            return [self.visit(ctx.exp())] + self.visit(ctx.exp_list_prime())

    # exp_prime: exp | ;
    def visitExp_prime(self, ctx: MT22Parser.Exp_primeContext):
        if ctx.exp():
            return self.visit(ctx.exp())
        else:
            return None

    # exp: exp1 SCOPE exp1 | exp1 ;
    def visitExp(self, ctx: MT22Parser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0))
        else:
            return BinExpr(ctx.SCOPE().getText(), self.visit(ctx.exp1(0)), self.visit(ctx.exp1(1)))

    # exp1: exp2 relational_op exp2 | exp2 ;
    def visitExp1(self, ctx: MT22Parser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2(0))
        else:
            return BinExpr(self.visit(ctx.relational_op()), self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))

    # exp2: exp2 logical_op exp3 | exp3 ;
    def visitExp2(self, ctx: MT22Parser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        else:
            return BinExpr(self.visit(ctx.logical_op()), self.visit(ctx.exp2()), self.visit(ctx.exp3()))

    # exp3: exp3 adding_op exp4 | exp4 ;
    def visitExp3(self, ctx: MT22Parser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        else:
            return BinExpr(self.visit(ctx.adding_op()), self.visit(ctx.exp3()), self.visit(ctx.exp4()))

    # exp4: exp4 multiplying_op exp5 | exp5 ;
    def visitExp4(self, ctx: MT22Parser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        else:
            return BinExpr(self.visit(ctx.multiplying_op()), self.visit(ctx.exp4()), self.visit(ctx.exp5()))

    # exp5: LOG_NOT exp5 | exp6 ;
    def visitExp5(self, ctx: MT22Parser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        else:
            return UnExpr(ctx.LOG_NOT().getText(), self.visit(ctx.exp5()))

    # exp6: SUBOP exp6 | exp7 ;
    def visitExp6(self, ctx: MT22Parser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        else:
            return UnExpr(ctx.SUBOP().getText(), self.visit(ctx.exp6()))

    # exp7: IDENTIFIER indexop | exp8;
    def visitExp7(self, ctx: MT22Parser.Exp7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp8())
        else:
            return ArrayCell(ctx.IDENTIFIER().getText(), self.visit(ctx.indexop()))

    # exp8: LP exp RP | literal | IDENTIFIER | func_call | arraylit;
    def visitExp8(self, ctx: MT22Parser.Exp8Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.exp())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.func_call():
            return self.visit(ctx.func_call())
        else: # if ctx.arraylit():
            return self.visit(ctx.arraylit())
    
    ################################################################ Statements ##########################################################
    # assign_stmt: lhs ASSIGN exp SEMICOLON ;
    def visitAssign_stmt(self, ctx: MT22Parser.Assign_stmtContext):
        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.exp()))

    # lhs: IDENTIFIER indexop? ;
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if ctx.indexop():
            return ArrayCell(ctx.IDENTIFIER().getText(), self.visit(ctx.indexop()))
        else:
            return Id(ctx.IDENTIFIER().getText())
    
    # if_stmt: IF LP exp RP stmt (ELSE stmt)? ;
    def visitIf_stmt(self, ctx: MT22Parser.If_stmtContext):
        if len(ctx.stmt()) == 2:
            elstmt = self.visit(ctx.stmt(1))
        else:
            elstmt = None
        
        return IfStmt(self.visit(ctx.exp()), self.visit(ctx.stmt(0)), elstmt)

    # for_stmt: FOR LP <lhs> ASSIGN exp COMMA exp COMMA exp RP stmt ;
    def visitFor_stmt(self, ctx: MT22Parser.For_stmtContext):
        asstmt = AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.exp(0)))
        return ForStmt(asstmt, self.visit(ctx.exp(1)), self.visit(ctx.exp(2)), self.visit(ctx.stmt()))

    # while_stmt: WHILE LP exp RP stmt ;
    def visitWhile_stmt(self, ctx: MT22Parser.While_stmtContext):
        return WhileStmt(self.visit(ctx.exp()), self.visit(ctx.stmt()))

    # dowhile_stmt: DO block_stmt WHILE LP exp RP SEMICOLON;
    def visitDowhile_stmt(self, ctx: MT22Parser.Dowhile_stmtContext):
        return DoWhileStmt(self.visit(ctx.exp()), self.visit(ctx.block_stmt()))

    # cont_stmt: CONTINUE SEMICOLON ;
    def visitCont_stmt(self, ctx: MT22Parser.Cont_stmtContext):
        return ContinueStmt()

    # break_stmt: BREAK SEMICOLON ;
    def visitBreak_stmt(self, ctx: MT22Parser.Break_stmtContext):
        return BreakStmt()

    # return_stmt: RETURN exp_prime SEMICOLON ;
    def visitReturn_stmt(self, ctx: MT22Parser.Return_stmtContext):
        return ReturnStmt(self.visit(ctx.exp_prime()))

    # call_stmt: IDENTIFIER LP exp_list RP SEMICOLON ;
    def visitCall_stmt(self, ctx: MT22Parser.Call_stmtContext):
        return CallStmt(ctx.IDENTIFIER().getText(), self.visit(ctx.exp_list()))

    # block_stmt: LB stmt_list RB ;
    def visitBlock_stmt(self, ctx: MT22Parser.Block_stmtContext):
        return BlockStmt(self.visit(ctx.stmt_list()))

    # stmt_list: stmt_list_prime | ;
    def visitStmt_list(self, ctx: MT22Parser.Stmt_listContext):
        if ctx.stmt_list_prime():
            return self.visit(ctx.stmt_list_prime())
        else:
            return []

    # stmt_list_prime: stmt_content stmt_list_prime | stmt_content ;
    def visitStmt_list_prime(self, ctx: MT22Parser.Stmt_list_primeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.stmt_content())
        else:
            return self.visit(ctx.stmt_content()) + self.visit(ctx.stmt_list_prime())

    # stmt_content: stmt_list_content | vardecl ;
    def visitStmt_content(self, ctx: MT22Parser.Stmt_contentContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        else:
            return self.visit(ctx.stmt_list_content())
    
    # stmt_list_content: stmt COMMA stmt_list_content | stmt;
    def visitStmt_list_content(self, ctx: MT22Parser.Stmt_list_contentContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.stmt())]
        else:
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmt_list_content())

    # stmt: assign_stmt | if_stmt | for_stmt | while_stmt | dowhile_stmt | continue_stmt | break_stmt | cont_stmt | return_stmt | call_stmt | block_stmt ;
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        return self.visit(ctx.getChild(0))
    
    ################################################################ Types ###############################################################
    # func_call: IDENTIFIER LP exp_list RP
    def visitFunc_call(self, ctx: MT22Parser.Func_callContext):
        return FuncCall(ctx.IDENTIFIER().getText(), self.visit(ctx.exp_list()))
    
    # atomic_typ: INTEGER | FLOAT | STRING | BOOLEAN ;
    def visitAtomic_typ(self, ctx: MT22Parser.Atomic_typContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        else: # if ctx.BOOL():
            return BooleanType()
    
    # literal: INTLIT | FLOATLIT | STRINGLIT | boolit ; 
    def visitLiteral(self, ctx: MT22Parser.LiteralContext):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            num = "0" + str(ctx.FLOATLIT().getText())
            return FloatLit(float(num))
        elif ctx.STRINGLIT():
            return StringLit(str(ctx.STRINGLIT().getText()))
        else: # if ctx.BOOL():
            return self.visit(ctx.boolit())
    
    # boolit: TRUE | FALSE ;
    def visitBoolit(self, ctx: MT22Parser.BoolitContext):
        if ctx.TRUE():
            return BooleanLit(True)
        else: #if ctx.FALSE():
            return BooleanLit(False)