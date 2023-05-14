import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    
    def test_00(self):
        program_input = """a: integer = 3;"""
        expected_output = "No entry point"
        self.assertTrue(TestChecker.test(program_input, expected_output, 400))

    def test_01(self):
        input = """x, y, z: integer = 1, 2, 3;
        main: function void() {
            return;
        }"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_03(self):
        """Simple program"""
        input = """main: function void () {}"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_04(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_05(self):
        input = """
        print: function integer(n: auto) {
            printInteger(n + 1);
        }
        main: function void() {
            print(1);
        }
        """
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 405))

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
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_07(self):
        input = """main: function void() {
            if(n == 0) {
                break;
            }
            else {
                n = var - 1;
            }
        }"""
        expect = """Undeclared Identifier: n"""
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_08(self):
        input = """x1, y1: auto;
        main: function void () {}"""
        expect = """Invalid Variable: x1"""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_09(self):
        input = """decrem2: function void(inherit out a: integer) {
                while (a < 10) {
                    a = a - 1;
                }
            }
            main: function void() {}"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_10(self):
        input = """foo1: function integer(x: integer, y: float) {
                return foo2(5, 3.1e10);
            }
            foo2: function float(x: float, y: integer) {
                return foo1(3.1e10, 5);
            }
            main: function void() {}"""
        expect = """Type mismatch in statement: ReturnStmt(FuncCall(foo2, [IntegerLit(5), FloatLit(31000000000.0)]))"""
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_11(self):
        input = """arr1, arr2: array [2] of float = {1.9,2.3}, {3,4.7};
        arr: array[1,3] of float = {{1,2,3}, {4,5,6}, {7,8,9}};
        main: function void() {}"""
        expect = """Illegal array literal: ArrayLit([IntegerLit(3), FloatLit(4.7)])"""
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_12(self):
        input = """checkop1: auto = 3 * 5 % 6 && 1 >= 0;
        main: function void() {}"""
        expect = """Type mismatch in expression: BinExpr(>=, BinExpr(&&, BinExpr(%, BinExpr(*, IntegerLit(3), IntegerLit(5)), IntegerLit(6)), IntegerLit(1)), IntegerLit(0))"""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_13(self):
        input = """checkop1: auto = 1 != true + "2"::"-3";
        main: function void() {}"""
        expect = """Type mismatch in expression: BinExpr(+, BooleanLit(True), StringLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_14(self):
        input = """goo: function void() {
                return arr["2"::"3"];
            }
            main: function void() {}"""
        expect = """Undeclared Variable: arr"""
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_15(self):
        input = """foo: function integer (a: auto){ 
            if (a == 0) return 0;
            else return 1;
        }

        main: function void () {
            a: integer = foo(0);
        }"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_16(self):
        input = """foo: function float(foo: integer) {
            return foo;
        }
        main: function void () {
            return;
        }"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_17(self):
        input = """
        a: float;
        b: integer;
        a: boolean;
        main: function void() {
                return;
            } """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_18(self):
        input = """
        main: function void() {
            a: integer = 1;
                while(a != 0)
                    a = a + 1;
                    do {
                        a = a + 1;
                    }
                    while(a != 10);
            }"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_19(self):
        input = """
        a: float;
            main: function void() {
                a = a + readFloat();
            }"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_20(self):
        input = """foo: function integer(a: integer) {
                return foo(readInteger(a));
            }
            main: function void () {}"""
        expect = """Type mismatch in statement: FuncCall(readInteger, [Id(a)])"""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_21(self):
        input = """main: function void() {
                while((a != b) && (b != c) && (c!= 0)) {
                    
                }
            }"""
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_22(self):
        input = """main: function void() {
                for(i = 0, (i < 10) && (i != a), i + 3) i = i + 1;
            }
            """
        expect = """Undeclared Identifier: i"""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_23(self):
        input = """a: float = 3.0;
        main: function void() {
                if (a != 10)
                    if (a != 9)
                        if (a != 8)
                            if (a != 7)
                                return a;
            }"""
        expect = """Type mismatch in expression: BinExpr(!=, Id(a), IntegerLit(10))"""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_24(self):
        input = """foo: function integer (a: integer, b: auto)
            {
                super();
                if (a == 1){}
            }
            main: function void () {}"""
        expect = """Invalid statement in function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_25(self):
        input = """
        bar: function integer(a: integer, b: integer) {}
        foo: function integer (c: integer, d: auto) inherit bar {
            super(1,2);
        }
        main: function void() {}"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_26(self):
        input = """bar: function integer(a: integer, a: integer) {}
        foo: function integer (c: integer, d: auto) inherit bar {
            super(1,2);
        }
        main: function void() {}"""
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_27(self):
        input = """foo: function void(x: integer, inherit y: array [2] of float) {
                do {
                    y = 1;
                }
                while (y != 0);
            }
            main: function void() {}"""
        expect = """Type mismatch in expression: BinExpr(!=, Id(y), IntegerLit(0))"""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_28(self):
        input = """goo: function void() {
                return {1, "HCMUT", True};
            }
            main: function void() {}"""
        expect = """Undeclared Identifier: True"""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_29(self):
        input = """main: function float() {}"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_30(self):
        input = """main: function float() {}
        main: function void() {}"""
        expect = """Redeclared Function: main"""
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_31(self):
        input = """foo: function string (a: string)
            {
                return "1"::a;
            }
            main: function void() {}"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_32(self):
        input = """foo: function integer (a: string)
            {
                return "1"::a;
            }
            main: function void() {}"""
        expect = """Type mismatch in statement: ReturnStmt(BinExpr(::, StringLit(1), Id(a)))"""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_33(self):
        input = """fact: function void(out a: integer) {
                /* do sth */
                {
                    // TODO
                }
            }
            main: function void() {}"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_34(self):
        input = """arr: array [2] of integer = -{1,2};
        main: function void() {}"""
        expect = """Type mismatch in Variable Declaration: VarDecl(arr, ArrayType([2], IntegerType), UnExpr(-, ArrayLit([IntegerLit(1), IntegerLit(2)])))"""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_35(self):
        input = """main: float = main();
        main: function void() {}"""
        expect = """Type mismatch in expression: FuncCall(main, [])"""
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_36(self):
        input = """backtrack: function void(i: integer, inherit out m: integer) {
            cur: integer = check();
            if (i >= m) {
                if (check()) {
                    res = min(res, cur);
                }
                return;
            }
            j: integer;
            for (j = 0, j < 2, j+1) {
                i = j;
                cur = cur + j * i;
                backtrack(i + 1);
                cur = cur - j * i;
            }
        }
        check: function boolean() {
                return 1;
            }
        min: function void(x: integer, y: float) {}
        main: function void () {}"""
        expect = """Type mismatch in Variable Declaration: VarDecl(cur, IntegerType, FuncCall(check, []))"""
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_37(self):
        input = """bar: function integer(inherit x: float) {}
            foo: function integer (a: integer, b: auto) inherit bar 
            {
                preventDefault();
                if (a == 1)
                {
                    b: integer;
                }
            }
            main: function void () {}"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_38(self):
        input = """bar : function void (a:float) inherit foo{
                super();
            } 
            foo : function auto (a: float){}
            main: function void () {}"""
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_39(self):
        input = """main: function void()
{
    m,n: integer;
    i,j,w: integer;
    host, temp: array [100] of integer;
    idx: integer;
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
    return;
}"""
        expect = """Undeclared Function: push_back"""
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_40(self):
        input = """
        a: auto;
        main: function void() {}"""
        expect = """Invalid Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_41(self):
        input = """
        a: auto = 5;
        main: function void (b: integer) {}"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_42(self):
        input = """
        a: array [2,2] of float = {{1,1},{2,2},{"a","b"}};
        main: function void () {}"""
        expect = """Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2, 2], FloatType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(1)]), ArrayLit([IntegerLit(2), IntegerLit(2)]), ArrayLit([StringLit(a), StringLit(b)])]))"""
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_43(self):
        input = """
        bar: function void (inherit c: auto){
            c = 1.1;
        }
        
        foo: function void (a: integer, b: auto) inherit bar {
                preventDefault();
                c = 1;
            }

        main: function void () {}
        """
        expect = """Type mismatch in statement: AssignStmt(Id(c), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_44(self):
        input = """
        bar: function void (inherit c: auto){
            c = 1.1;
        }
        
        foo: function void (a: integer, b: auto) inherit bar {
                super();
                c = 1;
            }

        main: function void () {}
        """
        expect = """Type mismatch in statement: CallStmt(super, )"""
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_45(self):
        input = """
        bar: function void (inherit c: auto){
            c = 1.1;
        }
        
        foo: function void (a: integer, b: auto) inherit bar {
                c = 1;
            }

        main: function void () {}"""
        expect = """Invalid statement in function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_46(self):
        input = """bar: function void (inherit c: auto){
            c = 1.1;
        }
        
        foo: function void (a: integer, b: auto) inherit bar {
                super(1);
                c = 1;
            }

        main: function void () {}"""
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_47(self):
        input = """  twoSum: function array [100] of integer(nums: array [100] of integer, target: integer)
        {
        i,j: integer = 0, 1;
        for (i=j, j < 1, i+1){
            r: integer = target - j;
            if (r <= 1) return 1;
            }
            return;
        }
        main: function void () {}"""
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_48(self):
        input = """
        twoSum: function array [100] of integer(nums: array [100] of integer, target: integer)
        {
        i,j: integer = 0, 1;
        for (i=j, j < 1, i+1){
            r: integer = target - j;
            if (r <= 1) {}
            break;
            }
            return;
        }
        main: function void () {}"""
        expect = """Type mismatch in statement: ReturnStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_49(self):
        input = """
        twoSum: function array [100] of integer(nums: array [100] of integer, target: integer)
        {
        i,j: integer = 0, 1;
        for (i=j, j < 1, i+1){
            r: integer = target - j;
            if (r <= 1) {}
            
            }
            break;
            return;
        }
        main: function void () {}"""
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_50(self):
        input = """
        twoSum: function array [100] of integer(nums: array [100] of integer, target: integer)
        {
        i,j: integer = 0, 1;
        for (i=j, j < 1, i+1){
            r: integer = target - j;
            if (r <= 1) {}
                break;
            }
            continue;
            return;
        }
        main: function void () {}"""
        expect = """Must in loop: ContinueStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_51(self):
        input = """
        foo: function auto() {return 1;}
        a: integer = --foo();
        main: function void () {}"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_52(self):
        input = """main: function void() {
                b: array[2] of integer = {1,3};
                c: float = 1.2;
                a: integer = b - c;
            }"""
        expect = """Type mismatch in expression: BinExpr(-, Id(b), Id(c))"""
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_53(self):
        input = """a: integer = (3 >= 4) || (1 <= 2);
        main: function void() {}"""
        expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(||, BinExpr(>=, IntegerLit(3), IntegerLit(4)), BinExpr(<=, IntegerLit(1), IntegerLit(2))))"""
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_54(self):
        input = """
        main: function void() {preventDefault();}"""
        expect = """Invalid statement in function: main"""
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_55(self):
        input = """main: function void() {
                a: string = "ab" + "c";
            }"""
        expect = """Type mismatch in expression: BinExpr(+, StringLit(ab), StringLit(c))"""
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_56(self):
        input = """ main: function void() {
                _ = _ <= _;
            }"""
        expect = """Undeclared Identifier: _"""
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_57(self):
        input = """
        a,b: auto = 4.5, 3;
        main: function void() {
                while(a + b != 10)
                    a = a + 1;
            }"""
        expect = """Type mismatch in expression: BinExpr(!=, BinExpr(+, Id(a), Id(b)), IntegerLit(10))"""
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_58(self):
        input = """main: function void() {
                readinteger();
                readinteger();
                readinteger();
            }"""
        expect = """Undeclared Function: readinteger"""
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_59(self):
        input = """ main: function void() {
                __: string;
                _: string = __::__;
            }"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_60(self):
        input = """ main: function void() {
                __: string;
                _: string = __ <= __;
            }"""
        expect = """Type mismatch in expression: BinExpr(<=, Id(__), Id(__))"""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_61(self):
        input = """ foo: function integer (a: auto, b: auto)
            {
            
            }
            bar: function auto ()
            {
                foo(1.1,1);
                foo(1,2);
                c: integer = bar();
                
            }
            main: function void() {}"""
        expect = """Type mismatch in expression: IntegerLit(1)"""
        self.assertTrue(TestChecker.test(input, expect, 461))

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
        expect = """Type mismatch in expression: ArrayCell(nums, [Id(i)])"""
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_63(self):
        input = """removeElement: function integer(nums: array [100] of integer, val: integer) {
    j,x: integer = 0, 1; 
    v: float = 2.1;
    while(x % v){
        if(x!=val){
            v[j]=x;
            j = j + 1;
        }
    }
    return j;
}
main: function void() {}"""
        expect = """Type mismatch in expression: BinExpr(%, Id(x), Id(v))"""
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_64(self):
        input = """searchInsert: function integer(nums: array [100] of integer, x: integer) {
        if(x<=nums[0]) return 0;
        if(nums[x-1] < x){ return 1;
        } if(nums[x-1]==x){ return 2;
        }
        i,j: integer = 0, x-1;
        while(i<=j){
            mid = (j-i)/2+i;
            if(nums[(mid-1) % x]<x 
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
        expect = """Type mismatch in expression: ArrayCell(nums, [IntegerLit(0)])"""
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_65(self):
        input = """foo: function integer (a: boolean, b: integer)
            {
                if (( 1 != true) && ( b == a))
                {
                
                }
            }
            main: function void() {}"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_66(self):
        input = """
        foo: function integer (a: boolean, b: float)
            {
                if (( 1 != true) && ( b == a))
                {
                
                }
            }
            main: function void() {}"""
        expect = """Type mismatch in expression: BinExpr(==, Id(b), Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_67(self):
        input = """foo: function integer (a: integer, b: float)
            {
                if (( 1 != true) && ( b >= a))
                {
                
                }
            }
            main: function void() {}"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_68(self):
        input = """  power: function float(x: float, n: integer){
        if(n==0){
            return 1;
        }
        return x * power(x, n-1);
    }
    myPow: function float(x: float, n: integer) inherit power{
        if (n == 100000) return (x == 1) && -1;
        if (n == -100000) return (x == 1 || (x == -1)) && 1;
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
    }
    main: function void() {}"""
        expect = """Invalid Parameter: x"""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_69(self):
        input = """
        power: function float(x: float, n: integer){
        if(n==0){
            return 1;
        }
        return x * power(x, n-1);
    }
    myPow: function float() inherit power{
        if (n == 100000) return (x == 1) && -1;
        if (n == -100000) return (x == 1 || (x == -1)) && 1;
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
    }
    main: function void() {}"""
        expect = """Invalid statement in function: myPow"""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_70(self):
        input = """power: function float(x: float, n: integer){
        if(n==0){
            return 1;
        }
        return x * power(x, n-1);
    }
    myPow: function float() inherit power{
        super();
        if (n == 100000) return (x == 1) && -1;
        if (n == -100000) return (x == 1 || (x == -1)) && 1;
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
    }
    main: function void() {}"""
        expect = """Type mismatch in statement: CallStmt(super, )"""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_71(self):
        input = """power: function float(x: float, n: integer){
        if(n==0){
            return 1;
        }
        return x * power(x, n-1);
    }
    myPow: function float() inherit power{
        preventDefault();
        if (n == 100000) return (x == 1) && -1;
        if (n == -100000) return (x == 1 || (x == -1)) && 1;
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
    }
    main: function void() {}"""
        expect = """Type mismatch in expression: BinExpr(==, Id(x), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_72(self):
        input = """power: function float(x: float, n: integer){
        if(n==0){
            return 1;
        }
        return x * power(x, n-1);
    }
    
    main: function void() {}"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_73(self):
        input = """bar: function void () inherit foo{
                super(1.1);
            } 
            foo: function auto(a: float) {} 
            main: function void() {}"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_74(self):
        input = """bar: function void (a: float) inherit foo{
                preventDefault();
                super(a);
            } 
            foo: function auto() {} 
            main: function void() {}"""
        expect = """Type mismatch in statement: CallStmt(super, Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_75(self):
        input = """bar: function void () inherit foo{
                super(true);
            } 
            foo: function auto(a: float) {} 
            main: function void() {}"""
        expect = """Type mismatch in expression: BooleanLit(True)"""
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_76(self):
        input = """main: function void() {
            preventDefault();
            super();
        }"""
        expect = """Invalid statement in function: main"""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_77(self):
        input = """
        nums: array[2] of integer = {1,2};
        print: function integer(a: integer) {
            return a;
        }
        main: function void() {
            print(nums[0]);
            print(nums[1]);
        }"""
        expect = """Type mismatch in expression: ArrayCell(nums, [IntegerLit(0)])"""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_78(self):
        input = """mySqrt: function integer(x: integer) {
        if (x == 0) return x;
        first, last: integer = 1, x;
        while (first <= last) {
            mid: integer = first + (last - first) / 2;
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
    }
    main: function void() {}"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_79(self):
        input = """mySqrt: function integer(x: integer) {
        i: float = 0;
        while(i*i <=x)
        {
            if( (i*i) <= x && ((i+1)*(i+1) > x))
                return i;
                i = i + 1;
            break;
        }
        return 0;
    }
    main: function void() {}"""
        expect = """Type mismatch in expression: BinExpr(<=, BinExpr(*, Id(i), Id(i)), BinExpr(&&, Id(x), BinExpr(>, BinExpr(*, BinExpr(+, Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(1))), Id(x))))"""
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_80(self):
        input = """ main: function void() {
            break;
        }"""
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_81(self):
        input = """main: function void() {
            return;
            break;
            continue;
        }"""
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_82(self):
        input = """main: function void () {
        a,b,c,d,_,__,__init__: auto = 1,2," ", "\\t", "\\r", {{1,3}}, ":";}"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_83(self):
        input = """main: function void() {
            readInteger();
            printInteger(2.3);
            readFloat();
            printFloat(); // change writeFloat to printFloat
            readBoolean();
            printBoolean();
        }"""
        expect = """Type mismatch in statement: CallStmt(printFloat, )"""
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_84(self):
        input = """main: function void() {
            readInteger();
            printInteger();
            readFloat();
            printFloat(); // change writeFloat to printFloat
            readBoolean();
            printBoolean();
        }"""
        expect = """Type mismatch in statement: CallStmt(printInteger, )"""
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_85(self):
        input = """
            a: string;
            b: boolean = 2;
            main: function void() {}"""
        expect = """Type mismatch in Variable Declaration: VarDecl(b, BooleanType, IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_86(self):
        input = """a: string;
            b: boolean = 0;
            c: string;
            d: string = a::c;
            main: function void() {}"""
        expect = """Type mismatch in Variable Declaration: VarDecl(b, BooleanType, IntegerLit(0))"""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_87(self):
        input = """a: string = "1";
            c: string;
            d: string = a::c + "2";
            main: function void() {}"""
        expect = """Type mismatch in expression: BinExpr(+, Id(c), StringLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_88(self):
        input = """singleNumber: function integer(nums: integer) inherit Expressions { 
       a: array [5,5,5,5,5] of integer;
	   while(x < nums)
		   a[x] = a[x] + 1;
	   while(z < a)
		   if(z::second==1)
			   return z::first;
	   return -1;
    }
    main: function void() {}"""
        expect = """Undeclared Function: Expressions"""
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_89(self):
        input = """singleNumber: function integer(nums: array[100] of integer)
    {
        return nums;
    }
    main: function void() {}"""
        expect = """Type mismatch in statement: ReturnStmt(Id(nums))"""
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_90(self):
        input = """singleNumber: function integer(nums: array[100] of integer)
    {
        return;
    }
    main: function void() {}"""
        expect = """Type mismatch in statement: ReturnStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_91(self):
        input = """result: integer = 123_456.789e10;
    MAX_SIZE: auto = 3 * int(Math::pow(10, 4));
    TOTAL_SIZE: auto = MAX_SIZE * 2 + 1;
    numOccurrence: array [100] of boolean = a[TOTAL_SIZE];
    main: function void() {}"""
        expect = """Type mismatch in Variable Declaration: VarDecl(result, IntegerType, FloatLit(1234567890000000.0))"""
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_92(self):
        input = """__init__: function auto (self: auto) {return __init__(1);}
        main: function void() {
            if(__init__(1) == "==") {
                self = "==";
            }
            else {
                if(__init__(1) == "<=") {
                    self = "<=";
                }
                else {
                    if (__init__(1) == "[,]") {
                        self = "[,]";
                    }
                    else {
                        self = "-";
                    }
                }
            }
            return __init__(1);
        }"""
        expect = """Type mismatch in expression: BinExpr(==, FuncCall(__init__, [IntegerLit(1)]), StringLit(==))"""
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_93(self):
        input = """sort: function integer(a: integer, b: integer)
{
    return a - b;
}

x: auto = sort(1,2);
main: function void() {}"""
        expect = """None"""
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_94(self):
        input = """
        sort: function integer(a: integer, b: integer)
{
    return a - b;
}

x: auto = sort();
main: function void() {}"""
        expect = """Type mismatch in statement: FuncCall(sort, [])"""
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_95(self):
        input = """sort: function integer(a: integer, b: integer)
{
    return a - b;
}

a: auto = sort();
main: function void() {}"""
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_96(self):
        input = """
        __init__: function auto (self: auto) {return __init__(1);}
        main: function void() {
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
        expect = """Undeclared Function: __init___"""
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_97(self):
        input = """
        a: integer = foo(1,2);
            foo: function integer(a:auto, b:integer) inherit bar
            {
                c: float = a;
                for (a=1,a<2,a+1)
                {
                    return b;
                    return false;
                }
                return "1" + "2";
            }

            bar: function void() {}
            main: function void() {}
            """
        expect = """Invalid statement in function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_98(self):
        input = """column, category, command: auto;
        print: function string(a: string) {return a;}
        main: function void() {
            print("FROM ", column, "\\n", "SELECT ", category, "\\n", "WHERE ", command[0,0], command[0,1], command[1,0], command[1,1], "\\n");
            return;
        }"""
        expect = """Invalid Variable: column"""
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_99(self):
        input = """
        print: function void(a: string) { return a;}
        main: function void() {
            print("------------------");
            print("| \\t \\t \\t \\t |");
            print("| \\r \\r \\r \\r |");
            print("| \\b \\b \\b \\b |");
            print("------------------");
        }"""
        expect = """Type mismatch in statement: ReturnStmt(Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 499))