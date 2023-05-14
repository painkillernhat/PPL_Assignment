import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_00(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_01(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_02(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_03(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_04(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_05(self):
        input = """
        print: function integer(n: auto) {
            printInteger(n);
        }
        """
        expect = """Program([
	FuncDecl(print, IntegerType, [Param(n, AutoType)], None, BlockStmt([CallStmt(printInteger, Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_06(self):
        input = """
        x: integer = 65;
        fact: function integer(n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_07(self):
        input = """main: function void() {
            if(n == 0) {
                break;
            }
            else {
                n = var - 1;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([BreakStmt()]), BlockStmt([AssignStmt(Id(n), BinExpr(-, Id(var), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_08(self):
        input = """x1, y1: auto;"""
        expect = """Program([
	VarDecl(x1, AutoType)
	VarDecl(y1, AutoType)
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_09(self):
        input = """decrem2: function void(inherit out a: integer) {
                while (a < 10) {
                    a = a - 1;
                }
            }"""
        expect = """Program([
	FuncDecl(decrem2, VoidType, [InheritOutParam(a, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(-, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_10(self):
        input = """foo1: function integer(x: integer, y: float) {
                return foo2(5, 3.1e10);
            }
            foo2: function float(x: float, y: integer) {
                return foo1(3.1e10, 5);
            }"""
        expect = """Program([
	FuncDecl(foo1, IntegerType, [Param(x, IntegerType), Param(y, FloatType)], None, BlockStmt([ReturnStmt(FuncCall(foo2, [IntegerLit(5), FloatLit(31000000000.0)]))]))
	FuncDecl(foo2, FloatType, [Param(x, FloatType), Param(y, IntegerType)], None, BlockStmt([ReturnStmt(FuncCall(foo1, [FloatLit(31000000000.0), IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_11(self):
        input = """arr1, arr2: array [2] of float = {1.9,2.3}, {3.6,4.7};"""
        expect = """Program([
	VarDecl(arr1, ArrayType([2], FloatType), ArrayLit([FloatLit(1.9), FloatLit(2.3)]))
	VarDecl(arr2, ArrayType([2], FloatType), ArrayLit([FloatLit(3.6), FloatLit(4.7)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_12(self):
        input = """checkop1: auto = 3 * 5 % 6 && 1 >= 0;"""
        expect = """Program([
	VarDecl(checkop1, AutoType, BinExpr(>=, BinExpr(&&, BinExpr(%, BinExpr(*, IntegerLit(3), IntegerLit(5)), IntegerLit(6)), IntegerLit(1)), IntegerLit(0)))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_13(self):
        input = """checkop3: boolean =  !true && !false || 11;"""
        expect = """Program([
	VarDecl(checkop3, BooleanType, BinExpr(||, BinExpr(&&, UnExpr(!, BooleanLit(True)), UnExpr(!, BooleanLit(False))), IntegerLit(11)))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_14(self):
        input = """goo: function void() {
                return arr[2::3];
            }"""
        expect = """Program([
	FuncDecl(goo, VoidType, [], None, BlockStmt([ReturnStmt(ArrayCell(arr, [BinExpr(::, IntegerLit(2), IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_15(self):
        input = """main: function void() {
            a[2+3] = {1,2,3,4,5};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(2), IntegerLit(3))]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_16(self):
        input = """checkop3: boolean =  !True && !False || 11;"""
        expect = """Program([
	VarDecl(checkop3, BooleanType, BinExpr(||, BinExpr(&&, UnExpr(!, Id(True)), UnExpr(!, Id(False))), IntegerLit(11)))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_17(self):
        input = """main: function void() {
                x = goo() + -goo();
            } """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, FuncCall(goo, []), UnExpr(-, FuncCall(goo, []))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_18(self):
        input = """
        main: function void() {
                while(a != 0) {
                    do {
                        a = a + 1;
                    }
                    while(a != 10);
                }
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(!=, Id(a), IntegerLit(0)), BlockStmt([DoWhileStmt(BinExpr(!=, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_19(self):
        input = """
       a: float;
            main: function void() {
                a = a + readFloat();
            }"""
        expect = """Program([
	VarDecl(a, FloatType)
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), FuncCall(readFloat, [])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_20(self):
        input = """foo: function integer(a: integer) {
                return foo(printInteger(a),b);
            }"""
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(a, IntegerType)], None, BlockStmt([ReturnStmt(FuncCall(foo, [FuncCall(printInteger, [Id(a)]), Id(b)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_21(self):
        input = """main: function void() {
                while((a != b) && (b != c) && (c!= 0)) {
                    
                }
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(&&, BinExpr(&&, BinExpr(!=, Id(a), Id(b)), BinExpr(!=, Id(b), Id(c))), BinExpr(!=, Id(c), IntegerLit(0))), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_22(self):
        input = """main: function void() {
                for(i = 0, (i < 10) && (i != a), i + 3) i = i + 1;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(&&, BinExpr(<, Id(i), IntegerLit(10)), BinExpr(!=, Id(i), Id(a))), BinExpr(+, Id(i), IntegerLit(3)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_23(self):
        input = """main: function void() {
                if (a != 10)
                    if (a != 9)
                        if (a != 8)
                            if (a != 7)
                                return a;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(!=, Id(a), IntegerLit(10)), IfStmt(BinExpr(!=, Id(a), IntegerLit(9)), IfStmt(BinExpr(!=, Id(a), IntegerLit(8)), IfStmt(BinExpr(!=, Id(a), IntegerLit(7)), ReturnStmt(Id(a))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_24(self):
        input = """main: function void() {
                a = (b == foo());
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(==, Id(b), FuncCall(foo, [])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_25(self):
        input = """main: function void() {
                for (a[0] = 0, a[0] < 10, a[0] + 1)
                    for (b = 0, b < 10, b + 1)
                        super(a[b] + b[a]);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [IntegerLit(0)]), IntegerLit(0)), BinExpr(<, ArrayCell(a, [IntegerLit(0)]), IntegerLit(10)), BinExpr(+, ArrayCell(a, [IntegerLit(0)]), IntegerLit(1)), ForStmt(AssignStmt(Id(b), IntegerLit(0)), BinExpr(<, Id(b), IntegerLit(10)), BinExpr(+, Id(b), IntegerLit(1)), CallStmt(super, BinExpr(+, ArrayCell(a, [Id(b)]), ArrayCell(b, [Id(a)])))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_26(self):
        input = """checkop4: boolean =  !0 || !11 || 1 || 11;"""
        expect = """Program([
	VarDecl(checkop4, BooleanType, BinExpr(||, BinExpr(||, BinExpr(||, UnExpr(!, IntegerLit(0)), UnExpr(!, IntegerLit(11))), IntegerLit(1)), IntegerLit(11)))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_27(self):
        input = """foo: function void(x: integer, inherit y: array [2] of float) {
                do {
                    a = 1;
                }
                while (a != 0);
            }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [Param(x, IntegerType), InheritParam(y, ArrayType([2], FloatType))], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), IntegerLit(1))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_28(self):
        input = """goo: function void() {
                return {1, "HCMUT", True};
            }"""
        expect = """Program([
	FuncDecl(goo, VoidType, [], None, BlockStmt([ReturnStmt(ArrayLit([IntegerLit(1), StringLit(HCMUT), Id(True)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_29(self):
        input = """goo: function void() {
                return arr[var1, var2, var3 + a[2,3]];
            }"""
        expect = """Program([
	FuncDecl(goo, VoidType, [], None, BlockStmt([ReturnStmt(ArrayCell(arr, [Id(var1), Id(var2), BinExpr(+, Id(var3), ArrayCell(a, [IntegerLit(2), IntegerLit(3)]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_30(self):
        input = """goo: function void() {
                return !0 || !11 || 1 || 11;
            }"""
        expect = """Program([
	FuncDecl(goo, VoidType, [], None, BlockStmt([ReturnStmt(BinExpr(||, BinExpr(||, BinExpr(||, UnExpr(!, IntegerLit(0)), UnExpr(!, IntegerLit(11))), IntegerLit(1)), IntegerLit(11)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_31(self):
        input = """goo: function void(a: array [2] of integer) {
                a[2] = {1,2};
                a = {1,2};
                return;
            }"""
        expect = """Program([
	FuncDecl(goo, VoidType, [Param(a, ArrayType([2], IntegerType))], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)])), AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2)])), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_32(self):
        input = """a: array [4,1] of boolean = {{}};"""
        expect = """Program([
	VarDecl(a, ArrayType([4, 1], BooleanType), ArrayLit([ArrayLit([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_33(self):
        input = """fact: function void(out a: integer) {
                /* do sth */
                {
                    // TODO
                }
            } """
        expect = """Program([
	FuncDecl(fact, VoidType, [OutParam(a, IntegerType)], None, BlockStmt([BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_34(self):
        input = """arr: array [2] of integer = -{1,2};"""
        expect = """Program([
	VarDecl(arr, ArrayType([2], IntegerType), UnExpr(-, ArrayLit([IntegerLit(1), IntegerLit(2)])))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_35(self):
        input = """main: float = main();"""
        expect = """Program([
	VarDecl(main, FloatType, FuncCall(main, []))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_36(self):
        input = """backtrack: function void(i: integer) {
            if (i >= m) {
                if (check()) {
                    res = min(res, cur);
                }
                return;
            }
            for (j = 0, j < 2, j+1) {
                flag[i] = j;
                cur = cur + j * e[i];
                backtrack(i + 1);
                cur = cur - j * e[i];
            }
        }"""
        expect = """Program([
	FuncDecl(backtrack, VoidType, [Param(i, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(i), Id(m)), BlockStmt([IfStmt(FuncCall(check, []), BlockStmt([AssignStmt(Id(res), FuncCall(min, [Id(res), Id(cur)]))])), ReturnStmt()])), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(2)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(flag, [Id(i)]), Id(j)), AssignStmt(Id(cur), BinExpr(+, Id(cur), BinExpr(*, Id(j), ArrayCell(e, [Id(i)])))), CallStmt(backtrack, BinExpr(+, Id(i), IntegerLit(1))), AssignStmt(Id(cur), BinExpr(-, Id(cur), BinExpr(*, Id(j), ArrayCell(e, [Id(i)]))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_37(self):
        input = """check: function boolean() {
            fill(vis + 1, vis + n + 1, false);
            dfs(node[1]);
            for (i = 1, i <= num_node, i + 1) {
                if (!vis[node[i]]) {
                    return false;
                }
            }
            return true;
        }"""
        expect = """Program([
	FuncDecl(check, BooleanType, [], None, BlockStmt([CallStmt(fill, BinExpr(+, Id(vis), IntegerLit(1)), BinExpr(+, BinExpr(+, Id(vis), Id(n)), IntegerLit(1)), BooleanLit(False)), CallStmt(dfs, ArrayCell(node, [IntegerLit(1)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(num_node)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(UnExpr(!, ArrayCell(vis, [ArrayCell(node, [Id(i)])])), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_38(self):
        input = """dfs: function void(inherit out u: integer) {
            vis[u] = true;
            for (i = adj[u], i >= 0, i - 1){ if (flag[i]) {
                v: integer = e[i] * get_v(u);
                if (vis[v]) {
                    continue;
                }
                dfs(v);
            }
            }
        }"""
        expect = """Program([
	FuncDecl(dfs, VoidType, [InheritOutParam(u, IntegerType)], None, BlockStmt([AssignStmt(ArrayCell(vis, [Id(u)]), BooleanLit(True)), ForStmt(AssignStmt(Id(i), ArrayCell(adj, [Id(u)])), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([IfStmt(ArrayCell(flag, [Id(i)]), BlockStmt([VarDecl(v, IntegerType, BinExpr(*, ArrayCell(e, [Id(i)]), FuncCall(get_v, [Id(u)]))), IfStmt(ArrayCell(vis, [Id(v)]), BlockStmt([ContinueStmt()])), CallStmt(dfs, Id(v))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_39(self):
        input = """main: function integer()
{
    m,n: integer;
    i,j,w: integer;
    host, temp: array [100] of integer;
    for (idx = 0, idx < n + 1, idx + 1) { push_back(0); temp_back(0);}
    for (idx = 2, idx < m + 2, idx + 1) {
        connect_t(i,j,w);
        data(t);
    }
    k: integer = 0;
    for (i = 0, i < k, i + 1){
        idx: integer;
        host[idx] = 1;
        temp[idx] = 1;
    }
    for (a = 0, a < size() - 1, a + 1) {
        connect_t(0, 0, 0);
        if (data[a] > data[a + 1]) {
            t = data[a];
            data[a] = data[a + 1];
            data[a + 1] = t;
        }
    }
    process(data, host, temp);
    return 0;
}"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(m, IntegerType), VarDecl(n, IntegerType), VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(w, IntegerType), VarDecl(host, ArrayType([100], IntegerType)), VarDecl(temp, ArrayType([100], IntegerType)), ForStmt(AssignStmt(Id(idx), IntegerLit(0)), BinExpr(<, Id(idx), BinExpr(+, Id(n), IntegerLit(1))), BinExpr(+, Id(idx), IntegerLit(1)), BlockStmt([CallStmt(push_back, IntegerLit(0)), CallStmt(temp_back, IntegerLit(0))])), ForStmt(AssignStmt(Id(idx), IntegerLit(2)), BinExpr(<, Id(idx), BinExpr(+, Id(m), IntegerLit(2))), BinExpr(+, Id(idx), IntegerLit(1)), BlockStmt([CallStmt(connect_t, Id(i), Id(j), Id(w)), CallStmt(data, Id(t))])), VarDecl(k, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(k)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(idx, IntegerType), AssignStmt(ArrayCell(host, [Id(idx)]), IntegerLit(1)), AssignStmt(ArrayCell(temp, [Id(idx)]), IntegerLit(1))])), ForStmt(AssignStmt(Id(a), IntegerLit(0)), BinExpr(<, Id(a), BinExpr(-, FuncCall(size, []), IntegerLit(1))), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([CallStmt(connect_t, IntegerLit(0), IntegerLit(0), IntegerLit(0)), IfStmt(BinExpr(>, ArrayCell(data, [Id(a)]), ArrayCell(data, [BinExpr(+, Id(a), IntegerLit(1))])), BlockStmt([AssignStmt(Id(t), ArrayCell(data, [Id(a)])), AssignStmt(ArrayCell(data, [Id(a)]), ArrayCell(data, [BinExpr(+, Id(a), IntegerLit(1))])), AssignStmt(ArrayCell(data, [BinExpr(+, Id(a), IntegerLit(1))]), Id(t))]))])), CallStmt(process, Id(data), Id(host), Id(temp)), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_40(self):
        input = """stop: function boolean(temp: array [100] of integer){
    sum: integer = 0;
    for (i = 0, i < size(), i + 1) sum = sum + temp[i];
    return sum == 0;
}
"""
        expect = """Program([
	FuncDecl(stop, BooleanType, [Param(temp, ArrayType([100], IntegerType))], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(size, [])), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(temp, [Id(i)])))), ReturnStmt(BinExpr(==, Id(sum), IntegerLit(0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_41(self):
        input = """process: function integer(data: array [100] of integer, host: array [100] of float, temp: array [100,100] of string) {
            sum: integer = 0;
    for (a = 0, a < size(), a + 1) {
        if (stop(temp)) break;
        i,j,w: integer = data[a] *i, data[a] *j, data[a] * w;
        //if (host[i] * host[j] == 0) continue;
        if (temp[i] + temp[j] == 0) continue;
        else {
            sum = sum + w;
            temp[i] = 0;
            temp[j] = 0;
        }
    }
    return sum;
}
"""
        expect = """Program([
	FuncDecl(process, IntegerType, [Param(data, ArrayType([100], IntegerType)), Param(host, ArrayType([100], FloatType)), Param(temp, ArrayType([100, 100], StringType))], None, BlockStmt([VarDecl(sum, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(a), IntegerLit(0)), BinExpr(<, Id(a), FuncCall(size, [])), BinExpr(+, Id(a), IntegerLit(1)), BlockStmt([IfStmt(FuncCall(stop, [Id(temp)]), BreakStmt()), VarDecl(i, IntegerType, BinExpr(*, ArrayCell(data, [Id(a)]), Id(i))), VarDecl(j, IntegerType, BinExpr(*, ArrayCell(data, [Id(a)]), Id(j))), VarDecl(w, IntegerType, BinExpr(*, ArrayCell(data, [Id(a)]), Id(w))), IfStmt(BinExpr(==, BinExpr(+, ArrayCell(temp, [Id(i)]), ArrayCell(temp, [Id(j)])), IntegerLit(0)), ContinueStmt(), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(w))), AssignStmt(ArrayCell(temp, [Id(i)]), IntegerLit(0)), AssignStmt(ArrayCell(temp, [Id(j)]), IntegerLit(0))]))])), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_42(self):
        input = """check: function boolean(s: string) {
    if(length() != 0) return false;
    for(i = 0, i < s::length(), i+1) {
        if(!((s[i] >= 0) && (s[i] <= 9))) return false;
    }
    return true;
}
count: function integer(ftime: string, etime: string) {
    start: integer = 3600*((ftime[0]-0)*10 +ftime[1]-0) + 60*((ftime[3]-0)*10 + ftime[4]-0) + (ftime[6]-0)*10 + ftime[7]-0;
    end: integer = 3600*((etime[0]-0)*10 +etime[1]-0) + 60*((etime[3]-0)*10 + etime[4]-0) + (etime[6]-0)*10 + etime[7]-0;
    return end - start;
}"""
        expect = """Program([
	FuncDecl(check, BooleanType, [Param(s, StringType)], None, BlockStmt([IfStmt(BinExpr(!=, FuncCall(length, []), IntegerLit(0)), ReturnStmt(BooleanLit(False))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(::, BinExpr(<, Id(i), Id(s)), FuncCall(length, [])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(UnExpr(!, BinExpr(&&, BinExpr(>=, ArrayCell(s, [Id(i)]), IntegerLit(0)), BinExpr(<=, ArrayCell(s, [Id(i)]), IntegerLit(9)))), ReturnStmt(BooleanLit(False)))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(count, IntegerType, [Param(ftime, StringType), Param(etime, StringType)], None, BlockStmt([VarDecl(start, IntegerType, BinExpr(-, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(*, IntegerLit(3600), BinExpr(-, BinExpr(+, BinExpr(*, BinExpr(-, ArrayCell(ftime, [IntegerLit(0)]), IntegerLit(0)), IntegerLit(10)), ArrayCell(ftime, [IntegerLit(1)])), IntegerLit(0))), BinExpr(*, IntegerLit(60), BinExpr(-, BinExpr(+, BinExpr(*, BinExpr(-, ArrayCell(ftime, [IntegerLit(3)]), IntegerLit(0)), IntegerLit(10)), ArrayCell(ftime, [IntegerLit(4)])), IntegerLit(0)))), BinExpr(*, BinExpr(-, ArrayCell(ftime, [IntegerLit(6)]), IntegerLit(0)), IntegerLit(10))), ArrayCell(ftime, [IntegerLit(7)])), IntegerLit(0))), VarDecl(end, IntegerType, BinExpr(-, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(*, IntegerLit(3600), BinExpr(-, BinExpr(+, BinExpr(*, BinExpr(-, ArrayCell(etime, [IntegerLit(0)]), IntegerLit(0)), IntegerLit(10)), ArrayCell(etime, [IntegerLit(1)])), IntegerLit(0))), BinExpr(*, IntegerLit(60), BinExpr(-, BinExpr(+, BinExpr(*, BinExpr(-, ArrayCell(etime, [IntegerLit(3)]), IntegerLit(0)), IntegerLit(10)), ArrayCell(etime, [IntegerLit(4)])), IntegerLit(0)))), BinExpr(*, BinExpr(-, ArrayCell(etime, [IntegerLit(6)]), IntegerLit(0)), IntegerLit(10))), ArrayCell(etime, [IntegerLit(7)])), IntegerLit(0))), ReturnStmt(BinExpr(-, Id(end), Id(start)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_43(self):
        input = """main: function integer()
{
    type: string;
    total, incorrect: integer = 0, 0;
    do {
        if(type == "#") continue;
        else {
            total = total + 1;
            fnum, tnum, date, ftime, etime: string;
            if((!check(fnum)) || (!check(tnum))) incorrect = incorrect + 1; 
            calls[fnum] = calls[fnum] + 1;
            time[fnum] = time[fnum] + count(ftime, etime);
        }
    }
    while(type != "#");
    
    check: integer = 0;
    do {
        if(type == "#") break;
        else{
            num: string;
            if(type == "?check_phone_number") {
                if(incorrect) return 1;
                else return 0;
            }
            if(type == "?number_calls_from") {
                printString(calls[num]);
            }
            if(type == "?number_total_calls") printInteger(total);
            if(type == "?count_time_calls_from") {
                return time[num];
            }
        }
    }
    while(type != "#");
    return 0;
}"""
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(type, StringType), VarDecl(total, IntegerType, IntegerLit(0)), VarDecl(incorrect, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(!=, Id(type), StringLit(#)), BlockStmt([IfStmt(BinExpr(==, Id(type), StringLit(#)), ContinueStmt(), BlockStmt([AssignStmt(Id(total), BinExpr(+, Id(total), IntegerLit(1))), VarDecl(fnum, StringType), VarDecl(tnum, StringType), VarDecl(date, StringType), VarDecl(ftime, StringType), VarDecl(etime, StringType), IfStmt(BinExpr(||, UnExpr(!, FuncCall(check, [Id(fnum)])), UnExpr(!, FuncCall(check, [Id(tnum)]))), AssignStmt(Id(incorrect), BinExpr(+, Id(incorrect), IntegerLit(1)))), AssignStmt(ArrayCell(calls, [Id(fnum)]), BinExpr(+, ArrayCell(calls, [Id(fnum)]), IntegerLit(1))), AssignStmt(ArrayCell(time, [Id(fnum)]), BinExpr(+, ArrayCell(time, [Id(fnum)]), FuncCall(count, [Id(ftime), Id(etime)])))]))])), VarDecl(check, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(!=, Id(type), StringLit(#)), BlockStmt([IfStmt(BinExpr(==, Id(type), StringLit(#)), BreakStmt(), BlockStmt([VarDecl(num, StringType), IfStmt(BinExpr(==, Id(type), StringLit(?check_phone_number)), BlockStmt([IfStmt(Id(incorrect), ReturnStmt(IntegerLit(1)), ReturnStmt(IntegerLit(0)))])), IfStmt(BinExpr(==, Id(type), StringLit(?number_calls_from)), BlockStmt([CallStmt(printString, ArrayCell(calls, [Id(num)]))])), IfStmt(BinExpr(==, Id(type), StringLit(?number_total_calls)), CallStmt(printInteger, Id(total))), IfStmt(BinExpr(==, Id(type), StringLit(?count_time_calls_from)), BlockStmt([ReturnStmt(ArrayCell(time, [Id(num)]))]))]))])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_44(self):
        input = """change: function string(input: string) {
    len: float = length();
    end: string = "";
    for(i = 0, i < len, i + 1) {
        if((input[i] >= 65) && (input[i] <= 90)) {
            end = end + input[i];
        }
        else {
            if(input[i] == "#") {
                if(i == len - 1) break;
                j: integer = i + 1;
                while((input[j] >= 65) && (input[j] <= 90)) {
                    end = end + input[j];
                    j = j + 1;
                }
            i = j - 1;
            }
        }

        if(input[i] == "@") {
            if(i == len) break;
            j: integer = i + 1;
            temp: string = "";
            while((input[j] != "#") && (input[j] != "@") && (input[j] != "\\n")) {
                temp = input[j] + temp;
                j = j + 1;
            }
            end = end + temp;
            i = j - 1;
        }
        else {
            break;
        }
    }
    return end;
}"""
        expect = """Program([
	FuncDecl(change, StringType, [Param(input, StringType)], None, BlockStmt([VarDecl(len, FloatType, FuncCall(length, [])), VarDecl(end, StringType, StringLit()), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(len)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>=, ArrayCell(input, [Id(i)]), IntegerLit(65)), BinExpr(<=, ArrayCell(input, [Id(i)]), IntegerLit(90))), BlockStmt([AssignStmt(Id(end), BinExpr(+, Id(end), ArrayCell(input, [Id(i)])))]), BlockStmt([IfStmt(BinExpr(==, ArrayCell(input, [Id(i)]), StringLit(#)), BlockStmt([IfStmt(BinExpr(==, Id(i), BinExpr(-, Id(len), IntegerLit(1))), BreakStmt()), VarDecl(j, IntegerType, BinExpr(+, Id(i), IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(>=, ArrayCell(input, [Id(j)]), IntegerLit(65)), BinExpr(<=, ArrayCell(input, [Id(j)]), IntegerLit(90))), BlockStmt([AssignStmt(Id(end), BinExpr(+, Id(end), ArrayCell(input, [Id(j)]))), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), AssignStmt(Id(i), BinExpr(-, Id(j), IntegerLit(1)))]))])), IfStmt(BinExpr(==, ArrayCell(input, [Id(i)]), StringLit(@)), BlockStmt([IfStmt(BinExpr(==, Id(i), Id(len)), BreakStmt()), VarDecl(j, IntegerType, BinExpr(+, Id(i), IntegerLit(1))), VarDecl(temp, StringType, StringLit()), WhileStmt(BinExpr(&&, BinExpr(&&, BinExpr(!=, ArrayCell(input, [Id(j)]), StringLit(#)), BinExpr(!=, ArrayCell(input, [Id(j)]), StringLit(@))), BinExpr(!=, ArrayCell(input, [Id(j)]), StringLit(\\n))), BlockStmt([AssignStmt(Id(temp), BinExpr(+, ArrayCell(input, [Id(j)]), Id(temp))), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), AssignStmt(Id(end), BinExpr(+, Id(end), Id(temp))), AssignStmt(Id(i), BinExpr(-, Id(j), IntegerLit(1)))]), BlockStmt([BreakStmt()]))])), ReturnStmt(Id(end))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_45(self):
        input = """countSearchRec: function integer (r: array [2,2] of integer, key: array [3,3,3] of integer) inherit SymbolTable
{
    if (!r)
    {
        return 0;
    }
    num_comp: integer = 1;
    if (compareData(r, _key) == -1)
    {
        num_comp = num_comp + 1;
        if (!r)
        {
            res: integer = num_comp;
            num_comp = 1;
            return res;
        }
        return countSearchRec(r, _key);
    }
    if (compareData(r, _key) == 1)
    {
        num_comp = num_comp + 1;
        if (!r)
        {
            res: integer = num_comp;
            num_comp = 1;
            return res;
        }
        return countSearchRec(r, _key);
    }
    res: integer = num_comp;
    num_comp = 1;
    return res;
}"""
        expect = """Program([
	FuncDecl(countSearchRec, IntegerType, [Param(r, ArrayType([2, 2], IntegerType)), Param(key, ArrayType([3, 3, 3], IntegerType))], SymbolTable, BlockStmt([IfStmt(UnExpr(!, Id(r)), BlockStmt([ReturnStmt(IntegerLit(0))])), VarDecl(num_comp, IntegerType, IntegerLit(1)), IfStmt(BinExpr(==, FuncCall(compareData, [Id(r), Id(_key)]), UnExpr(-, IntegerLit(1))), BlockStmt([AssignStmt(Id(num_comp), BinExpr(+, Id(num_comp), IntegerLit(1))), IfStmt(UnExpr(!, Id(r)), BlockStmt([VarDecl(res, IntegerType, Id(num_comp)), AssignStmt(Id(num_comp), IntegerLit(1)), ReturnStmt(Id(res))])), ReturnStmt(FuncCall(countSearchRec, [Id(r), Id(_key)]))])), IfStmt(BinExpr(==, FuncCall(compareData, [Id(r), Id(_key)]), IntegerLit(1)), BlockStmt([AssignStmt(Id(num_comp), BinExpr(+, Id(num_comp), IntegerLit(1))), IfStmt(UnExpr(!, Id(r)), BlockStmt([VarDecl(res, IntegerType, Id(num_comp)), AssignStmt(Id(num_comp), IntegerLit(1)), ReturnStmt(Id(res))])), ReturnStmt(FuncCall(countSearchRec, [Id(r), Id(_key)]))])), VarDecl(res, IntegerType, Id(num_comp)), AssignStmt(Id(num_comp), IntegerLit(1)), ReturnStmt(Id(res))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_46(self):
        input = """calculate: function void()
    {
        sum: float = 0;
        for (i = 0, i < 4, i + 1)
        {
            sum = sum + college_score[i]::assignment;
            sum = sum + college_score[i]::exam;
            sum = sum + college_score[i]::test;
        }
        average_score: float = sum * 1.0 / 12;
    }"""
        expect = """Program([
	FuncDecl(calculate, VoidType, [], None, BlockStmt([VarDecl(sum, FloatType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(::, BinExpr(+, Id(sum), ArrayCell(college_score, [Id(i)])), Id(assignment))), AssignStmt(Id(sum), BinExpr(::, BinExpr(+, Id(sum), ArrayCell(college_score, [Id(i)])), Id(exam))), AssignStmt(Id(sum), BinExpr(::, BinExpr(+, Id(sum), ArrayCell(college_score, [Id(i)])), Id(test)))])), VarDecl(average_score, FloatType, BinExpr(/, BinExpr(*, Id(sum), FloatLit(1.0)), IntegerLit(12)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_47(self):
        input = """  twoSum: function array [100] of integer(self: integer, nums: array [100] of integer, target: integer)
        {
        d = {};
        for (i=j, j < enumerate(nums), i+1){
            r = target - j;
            if (r <= d) return a[d[r], i];
            d[j] = i;
            }
        }"""
        expect = """Program([
	FuncDecl(twoSum, ArrayType([100], IntegerType), [Param(self, IntegerType), Param(nums, ArrayType([100], IntegerType)), Param(target, IntegerType)], None, BlockStmt([AssignStmt(Id(d), ArrayLit([])), ForStmt(AssignStmt(Id(i), Id(j)), BinExpr(<, Id(j), FuncCall(enumerate, [Id(nums)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(r), BinExpr(-, Id(target), Id(j))), IfStmt(BinExpr(<=, Id(r), Id(d)), ReturnStmt(ArrayCell(a, [ArrayCell(d, [Id(r)]), Id(i)]))), AssignStmt(ArrayCell(d, [Id(j)]), Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_48(self):
        input = """isPalindrome: function boolean(x: integer) {
       y: integer=x;
        if(x<0) return false;
            
        temp: integer=0;
        while(y)
        {
            temp=temp*10+y%10;
            y= y/10;
        }
        if(temp==x) return true;
        else return false;
     
    }"""
        expect = """Program([
	FuncDecl(isPalindrome, BooleanType, [Param(x, IntegerType)], None, BlockStmt([VarDecl(y, IntegerType, Id(x)), IfStmt(BinExpr(<, Id(x), IntegerLit(0)), ReturnStmt(BooleanLit(False))), VarDecl(temp, IntegerType, IntegerLit(0)), WhileStmt(Id(y), BlockStmt([AssignStmt(Id(temp), BinExpr(+, BinExpr(*, Id(temp), IntegerLit(10)), BinExpr(%, Id(y), IntegerLit(10)))), AssignStmt(Id(y), BinExpr(/, Id(y), IntegerLit(10)))])), IfStmt(BinExpr(==, Id(temp), Id(x)), ReturnStmt(BooleanLit(True)), ReturnStmt(BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_49(self):
        input = """romanToInt: function integer(s: string) {
        ans: integer=0;
        mp: array [7] of string = {"I","V","X","L","C","D","M"};

    for(i=0, i<size(), i+1){
        if(mp[s[i]] < mp[s[i+1]]){
            //for cases such as IV,CM, XL, etc...
            ans=ans-mp[s[i]];
        }
        else{
            ans=ans+mp[s[i]];
        }
    }
        return ans;
    }"""
        expect = """Program([
	FuncDecl(romanToInt, IntegerType, [Param(s, StringType)], None, BlockStmt([VarDecl(ans, IntegerType, IntegerLit(0)), VarDecl(mp, ArrayType([7], StringType), ArrayLit([StringLit(I), StringLit(V), StringLit(X), StringLit(L), StringLit(C), StringLit(D), StringLit(M)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(size, [])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(mp, [ArrayCell(s, [Id(i)])]), ArrayCell(mp, [ArrayCell(s, [BinExpr(+, Id(i), IntegerLit(1))])])), BlockStmt([AssignStmt(Id(ans), BinExpr(-, Id(ans), ArrayCell(mp, [ArrayCell(s, [Id(i)])])))]), BlockStmt([AssignStmt(Id(ans), BinExpr(+, Id(ans), ArrayCell(mp, [ArrayCell(s, [Id(i)])])))]))])), ReturnStmt(Id(ans))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_50(self):
        input = """romanToInt: function integer(s: string) {
        cnt: integer=0;
        m: array [100,100] of integer;
        m[1]=1;
        m[5]=5;
        m[10]=10;
        m[50]=50;
        m[100]=100;
        m[500]=500;
        m[1000]=1000;
        for(i=0, i<size(), i+1) {
            if(i!=size()-1){
                if(m[s[i]]<m[s[i+1]]){
                    cnt= cnt - m[s[i]];
                }
                else{
                    cnt= cnt + m[s[i]];
                }
            }
            else{
                cnt= cnt + m[s[i]];
            }
        }
        return cnt;
    }"""
        expect = """Program([
	FuncDecl(romanToInt, IntegerType, [Param(s, StringType)], None, BlockStmt([VarDecl(cnt, IntegerType, IntegerLit(0)), VarDecl(m, ArrayType([100, 100], IntegerType)), AssignStmt(ArrayCell(m, [IntegerLit(1)]), IntegerLit(1)), AssignStmt(ArrayCell(m, [IntegerLit(5)]), IntegerLit(5)), AssignStmt(ArrayCell(m, [IntegerLit(10)]), IntegerLit(10)), AssignStmt(ArrayCell(m, [IntegerLit(50)]), IntegerLit(50)), AssignStmt(ArrayCell(m, [IntegerLit(100)]), IntegerLit(100)), AssignStmt(ArrayCell(m, [IntegerLit(500)]), IntegerLit(500)), AssignStmt(ArrayCell(m, [IntegerLit(1000)]), IntegerLit(1000)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(size, [])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, Id(i), BinExpr(-, FuncCall(size, []), IntegerLit(1))), BlockStmt([IfStmt(BinExpr(<, ArrayCell(m, [ArrayCell(s, [Id(i)])]), ArrayCell(m, [ArrayCell(s, [BinExpr(+, Id(i), IntegerLit(1))])])), BlockStmt([AssignStmt(Id(cnt), BinExpr(-, Id(cnt), ArrayCell(m, [ArrayCell(s, [Id(i)])])))]), BlockStmt([AssignStmt(Id(cnt), BinExpr(+, Id(cnt), ArrayCell(m, [ArrayCell(s, [Id(i)])])))]))]), BlockStmt([AssignStmt(Id(cnt), BinExpr(+, Id(cnt), ArrayCell(m, [ArrayCell(s, [Id(i)])])))]))])), ReturnStmt(Id(cnt))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_51(self):
        input = """a: integer = --foo();"""
        expect = """Program([
	VarDecl(a, IntegerType, UnExpr(-, UnExpr(-, FuncCall(foo, []))))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_52(self):
        input = """main: function void() {
                a = {1,3} - 1.2;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, ArrayLit([IntegerLit(1), IntegerLit(3)]), FloatLit(1.2)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_53(self):
        input = """a: integer = (3 >= 4) || (1 <= 2);"""
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(||, BinExpr(>=, IntegerLit(3), IntegerLit(4)), BinExpr(<=, IntegerLit(1), IntegerLit(2))))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_54(self):
        input = """ main: function void() {
                while(a != 0)
                    do {a = 1;}
                    while (a != 10);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(!=, Id(a), IntegerLit(0)), DoWhileStmt(BinExpr(!=, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), IntegerLit(1))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_55(self):
        input = """main: function void() {
                a: string = "ab" + "c";
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, BinExpr(+, StringLit(ab), StringLit(c)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_56(self):
        input = """ main: function void() {
                _ = _ <= _;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(_), BinExpr(<=, Id(_), Id(_)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_57(self):
        input = """main: function void() {
                while(a + b != 10)
                    a = a + 1;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(!=, BinExpr(+, Id(a), Id(b)), IntegerLit(10)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_58(self):
        input = """main: function void() {
                readinteger();
                readinteger();
                readinteger();
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(readinteger, ), CallStmt(readinteger, ), CallStmt(readinteger, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_59(self):
        input = """longestCommonPrefix: function string(strs: array [100] of string) {
        sort(begin(), end());
        a: integer=size();
        n: string=strs[0]; m = strs[a-1]; ans: string = "";
        for(i=0, i<size(), i+1){
            if(n[i]==m[i]) {ans = ans + n[i];}
            else break;
        }
        return ans;
        
    }"""
        expect = """Program([
	FuncDecl(longestCommonPrefix, StringType, [Param(strs, ArrayType([100], StringType))], None, BlockStmt([CallStmt(sort, FuncCall(begin, []), FuncCall(end, [])), VarDecl(a, IntegerType, FuncCall(size, [])), VarDecl(n, StringType, ArrayCell(strs, [IntegerLit(0)])), AssignStmt(Id(m), ArrayCell(strs, [BinExpr(-, Id(a), IntegerLit(1))])), VarDecl(ans, StringType, StringLit()), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(size, [])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(n, [Id(i)]), ArrayCell(m, [Id(i)])), BlockStmt([AssignStmt(Id(ans), BinExpr(+, Id(ans), ArrayCell(n, [Id(i)])))]), BreakStmt())])), ReturnStmt(Id(ans))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_60(self):
        input = """ longestCommonPrefix: function string(strs: array [100] of string) {
        ans: integer = s[0] * length(); n = size();
        for(i=1, i<n, i % 10){
            j: integer = 0;
            while(j < s[i] * length() && (s[i,j] == s[0,j])) j = j + 1;
            ans = min(ans, j);
        }
        return s[0] * substr(0, ans);
    }"""
        expect = """Program([
	FuncDecl(longestCommonPrefix, StringType, [Param(strs, ArrayType([100], StringType))], None, BlockStmt([VarDecl(ans, IntegerType, BinExpr(*, ArrayCell(s, [IntegerLit(0)]), FuncCall(length, []))), AssignStmt(Id(n), FuncCall(size, [])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(%, Id(i), IntegerLit(10)), BlockStmt([VarDecl(j, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, Id(j), BinExpr(&&, BinExpr(*, ArrayCell(s, [Id(i)]), FuncCall(length, [])), BinExpr(==, ArrayCell(s, [Id(i), Id(j)]), ArrayCell(s, [IntegerLit(0), Id(j)])))), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))), AssignStmt(Id(ans), FuncCall(min, [Id(ans), Id(j)]))])), ReturnStmt(BinExpr(*, ArrayCell(s, [IntegerLit(0)]), FuncCall(substr, [IntegerLit(0), Id(ans)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_61(self):
        input = """ longestCommonPrefix: function string(strs: array [100] of string) {
    // sort the array because its rearrange alphabetical order
   sort();


  for (i = 0, i < strs[0]::length, i % 10) {
    if (strs[0,i] != strs[strs::length - 1,i]){
return strs[0]::substr(0, i);
    } 
  }

  return strs[0];  
}"""
        expect = """Program([
	FuncDecl(longestCommonPrefix, StringType, [Param(strs, ArrayType([100], StringType))], None, BlockStmt([CallStmt(sort, ), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(::, BinExpr(<, Id(i), ArrayCell(strs, [IntegerLit(0)])), Id(length)), BinExpr(%, Id(i), IntegerLit(10)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(strs, [IntegerLit(0), Id(i)]), ArrayCell(strs, [BinExpr(::, Id(strs), BinExpr(-, Id(length), IntegerLit(1))), Id(i)])), BlockStmt([ReturnStmt(BinExpr(::, ArrayCell(strs, [IntegerLit(0)]), FuncCall(substr, [IntegerLit(0), Id(i)])))]))])), ReturnStmt(ArrayCell(strs, [IntegerLit(0)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_62(self):
        input = """removeElement: function integer(nums: array [100] of integer, val: integer) {
        j: integer=0;
        for(nums[i]=0, nums[i]< nums::size(), nums[i] + 1){
            if(nums[i]!=val){
                nums[j+1]=nums[i];
            }
        }
        return j;        
    }"""
        expect = """Program([
	FuncDecl(removeElement, IntegerType, [Param(nums, ArrayType([100], IntegerType)), Param(val, IntegerType)], None, BlockStmt([VarDecl(j, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(ArrayCell(nums, [Id(i)]), IntegerLit(0)), BinExpr(::, BinExpr(<, ArrayCell(nums, [Id(i)]), Id(nums)), FuncCall(size, [])), BinExpr(+, ArrayCell(nums, [Id(i)]), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(nums, [Id(i)]), Id(val)), BlockStmt([AssignStmt(ArrayCell(nums, [BinExpr(+, Id(j), IntegerLit(1))]), ArrayCell(nums, [Id(i)]))]))])), ReturnStmt(Id(j))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_63(self):
        input = """removeElement: function integer(nums: array [100] of integer, val: integer) {
    j: integer = 0; 
    while(x % v){
        if(x!=val){
            v[j]=x;
            j = j + 1;
        }
    }
    return j;
}  """
        expect = """Program([
	FuncDecl(removeElement, IntegerType, [Param(nums, ArrayType([100], IntegerType)), Param(val, IntegerType)], None, BlockStmt([VarDecl(j, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(%, Id(x), Id(v)), BlockStmt([IfStmt(BinExpr(!=, Id(x), Id(val)), BlockStmt([AssignStmt(ArrayCell(v, [Id(j)]), Id(x)), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))]))])), ReturnStmt(Id(j))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_64(self):
        input = """searchInsert: function integer(nums: array [100] of integer, x: integer) {
        if(x<=nums[0]) return 0;
        if(nums[nums::size()-1] < x){ return nums::size();
        } if(nums[nums::size()-1]==x){ return nums::size()-1;
        }
        i,j: integer = 0, nums::size()-1;
        while(i<=j){
            mid = (j-i)/2+i;
            if(nums[(mid-1)%nums::size()]<x 
                && (nums[mid]>=x)) {
                return mid;
            }else { if(nums[mid]>x){
                j = mid-1;
            }else{
                i = mid+1;
            }
            }
        }
        return i;
    }"""
        expect = """Program([
	FuncDecl(searchInsert, IntegerType, [Param(nums, ArrayType([100], IntegerType)), Param(x, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(x), ArrayCell(nums, [IntegerLit(0)])), ReturnStmt(IntegerLit(0))), IfStmt(BinExpr(<, ArrayCell(nums, [BinExpr(::, Id(nums), BinExpr(-, FuncCall(size, []), IntegerLit(1)))]), Id(x)), BlockStmt([ReturnStmt(BinExpr(::, Id(nums), FuncCall(size, [])))])), IfStmt(BinExpr(==, ArrayCell(nums, [BinExpr(::, Id(nums), BinExpr(-, FuncCall(size, []), IntegerLit(1)))]), Id(x)), BlockStmt([ReturnStmt(BinExpr(::, Id(nums), BinExpr(-, FuncCall(size, []), IntegerLit(1))))])), VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(j, IntegerType, BinExpr(::, Id(nums), BinExpr(-, FuncCall(size, []), IntegerLit(1)))), WhileStmt(BinExpr(<=, Id(i), Id(j)), BlockStmt([AssignStmt(Id(mid), BinExpr(+, BinExpr(/, BinExpr(-, Id(j), Id(i)), IntegerLit(2)), Id(i))), IfStmt(BinExpr(<, ArrayCell(nums, [BinExpr(::, BinExpr(%, BinExpr(-, Id(mid), IntegerLit(1)), Id(nums)), FuncCall(size, []))]), BinExpr(&&, Id(x), BinExpr(>=, ArrayCell(nums, [Id(mid)]), Id(x)))), BlockStmt([ReturnStmt(Id(mid))]), BlockStmt([IfStmt(BinExpr(>, ArrayCell(nums, [Id(mid)]), Id(x)), BlockStmt([AssignStmt(Id(j), BinExpr(-, Id(mid), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(mid), IntegerLit(1)))]))]))])), ReturnStmt(Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_65(self):
        input = """searchInsert: function integer(nums: array [100] of integer, x: integer) {
     
       hi, lo: integer = nums::size()-1, 0;
       while(hi >= lo)
       {
         mid: float = (hi + lo)/2;

         if(nums[mid]==target) return mid;
    
         else {if(nums[mid] > target) hi = mid - 1;
         
         else lo = mid + 1;
         }
       }

      return lo;
    }"""
        expect = """Program([
	FuncDecl(searchInsert, IntegerType, [Param(nums, ArrayType([100], IntegerType)), Param(x, IntegerType)], None, BlockStmt([VarDecl(hi, IntegerType, BinExpr(::, Id(nums), BinExpr(-, FuncCall(size, []), IntegerLit(1)))), VarDecl(lo, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(>=, Id(hi), Id(lo)), BlockStmt([VarDecl(mid, FloatType, BinExpr(/, BinExpr(+, Id(hi), Id(lo)), IntegerLit(2))), IfStmt(BinExpr(==, ArrayCell(nums, [Id(mid)]), Id(target)), ReturnStmt(Id(mid)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(nums, [Id(mid)]), Id(target)), AssignStmt(Id(hi), BinExpr(-, Id(mid), IntegerLit(1))), AssignStmt(Id(lo), BinExpr(+, Id(mid), IntegerLit(1))))]))])), ReturnStmt(Id(lo))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_66(self):
        input = """safeRow: function boolean(board: array [100] of integer, row: integer, col: integer, num: string)
{
for (i = 0, i < 9, i+1)
{
if (board[i,col] == num && (i != row))
{
return false;
}
}
return true;
}
safeCol: function boolean(board: array [100] of integer, row: integer, col: integer, num: string)
{
for (i = 0, i < 9, i+1)
{
if (board[row,i] == num && (i != col))
{
return false;
}
}
return true;
}
safeGrid: function boolean(board: array [100] of integer, row: integer, col: integer, num: string)
{
rowfact: integer = row - row % 3;
colfact: integer = col - col % 3;
for (i = 0, i < 3, i+1)
{
for (j = 0, j < 3, j+1)
{
r, c: integer = i + (row - row % 3), j + (col - col % 3);
if (board[r,c] == num && (r != row) && (c != col))
{
return false;
}
}
}
return true;
}"""
        expect = """Program([
	FuncDecl(safeRow, BooleanType, [Param(board, ArrayType([100], IntegerType)), Param(row, IntegerType), Param(col, IntegerType), Param(num, StringType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(9)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(board, [Id(i), Id(col)]), BinExpr(&&, Id(num), BinExpr(!=, Id(i), Id(row)))), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(safeCol, BooleanType, [Param(board, ArrayType([100], IntegerType)), Param(row, IntegerType), Param(col, IntegerType), Param(num, StringType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(9)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(board, [Id(row), Id(i)]), BinExpr(&&, Id(num), BinExpr(!=, Id(i), Id(col)))), BlockStmt([ReturnStmt(BooleanLit(False))]))])), ReturnStmt(BooleanLit(True))]))
	FuncDecl(safeGrid, BooleanType, [Param(board, ArrayType([100], IntegerType)), Param(row, IntegerType), Param(col, IntegerType), Param(num, StringType)], None, BlockStmt([VarDecl(rowfact, IntegerType, BinExpr(-, Id(row), BinExpr(%, Id(row), IntegerLit(3)))), VarDecl(colfact, IntegerType, BinExpr(-, Id(col), BinExpr(%, Id(col), IntegerLit(3)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(3)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([VarDecl(r, IntegerType, BinExpr(+, Id(i), BinExpr(-, Id(row), BinExpr(%, Id(row), IntegerLit(3))))), VarDecl(c, IntegerType, BinExpr(+, Id(j), BinExpr(-, Id(col), BinExpr(%, Id(col), IntegerLit(3))))), IfStmt(BinExpr(==, ArrayCell(board, [Id(r), Id(c)]), BinExpr(&&, BinExpr(&&, Id(num), BinExpr(!=, Id(r), Id(row))), BinExpr(!=, Id(c), Id(col)))), BlockStmt([ReturnStmt(BooleanLit(False))]))]))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_67(self):
        input = """isValidSudoku: function boolean(self: integer, board: array [100] of integer){
        res = {};
        while( i < range(9)){
            while(j < range(9)) {
                element = board[i,j];
                if (element != ".")
                    res = res + {{i, element}, {element, j}, {i % 3, j % 3, element}};
            }
        }
                
        return len(res) == len(set(res));}"""
        expect = """Program([
	FuncDecl(isValidSudoku, BooleanType, [Param(self, IntegerType), Param(board, ArrayType([100], IntegerType))], None, BlockStmt([AssignStmt(Id(res), ArrayLit([])), WhileStmt(BinExpr(<, Id(i), FuncCall(range, [IntegerLit(9)])), BlockStmt([WhileStmt(BinExpr(<, Id(j), FuncCall(range, [IntegerLit(9)])), BlockStmt([AssignStmt(Id(element), ArrayCell(board, [Id(i), Id(j)])), IfStmt(BinExpr(!=, Id(element), StringLit(.)), AssignStmt(Id(res), BinExpr(+, Id(res), ArrayLit([ArrayLit([Id(i), Id(element)]), ArrayLit([Id(element), Id(j)]), ArrayLit([BinExpr(%, Id(i), IntegerLit(3)), BinExpr(%, Id(j), IntegerLit(3)), Id(element)])]))))]))])), ReturnStmt(BinExpr(==, FuncCall(len, [Id(res)]), FuncCall(len, [FuncCall(set, [Id(res)])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_68(self):
        input = """  power: function float(x: float, n: integer){
        if(n==0){
            return 1;
        }
        return x * power(x, n-1);
    }
    myPow: function float(x: float, n: integer) inherit power{
        if (n == INT_MAX) return (x == 1) && -1;
        if (n == INT_MIN) return (x == 1 || (x == -1)) && 1;
        num: float = 1;
        if(n>=0){
            num = power(x, n);
        }
        else{
            n = -n;
            num = power(x, n);
            num = 1.e20/num;
        }
        return num;
    }"""
        expect = """Program([
	FuncDecl(power, FloatType, [Param(x, FloatType), Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(IntegerLit(1))])), ReturnStmt(BinExpr(*, Id(x), FuncCall(power, [Id(x), BinExpr(-, Id(n), IntegerLit(1))])))]))
	FuncDecl(myPow, FloatType, [Param(x, FloatType), Param(n, IntegerType)], power, BlockStmt([IfStmt(BinExpr(==, Id(n), Id(INT_MAX)), ReturnStmt(BinExpr(&&, BinExpr(==, Id(x), IntegerLit(1)), UnExpr(-, IntegerLit(1))))), IfStmt(BinExpr(==, Id(n), Id(INT_MIN)), ReturnStmt(BinExpr(&&, BinExpr(==, Id(x), BinExpr(||, IntegerLit(1), BinExpr(==, Id(x), UnExpr(-, IntegerLit(1))))), IntegerLit(1)))), VarDecl(num, FloatType, IntegerLit(1)), IfStmt(BinExpr(>=, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(num), FuncCall(power, [Id(x), Id(n)]))]), BlockStmt([AssignStmt(Id(n), UnExpr(-, Id(n))), AssignStmt(Id(num), FuncCall(power, [Id(x), Id(n)])), AssignStmt(Id(num), BinExpr(/, FloatLit(1e+20), Id(num)))])), ReturnStmt(Id(num))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_69(self):
        input = """ myPow: function float(x: float, n: integer) {
        if(n==0) return 1;
        if(n<0) {
            n = abs(n);
            x = 1/x;
        }
        if(n%2==0){
            return myPow(x*x, n/2);
        }
        else{
            return x*myPow(x, n-1);
        }
    }"""
        expect = """Program([
	FuncDecl(myPow, FloatType, [Param(x, FloatType), Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1))), IfStmt(BinExpr(<, Id(n), IntegerLit(0)), BlockStmt([AssignStmt(Id(n), FuncCall(abs, [Id(n)])), AssignStmt(Id(x), BinExpr(/, IntegerLit(1), Id(x)))])), IfStmt(BinExpr(==, BinExpr(%, Id(n), IntegerLit(2)), IntegerLit(0)), BlockStmt([ReturnStmt(FuncCall(myPow, [BinExpr(*, Id(x), Id(x)), BinExpr(/, Id(n), IntegerLit(2))]))]), BlockStmt([ReturnStmt(BinExpr(*, Id(x), FuncCall(myPow, [Id(x), BinExpr(-, Id(n), IntegerLit(1))])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_70(self):
        input = """myPow: function float(x: float, n: integer) {
    if (n == 0) {
        return 1.0;
    }
    res: float = 1.0;
    p: integer = abs(n);
    while (p > 0) {
        if (p % 2 == 1) {
            res = res * x;
        }
        x = x * x;
        p = p/ 2;
    }
    if (n < 0) {
        return 1.0 / res;
    } else {
        return res;
    }
}"""
        expect = """Program([
	FuncDecl(myPow, FloatType, [Param(x, FloatType), Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(FloatLit(1.0))])), VarDecl(res, FloatType, FloatLit(1.0)), VarDecl(p, IntegerType, FuncCall(abs, [Id(n)])), WhileStmt(BinExpr(>, Id(p), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(p), IntegerLit(2)), IntegerLit(1)), BlockStmt([AssignStmt(Id(res), BinExpr(*, Id(res), Id(x)))])), AssignStmt(Id(x), BinExpr(*, Id(x), Id(x))), AssignStmt(Id(p), BinExpr(/, Id(p), IntegerLit(2)))])), IfStmt(BinExpr(<, Id(n), IntegerLit(0)), BlockStmt([ReturnStmt(BinExpr(/, FloatLit(1.0), Id(res)))]), BlockStmt([ReturnStmt(Id(res))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_71(self):
        input = """multiply: function string(num1: string, out num2: string) {
        if (num1 == "0" || (num2 == "0")) return "0";
        
        res: array [100] of integer = {size()+num2::size(), 0};
        
        for (i = num1::size()-1, i >= 0, i-1) {
            for (j = num2::size()-1, j >= 0, j-1) {
                res[i + j + 1] =res[i + j + 1]+ (num1[i]-"0") * (num2[j]-"0");
                res[i + j] = res[i + j]+ res[i + j + 1] / 10;
                res[i + j + 1] = res[i + j + 1] % 10;
            }
        }
        
        i: auto = 0;
        ans: auto = "";
        while (res[i] == 0) i = i + 1;
        while (i < res::size()) ans = ans + to_string(res[i+1]);
        
        return ans;
    }"""
        expect = """Program([
	FuncDecl(multiply, StringType, [Param(num1, StringType), OutParam(num2, StringType)], None, BlockStmt([IfStmt(BinExpr(==, Id(num1), BinExpr(||, StringLit(0), BinExpr(==, Id(num2), StringLit(0)))), ReturnStmt(StringLit(0))), VarDecl(res, ArrayType([100], IntegerType), ArrayLit([BinExpr(::, BinExpr(+, FuncCall(size, []), Id(num2)), FuncCall(size, [])), IntegerLit(0)])), ForStmt(AssignStmt(Id(i), BinExpr(::, Id(num1), BinExpr(-, FuncCall(size, []), IntegerLit(1)))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(::, Id(num2), BinExpr(-, FuncCall(size, []), IntegerLit(1)))), BinExpr(>=, Id(j), IntegerLit(0)), BinExpr(-, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(res, [BinExpr(+, BinExpr(+, Id(i), Id(j)), IntegerLit(1))]), BinExpr(+, ArrayCell(res, [BinExpr(+, BinExpr(+, Id(i), Id(j)), IntegerLit(1))]), BinExpr(*, BinExpr(-, ArrayCell(num1, [Id(i)]), StringLit(0)), BinExpr(-, ArrayCell(num2, [Id(j)]), StringLit(0))))), AssignStmt(ArrayCell(res, [BinExpr(+, Id(i), Id(j))]), BinExpr(+, ArrayCell(res, [BinExpr(+, Id(i), Id(j))]), BinExpr(/, ArrayCell(res, [BinExpr(+, BinExpr(+, Id(i), Id(j)), IntegerLit(1))]), IntegerLit(10)))), AssignStmt(ArrayCell(res, [BinExpr(+, BinExpr(+, Id(i), Id(j)), IntegerLit(1))]), BinExpr(%, ArrayCell(res, [BinExpr(+, BinExpr(+, Id(i), Id(j)), IntegerLit(1))]), IntegerLit(10)))]))])), VarDecl(i, AutoType, IntegerLit(0)), VarDecl(ans, AutoType, StringLit()), WhileStmt(BinExpr(==, ArrayCell(res, [Id(i)]), IntegerLit(0)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))), WhileStmt(BinExpr(::, BinExpr(<, Id(i), Id(res)), FuncCall(size, [])), AssignStmt(Id(ans), BinExpr(+, Id(ans), FuncCall(to_string, [ArrayCell(res, [BinExpr(+, Id(i), IntegerLit(1))])])))), ReturnStmt(Id(ans))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_72(self):
        input = """reverse: function integer(inherit x: integer) {
        r: integer=0;      // decleare r 
        while(x){
         r=r*10+x%10; // find remainder and add its to r
         x=x/10;     // Update the value of x
        }
        if(r>INT_MAX || (r<INT_MIN)) return 0; // check 32 bit range if r is outside the range then return 0  
        return int(r);  // if r in the 32 bit range return r
    }"""
        expect = """Program([
	FuncDecl(reverse, IntegerType, [InheritParam(x, IntegerType)], None, BlockStmt([VarDecl(r, IntegerType, IntegerLit(0)), WhileStmt(Id(x), BlockStmt([AssignStmt(Id(r), BinExpr(+, BinExpr(*, Id(r), IntegerLit(10)), BinExpr(%, Id(x), IntegerLit(10)))), AssignStmt(Id(x), BinExpr(/, Id(x), IntegerLit(10)))])), IfStmt(BinExpr(>, Id(r), BinExpr(||, Id(INT_MAX), BinExpr(<, Id(r), Id(INT_MIN)))), ReturnStmt(IntegerLit(0))), ReturnStmt(FuncCall(int, [Id(r)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_73(self):
        input = """reverse: function integer(self: integer, x: integer){
        if (x < 0){
            sign = -1;
            x = -x;
        }
        else{
            sign = 1;
        }
        // Convert integer to string, reverse it, and convert back to integer
        reversed_x = int(str(x[0::-1]));

        /* Check if reversed integer is outside range of signed 32-bit integer */

        if (reversed_x > 2*31 - 1) return 0;
            
        // Restore the sign of the reversed integer
        return sign * reversed_x; }"""
        expect = """Program([
	FuncDecl(reverse, IntegerType, [Param(self, IntegerType), Param(x, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(x), IntegerLit(0)), BlockStmt([AssignStmt(Id(sign), UnExpr(-, IntegerLit(1))), AssignStmt(Id(x), UnExpr(-, Id(x)))]), BlockStmt([AssignStmt(Id(sign), IntegerLit(1))])), AssignStmt(Id(reversed_x), FuncCall(int, [FuncCall(str, [ArrayCell(x, [BinExpr(::, IntegerLit(0), UnExpr(-, IntegerLit(1)))])])])), IfStmt(BinExpr(>, Id(reversed_x), BinExpr(-, BinExpr(*, IntegerLit(2), IntegerLit(31)), IntegerLit(1))), ReturnStmt(IntegerLit(0))), ReturnStmt(BinExpr(*, Id(sign), Id(reversed_x)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_74(self):
        input = """myAtoi: function integer(s: string) {
       str, minus, flag, i: auto = "", 1, 0, 0;
       while(s[i] == " ") i = i + 1; //removing all spaces
       if(s[i] == "-" || (s[i] == "+")){
          if(s[i] == "-") minus = -1;
           i = i + 1;
       }//seeing weather the number is pos or neg
    
       for(i=0, i<length(), i+1){
          if(s[i] >= 48 && (s[i] <= 57)) {
            str = str + s[i];
          }
          else continue;
       }
       if(length() == 0) return 0;
    }"""
        expect = """Program([
	FuncDecl(myAtoi, IntegerType, [Param(s, StringType)], None, BlockStmt([VarDecl(str, AutoType, StringLit()), VarDecl(minus, AutoType, IntegerLit(1)), VarDecl(flag, AutoType, IntegerLit(0)), VarDecl(i, AutoType, IntegerLit(0)), WhileStmt(BinExpr(==, ArrayCell(s, [Id(i)]), StringLit( )), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))), IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), BinExpr(||, StringLit(-), BinExpr(==, ArrayCell(s, [Id(i)]), StringLit(+)))), BlockStmt([IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), StringLit(-)), AssignStmt(Id(minus), UnExpr(-, IntegerLit(1)))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(length, [])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>=, ArrayCell(s, [Id(i)]), BinExpr(&&, IntegerLit(48), BinExpr(<=, ArrayCell(s, [Id(i)]), IntegerLit(57)))), BlockStmt([AssignStmt(Id(str), BinExpr(+, Id(str), ArrayCell(s, [Id(i)])))]), ContinueStmt())])), IfStmt(BinExpr(==, FuncCall(length, []), IntegerLit(0)), ReturnStmt(IntegerLit(0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_75(self):
        input = """  myAtoi: function integer(s: string) {
        len, num, i: auto = s::size(), 0.0, 0;
        while(s[i] == " "){
            i = i + 1;
        }
        positive, negative: boolean = (s[i] == "+"), (s[i] == "-");
        while(i < len && (s[i] >= "0") && (s[i] <= "9")){
            num = num*10 + (s[i]-"0");
            i = i + 1;
        }
        
        return int(num);
    }"""
        expect = """Program([
	FuncDecl(myAtoi, IntegerType, [Param(s, StringType)], None, BlockStmt([VarDecl(len, AutoType, BinExpr(::, Id(s), FuncCall(size, []))), VarDecl(num, AutoType, FloatLit(0.0)), VarDecl(i, AutoType, IntegerLit(0)), WhileStmt(BinExpr(==, ArrayCell(s, [Id(i)]), StringLit( )), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), VarDecl(positive, BooleanType, BinExpr(==, ArrayCell(s, [Id(i)]), StringLit(+))), VarDecl(negative, BooleanType, BinExpr(==, ArrayCell(s, [Id(i)]), StringLit(-))), WhileStmt(BinExpr(<, Id(i), BinExpr(&&, BinExpr(&&, Id(len), BinExpr(>=, ArrayCell(s, [Id(i)]), StringLit(0))), BinExpr(<=, ArrayCell(s, [Id(i)]), StringLit(9)))), BlockStmt([AssignStmt(Id(num), BinExpr(+, BinExpr(*, Id(num), IntegerLit(10)), BinExpr(-, ArrayCell(s, [Id(i)]), StringLit(0)))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(FuncCall(int, [Id(num)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_76(self):
        input = """addBinary: function string(a: string, b: string) {
        if(b::size() > (a::size())) swap(a,b);
        
        while(b::size() < (a::size())) b = "0" + b;

        carry, res: auto = 0, "";

        for(i = b::size()-1, i >= 0 , i - 1)
        {
             
             if(b[i] == "1" && (a[i]=="1"))
             {
                if(carry == 0) res = "0" + res;
                
                else res = "1" + res;
                carry = 1;
             }

             else {if(b[i] =="0" && (a[i] =="0"))
             {

                if(carry == 0) res = "0" + res;
                 
                else
                {
                    res = "1" + res;
                    carry = 0;
                }
             }
            }
             if((b[i]=="0" && (a[i]=="1")) || (b[i]=="1" && (a[i] == "0")))
             {
                 
                if(carry == 0) res = "1" + res;
                else res = "0" + res;
                 
             }
             
        }
        if(carry == 1) res = "1" + res;
        
        return res;
    }"""
        expect = """Program([
	FuncDecl(addBinary, StringType, [Param(a, StringType), Param(b, StringType)], None, BlockStmt([IfStmt(BinExpr(::, Id(b), BinExpr(>, FuncCall(size, []), BinExpr(::, Id(a), FuncCall(size, [])))), CallStmt(swap, Id(a), Id(b))), WhileStmt(BinExpr(::, Id(b), BinExpr(<, FuncCall(size, []), BinExpr(::, Id(a), FuncCall(size, [])))), AssignStmt(Id(b), BinExpr(+, StringLit(0), Id(b)))), VarDecl(carry, AutoType, IntegerLit(0)), VarDecl(res, AutoType, StringLit()), ForStmt(AssignStmt(Id(i), BinExpr(::, Id(b), BinExpr(-, FuncCall(size, []), IntegerLit(1)))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, ArrayCell(b, [Id(i)]), BinExpr(&&, StringLit(1), BinExpr(==, ArrayCell(a, [Id(i)]), StringLit(1)))), BlockStmt([IfStmt(BinExpr(==, Id(carry), IntegerLit(0)), AssignStmt(Id(res), BinExpr(+, StringLit(0), Id(res))), AssignStmt(Id(res), BinExpr(+, StringLit(1), Id(res)))), AssignStmt(Id(carry), IntegerLit(1))]), BlockStmt([IfStmt(BinExpr(==, ArrayCell(b, [Id(i)]), BinExpr(&&, StringLit(0), BinExpr(==, ArrayCell(a, [Id(i)]), StringLit(0)))), BlockStmt([IfStmt(BinExpr(==, Id(carry), IntegerLit(0)), AssignStmt(Id(res), BinExpr(+, StringLit(0), Id(res))), BlockStmt([AssignStmt(Id(res), BinExpr(+, StringLit(1), Id(res))), AssignStmt(Id(carry), IntegerLit(0))]))]))])), IfStmt(BinExpr(||, BinExpr(==, ArrayCell(b, [Id(i)]), BinExpr(&&, StringLit(0), BinExpr(==, ArrayCell(a, [Id(i)]), StringLit(1)))), BinExpr(==, ArrayCell(b, [Id(i)]), BinExpr(&&, StringLit(1), BinExpr(==, ArrayCell(a, [Id(i)]), StringLit(0))))), BlockStmt([IfStmt(BinExpr(==, Id(carry), IntegerLit(0)), AssignStmt(Id(res), BinExpr(+, StringLit(1), Id(res))), AssignStmt(Id(res), BinExpr(+, StringLit(0), Id(res))))]))])), IfStmt(BinExpr(==, Id(carry), IntegerLit(1)), AssignStmt(Id(res), BinExpr(+, StringLit(1), Id(res)))), ReturnStmt(Id(res))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_77(self):
        input = """addBinary: function string(a: string, b: string) {
        ans: string;
        carry: integer = 0;
        i,j: float = a::length() - 1, b::length() - 1;
        while(i >= 0 || (j >= 0) || carry) {
            if (i >= 0) carry = carry + a[i-1] - "0";
            if (j >= 0) carry = carry + b[j-1] - "0";
            ans = ans + carry % 2 + "0";
            carry = carry / 2;
        }
        reverse(begin(ans), end(ans));
        return ans;
    }"""
        expect = """Program([
	FuncDecl(addBinary, StringType, [Param(a, StringType), Param(b, StringType)], None, BlockStmt([VarDecl(ans, StringType), VarDecl(carry, IntegerType, IntegerLit(0)), VarDecl(i, FloatType, BinExpr(::, Id(a), BinExpr(-, FuncCall(length, []), IntegerLit(1)))), VarDecl(j, FloatType, BinExpr(::, Id(b), BinExpr(-, FuncCall(length, []), IntegerLit(1)))), WhileStmt(BinExpr(>=, Id(i), BinExpr(||, BinExpr(||, IntegerLit(0), BinExpr(>=, Id(j), IntegerLit(0))), Id(carry))), BlockStmt([IfStmt(BinExpr(>=, Id(i), IntegerLit(0)), AssignStmt(Id(carry), BinExpr(-, BinExpr(+, Id(carry), ArrayCell(a, [BinExpr(-, Id(i), IntegerLit(1))])), StringLit(0)))), IfStmt(BinExpr(>=, Id(j), IntegerLit(0)), AssignStmt(Id(carry), BinExpr(-, BinExpr(+, Id(carry), ArrayCell(b, [BinExpr(-, Id(j), IntegerLit(1))])), StringLit(0)))), AssignStmt(Id(ans), BinExpr(+, BinExpr(+, Id(ans), BinExpr(%, Id(carry), IntegerLit(2))), StringLit(0))), AssignStmt(Id(carry), BinExpr(/, Id(carry), IntegerLit(2)))])), CallStmt(reverse, FuncCall(begin, [Id(ans)]), FuncCall(end, [Id(ans)])), ReturnStmt(Id(ans))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_78(self):
        input = """mySqrt: function integer(x: integer) {
        if (x == 0) return x;
        first, last: integer = 1, x;
        while (first <= last) {
            mid: integer = first + (last - first) / 2;
            // mid * mid == x gives runtime error
            if (mid  == x / mid)
                return mid;
            else {if (mid > x / mid) {
                last = mid - 1;
            }
            else {
                first = mid + 1;
            }
            }
        }
        return last;
    }"""
        expect = """Program([
	FuncDecl(mySqrt, IntegerType, [Param(x, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(0)), ReturnStmt(Id(x))), VarDecl(first, IntegerType, IntegerLit(1)), VarDecl(last, IntegerType, Id(x)), WhileStmt(BinExpr(<=, Id(first), Id(last)), BlockStmt([VarDecl(mid, IntegerType, BinExpr(+, Id(first), BinExpr(/, BinExpr(-, Id(last), Id(first)), IntegerLit(2)))), IfStmt(BinExpr(==, Id(mid), BinExpr(/, Id(x), Id(mid))), ReturnStmt(Id(mid)), BlockStmt([IfStmt(BinExpr(>, Id(mid), BinExpr(/, Id(x), Id(mid))), BlockStmt([AssignStmt(Id(last), BinExpr(-, Id(mid), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(first), BinExpr(+, Id(mid), IntegerLit(1)))]))]))])), ReturnStmt(Id(last))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_79(self):
        input = """mySqrt: function integer(x: integer) {
        i: float = 0;
        while(i*i <=x)
        {
            if( (i*i) <= x && ((i+1)*(i+1) > x))
                return int(i);
                i = i + 1;
        }
        return 0;
    }"""
        expect = """Program([
	FuncDecl(mySqrt, IntegerType, [Param(x, IntegerType)], None, BlockStmt([VarDecl(i, FloatType, IntegerLit(0)), WhileStmt(BinExpr(<=, BinExpr(*, Id(i), Id(i)), Id(x)), BlockStmt([IfStmt(BinExpr(<=, BinExpr(*, Id(i), Id(i)), BinExpr(&&, Id(x), BinExpr(>, BinExpr(*, BinExpr(+, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(1))), Id(x)))), ReturnStmt(FuncCall(int, [Id(i)]))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_80(self):
        input = """ plusOne: function array [100] of integer(digits: array [100] of integer) {
        for (i = digits::size()-1, i >= 0, i-1) {
            if (digits[i] < 9) {
                digits[i] = digits[i] + 1;
                return digits;}
            digits[i] = 0;
        }
        insert(digits::begin(),1);
        return digits;
    }"""
        expect = """Program([
	FuncDecl(plusOne, ArrayType([100], IntegerType), [Param(digits, ArrayType([100], IntegerType))], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(::, Id(digits), BinExpr(-, FuncCall(size, []), IntegerLit(1)))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(digits, [Id(i)]), IntegerLit(9)), BlockStmt([AssignStmt(ArrayCell(digits, [Id(i)]), BinExpr(+, ArrayCell(digits, [Id(i)]), IntegerLit(1))), ReturnStmt(Id(digits))])), AssignStmt(ArrayCell(digits, [Id(i)]), IntegerLit(0))])), CallStmt(insert, BinExpr(::, Id(digits), FuncCall(begin, [])), IntegerLit(1)), ReturnStmt(Id(digits))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_81(self):
        input = """main: function void() {
            break;
            continue;
            return;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BreakStmt(), ContinueStmt(), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_82(self):
        input = """
        a,b,c,d,_,__,__init__: auto = 1,2," ", "\\t", "\\r", {{1,3}}, self;"""
        expect = """Program([
	VarDecl(a, AutoType, IntegerLit(1))
	VarDecl(b, AutoType, IntegerLit(2))
	VarDecl(c, AutoType, StringLit( ))
	VarDecl(d, AutoType, StringLit(\\t))
	VarDecl(_, AutoType, StringLit(\\r))
	VarDecl(__, AutoType, ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(3)])]))
	VarDecl(__init__, AutoType, Id(self))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_83(self):
        input = """main: function void() {
            __init__: auto = __init__;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(__init__, AutoType, Id(__init__))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_84(self):
        input = """main: function void() {
            readint();
            printint();
            readfloat();
            printfloat(); // change writeFloat to printFloat
            readbool();
            printbool();
            readstr();
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(readint, ), CallStmt(printint, ), CallStmt(readfloat, ), CallStmt(printfloat, ), CallStmt(readbool, ), CallStmt(printbool, ), CallStmt(readstr, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_85(self):
        input = """isOverlap: function boolean(a: array [100] of integer, b: array [100] of integer){
        return min(a[1], b[1]) - max(a[0], b[0]) >= 0;
    }"""
        expect = """Program([
	FuncDecl(isOverlap, BooleanType, [Param(a, ArrayType([100], IntegerType)), Param(b, ArrayType([100], IntegerType))], None, BlockStmt([ReturnStmt(BinExpr(>=, BinExpr(-, FuncCall(min, [ArrayCell(a, [IntegerLit(1)]), ArrayCell(b, [IntegerLit(1)])]), FuncCall(max, [ArrayCell(a, [IntegerLit(0)]), ArrayCell(b, [IntegerLit(0)])])), IntegerLit(0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_86(self):
        input = """merge: function array [100] of integer(a: array [100] of integer, b: array [100] of integer)
    {
        return {min(a[0],b[0]),max(a[1],b[1])};
    }  """
        expect = """Program([
	FuncDecl(merge, ArrayType([100], IntegerType), [Param(a, ArrayType([100], IntegerType)), Param(b, ArrayType([100], IntegerType))], None, BlockStmt([ReturnStmt(ArrayLit([FuncCall(min, [ArrayCell(a, [IntegerLit(0)]), ArrayCell(b, [IntegerLit(0)])]), FuncCall(max, [ArrayCell(a, [IntegerLit(1)]), ArrayCell(b, [IntegerLit(1)])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_87(self):
        input = """insert: function array [100] of integer() {
        while(val != intervals){
            if(val[1]<inp[0]) push_back(val);
            
            else{
                inp[0] = min(inp[0],val[0]);
                inp[1] = max(inp[1],val[1]);
            }
        }
        push_back(inp);
        return temp;
    }"""
        expect = """Program([
	FuncDecl(insert, ArrayType([100], IntegerType), [], None, BlockStmt([WhileStmt(BinExpr(!=, Id(val), Id(intervals)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(val, [IntegerLit(1)]), ArrayCell(inp, [IntegerLit(0)])), CallStmt(push_back, Id(val)), BlockStmt([AssignStmt(ArrayCell(inp, [IntegerLit(0)]), FuncCall(min, [ArrayCell(inp, [IntegerLit(0)]), ArrayCell(val, [IntegerLit(0)])])), AssignStmt(ArrayCell(inp, [IntegerLit(1)]), FuncCall(max, [ArrayCell(inp, [IntegerLit(1)]), ArrayCell(val, [IntegerLit(1)])]))]))])), CallStmt(push_back, Id(inp)), ReturnStmt(Id(temp))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_88(self):
        input = """singleNumber: function integer(nums: integer) inherit Expressions { 
       a: array [5,5,5,5,5] of integer;
	   while(x < nums)
		   a[x] = a[x] + 1;
	   while(z < a)
		   if(z::second==1)
			   return z::first;
	   return -1;
    }"""
        expect = """Program([
	FuncDecl(singleNumber, IntegerType, [Param(nums, IntegerType)], Expressions, BlockStmt([VarDecl(a, ArrayType([5, 5, 5, 5, 5], IntegerType)), WhileStmt(BinExpr(<, Id(x), Id(nums)), AssignStmt(ArrayCell(a, [Id(x)]), BinExpr(+, ArrayCell(a, [Id(x)]), IntegerLit(1)))), WhileStmt(BinExpr(<, Id(z), Id(a)), IfStmt(BinExpr(::, Id(z), BinExpr(==, Id(second), IntegerLit(1))), ReturnStmt(BinExpr(::, Id(z), Id(first))))), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_89(self):
        input = """singleNumber: function integer(nums: array[100] of integer) inherit Expressions { 
       sort(nums::begin(),nums::end());
        for(i=1, i<nums::size(), i+2)
        {
            if(nums[i]!=nums[i-1])
                return nums[i-1];
        }
        return nums[nums::size()-1];
    }"""
        expect = """Program([
	FuncDecl(singleNumber, IntegerType, [Param(nums, ArrayType([100], IntegerType))], Expressions, BlockStmt([CallStmt(sort, BinExpr(::, Id(nums), FuncCall(begin, [])), BinExpr(::, Id(nums), FuncCall(end, []))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(::, BinExpr(<, Id(i), Id(nums)), FuncCall(size, [])), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(!=, ArrayCell(nums, [Id(i)]), ArrayCell(nums, [BinExpr(-, Id(i), IntegerLit(1))])), ReturnStmt(ArrayCell(nums, [BinExpr(-, Id(i), IntegerLit(1))])))])), ReturnStmt(ArrayCell(nums, [BinExpr(::, Id(nums), BinExpr(-, FuncCall(size, []), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_90(self):
        input = """singleNumber: function integer(nums: array[100] of integer)
    {
        return accumulate(nums::begin(), nums::end(), 0, {{}});
    }"""
        expect = """Program([
	FuncDecl(singleNumber, IntegerType, [Param(nums, ArrayType([100], IntegerType))], None, BlockStmt([ReturnStmt(FuncCall(accumulate, [BinExpr(::, Id(nums), FuncCall(begin, [])), BinExpr(::, Id(nums), FuncCall(end, [])), IntegerLit(0), ArrayLit([ArrayLit([])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_91(self):
        input = """result: integer = 123_456.789e10;
    MAX_SIZE: auto = 3 * int(Math::pow(10, 4));
    TOTAL_SIZE: auto = MAX_SIZE * 2 + 1;
    numOccurrence: array [100] of boolean = a[TOTAL_SIZE];"""
        expect = """Program([
	VarDecl(result, IntegerType, FloatLit(1234567890000000.0))
	VarDecl(MAX_SIZE, AutoType, BinExpr(*, IntegerLit(3), FuncCall(int, [BinExpr(::, Id(Math), FuncCall(pow, [IntegerLit(10), IntegerLit(4)]))])))
	VarDecl(TOTAL_SIZE, AutoType, BinExpr(+, BinExpr(*, Id(MAX_SIZE), IntegerLit(2)), IntegerLit(1)))
	VarDecl(numOccurrence, ArrayType([100], BooleanType), ArrayCell(a, [Id(TOTAL_SIZE)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_92(self):
        input = """isPalindrome: function boolean(s:string) {

            // if not alpha numeric increase/decrement pointer respectiverly
            if(!isalnum(int(startChar))){
                start = start + 1;
                continue;
            }
            if(!isalnum(int(lastChar))){
                end = end - 1;
                break;
            }

            // if char match go for next char
            if(startChar==lastChar){
                start = start + 1;
                end = end - 1;
            }else{
                return false;
            }
        return true;
    }"""
        expect = """Program([
	FuncDecl(isPalindrome, BooleanType, [Param(s, StringType)], None, BlockStmt([IfStmt(UnExpr(!, FuncCall(isalnum, [FuncCall(int, [Id(startChar)])])), BlockStmt([AssignStmt(Id(start), BinExpr(+, Id(start), IntegerLit(1))), ContinueStmt()])), IfStmt(UnExpr(!, FuncCall(isalnum, [FuncCall(int, [Id(lastChar)])])), BlockStmt([AssignStmt(Id(end), BinExpr(-, Id(end), IntegerLit(1))), BreakStmt()])), IfStmt(BinExpr(==, Id(startChar), Id(lastChar)), BlockStmt([AssignStmt(Id(start), BinExpr(+, Id(start), IntegerLit(1))), AssignStmt(Id(end), BinExpr(-, Id(end), IntegerLit(1)))]), BlockStmt([ReturnStmt(BooleanLit(False))])), ReturnStmt(BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_93(self):
        input = """main: function void() {
            return compose_comp(compose(foo(goo(hoo(doo(zoo(1)))))));
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(FuncCall(compose_comp, [FuncCall(compose, [FuncCall(foo, [FuncCall(goo, [FuncCall(hoo, [FuncCall(doo, [FuncCall(zoo, [IntegerLit(1)])])])])])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_94(self):
        input = """majorityElement: function integer(arr: array [100] of integer) {
        ele, count: auto = arr[0,1], 0;
        for(i=0, i<size(), i+1){
            if(count==0) ele=arr[i];
            count = count + ((ele==arr[i])== 10);
        }
        return ele;
    }"""
        expect = """Program([
	FuncDecl(majorityElement, IntegerType, [Param(arr, ArrayType([100], IntegerType))], None, BlockStmt([VarDecl(ele, AutoType, ArrayCell(arr, [IntegerLit(0), IntegerLit(1)])), VarDecl(count, AutoType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(size, [])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(count), IntegerLit(0)), AssignStmt(Id(ele), ArrayCell(arr, [Id(i)]))), AssignStmt(Id(count), BinExpr(+, Id(count), BinExpr(==, BinExpr(==, Id(ele), ArrayCell(arr, [Id(i)])), IntegerLit(10))))])), ReturnStmt(Id(ele))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_95(self):
        input = """sort: function integer(a: integer, b: integer)
{
    return int(a)-int(b);
}
majorityElement: function integer(nums: array [100] of integer, numsSize: integer){
qsort(nums,numsSize,sizeof(int),sort);
return nums[numsSize/2];

}
a: auto = sort();"""
        expect = """Program([
	FuncDecl(sort, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(-, FuncCall(int, [Id(a)]), FuncCall(int, [Id(b)])))]))
	FuncDecl(majorityElement, IntegerType, [Param(nums, ArrayType([100], IntegerType)), Param(numsSize, IntegerType)], None, BlockStmt([CallStmt(qsort, Id(nums), Id(numsSize), FuncCall(sizeof, [Id(int)]), Id(sort)), ReturnStmt(ArrayCell(nums, [BinExpr(/, Id(numsSize), IntegerLit(2))]))]))
	VarDecl(a, AutoType, FuncCall(sort, []))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_96(self):
        input = """main: function void() {
            if(__init___(self) == "==") {
                self = "==";
            }
            else {
                if(__init__(self) == "<=") {
                    self = "<=";
                }
                else {
                    if (__init__(self) == "[,]") {
                        self = "[,]";
                    }
                    else {
                        self = "-";
                    }
                }
            }
            return __init__(self);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, FuncCall(__init___, [Id(self)]), StringLit(==)), BlockStmt([AssignStmt(Id(self), StringLit(==))]), BlockStmt([IfStmt(BinExpr(==, FuncCall(__init__, [Id(self)]), StringLit(<=)), BlockStmt([AssignStmt(Id(self), StringLit(<=))]), BlockStmt([IfStmt(BinExpr(==, FuncCall(__init__, [Id(self)]), StringLit([,])), BlockStmt([AssignStmt(Id(self), StringLit([,]))]), BlockStmt([AssignStmt(Id(self), StringLit(-))]))]))])), ReturnStmt(FuncCall(__init__, [Id(self)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_97(self):
        input = """main: function void() {
            for (i = foo(), i < goo(), i + hoo()) {
                do {
                    i = zoo();
                }
                while(!zoo(!foo(!goo(-hoo()))));
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), FuncCall(foo, [])), BinExpr(<, Id(i), FuncCall(goo, [])), BinExpr(+, Id(i), FuncCall(hoo, [])), BlockStmt([DoWhileStmt(UnExpr(!, FuncCall(zoo, [UnExpr(!, FuncCall(foo, [UnExpr(!, FuncCall(goo, [UnExpr(-, FuncCall(hoo, []))]))]))])), BlockStmt([AssignStmt(Id(i), FuncCall(zoo, []))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_98(self):
        input = """column, category, command: auto;
        main: function void() {
            print("FROM ", column, "\\n", "SELECT ", category, "\\n", "WHERE ", command[0,0], command[0,1], command[1,0], command[1,1], "\\n");
            return;
        }"""
        expect = """Program([
	VarDecl(column, AutoType)
	VarDecl(category, AutoType)
	VarDecl(command, AutoType)
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, StringLit(FROM ), Id(column), StringLit(\\n), StringLit(SELECT ), Id(category), StringLit(\\n), StringLit(WHERE ), ArrayCell(command, [IntegerLit(0), IntegerLit(0)]), ArrayCell(command, [IntegerLit(0), IntegerLit(1)]), ArrayCell(command, [IntegerLit(1), IntegerLit(0)]), ArrayCell(command, [IntegerLit(1), IntegerLit(1)]), StringLit(\\n)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_99(self):
        input = """main: function void() inherit Foo {
            print("------------------");
            print("| \\t \\t \\t \\t |"); \t
            print("| \\r \\r \\r \\r |"); \b
            print("| \\b \\b \\b \\b |"); \b
            print("------------------");
            foo = a;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], Foo, BlockStmt([CallStmt(print, StringLit(------------------)), CallStmt(print, StringLit(| \\t \\t \\t \\t |)), CallStmt(print, StringLit(| \\r \\r \\r \\r |)), CallStmt(print, StringLit(| \\b \\b \\b \\b |)), CallStmt(print, StringLit(------------------)), AssignStmt(Id(foo), Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

#     def test(self):
#         input = """a: float = .e10;"""
#         expect = """Program([
# 	VarDecl(a, FloatType, FloatLit(0.0))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 400))
