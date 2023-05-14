# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#program_decl.
    def visitProgram_decl(self, ctx:MT22Parser.Program_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#program_content.
    def visitProgram_content(self, ctx:MT22Parser.Program_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl_short.
    def visitVar_decl_short(self, ctx:MT22Parser.Var_decl_shortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_part.
    def visitVar_part(self, ctx:MT22Parser.Var_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_recur.
    def visitVar_recur(self, ctx:MT22Parser.Var_recurContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_list.
    def visitInit_list(self, ctx:MT22Parser.Init_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension.
    def visitDimension(self, ctx:MT22Parser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_list.
    def visitInt_list(self, ctx:MT22Parser.Int_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramdecl.
    def visitParamdecl(self, ctx:MT22Parser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_list.
    def visitParam_list(self, ctx:MT22Parser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param_list_prime.
    def visitParam_list_prime(self, ctx:MT22Parser.Param_list_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_call.
    def visitFunc_call(self, ctx:MT22Parser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_op.
    def visitRelational_op(self, ctx:MT22Parser.Relational_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_op.
    def visitLogical_op(self, ctx:MT22Parser.Logical_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#adding_op.
    def visitAdding_op(self, ctx:MT22Parser.Adding_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiplying_op.
    def visitMultiplying_op(self, ctx:MT22Parser.Multiplying_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexop.
    def visitIndexop(self, ctx:MT22Parser.IndexopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_list.
    def visitExp_list(self, ctx:MT22Parser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_list_prime.
    def visitExp_list_prime(self, ctx:MT22Parser.Exp_list_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_prime.
    def visitExp_prime(self, ctx:MT22Parser.Exp_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp.
    def visitExp(self, ctx:MT22Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp1.
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp2.
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp3.
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp4.
    def visitExp4(self, ctx:MT22Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp5.
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp6.
    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp7.
    def visitExp7(self, ctx:MT22Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp8.
    def visitExp8(self, ctx:MT22Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhile_stmt.
    def visitDowhile_stmt(self, ctx:MT22Parser.Dowhile_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#cont_stmt.
    def visitCont_stmt(self, ctx:MT22Parser.Cont_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt_list.
    def visitStmt_list(self, ctx:MT22Parser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt_list_prime.
    def visitStmt_list_prime(self, ctx:MT22Parser.Stmt_list_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt_content.
    def visitStmt_content(self, ctx:MT22Parser.Stmt_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt_list_content.
    def visitStmt_list_content(self, ctx:MT22Parser.Stmt_list_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolit.
    def visitBoolit(self, ctx:MT22Parser.BoolitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_typ.
    def visitAtomic_typ(self, ctx:MT22Parser.Atomic_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#literal.
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        return self.visitChildren(ctx)



del MT22Parser