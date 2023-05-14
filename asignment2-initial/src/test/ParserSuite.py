import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    
    # def test_00(self):
    #     input = """
    #     print: function integer(n: auto) {
    #         printInteger(n);
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect,200))
    
    def test_01(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_02(self):
        input = "x,y: array [2,3] of integer;"
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    # def test_03(self):
    #     input = """ 
    #     x: integer = 65;
    #     fact: function integer(n: integer) {
    #         if (n == 0) return 1;
    #         else return n * fact(n - 1);
    #     }
    #     inc: function void(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     main: function void() {
    #         delta: integer = fact(3);
    #         inc(x, delta);
    #         printInteger(x);
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 203))
    
    def test_04(self):
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 204))
    
    def test_05(self):
        input = """
        main: function void() {
            if(n == 0) {
                break;
            }
            else {
                n = var - 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_06(self):
        input = """x1, y1: auto;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_07(self):
        input = """
            decrem: function void(inherit out a: integer) {
                while (a < 10) {
                    a--;
                }
            }
        """
        expect = "Error on line 4 col 21: -"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_08(self):
        input = """
            decrem2: function void(inherit out a: integer) {
                while (a < 10) {
                    a = a - 1;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    
    # def test_09(self):
    #     input = """
    #         read: function void() {
    #             for (i = 1, i < 10, i + 1) {
    #                 readInteger(i);
    #             }
    #         }
    #     """
    #     expect = "Error on line 4 col 32: i"
    #     self.assertTrue(TestParser.test(input, expect, 209))
    
    def test_10(self):
        input = """
            foo1: function integer(x: integer, y: float) {
                return foo2(5, 3.1e10);
            }
            foo2: function float(x: float, y: integer) {
                return foo1(3.1e10, 5);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_11(self):
        input = """inherit out x: auto;"""
        expect = "Error on line 1 col 0: inherit"
        self.assertTrue(TestParser.test(input, expect, 211))
    
    def test_12(self):
        input = """"""
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 212))
    
    def test_13(self):
        input = """
            arr1, arr2: array [2] of float = {1.9,2.3}, {3.6,4.7};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
    
    def test_14(self):
        input = """
            checkop1: auto = 3 * 5 % 6 && 1 >= 0;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_15(self):
        input = """
            checkop2: integer = 3 * 5 % 6 && 1 >= 0 <= 4;
        """
        expect = "Error on line 2 col 52: <="
        self.assertTrue(TestParser.test(input, expect, 215))
    
    def test_16(self):
        input = """
            checkop3: boolean =  !True && !False || 11;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    
    def test_17(self):
        input = """checkop4: boolean =  !True !False || 11;
        """
        expect = "Error on line 1 col 27: !"
        self.assertTrue(TestParser.test(input, expect, 217))
    
    def test_18(self):
        input = """checkop4: boolean =  !0 || !11 || 1 || 11;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    
    def test_19(self):
        input = """checkop5: boolean =  !00 || !11 || 1 || 11;
        """
        expect = "Error on line 1 col 23: 0"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_20(self):
        input = """ 
            foo: function void(x, y: integer) {
                do {
                    a = 1;
                }
                while (a != 0)
            }
        """
        expect = "Error on line 2 col 32: ,"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_21(self):
        input = """ 
            foo: function void(x: integer, inherit y: array [2] of float) {
                do {
                    a = 1;
                }
                while (a != 0);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
    
    def test_22(self):
        input = """ 
            goo: function void() {
                return {1,2,3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    
    def test_23(self):
        input = """ 
            goo: function void() {
                return {1, "HCMUT", True};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
    
    def test_24(self):
        input = """ 
            goo: function void() {
                return arr[2::3];
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_25(self):
        input = """ 
            goo: function void() {
                return arr[var1, var2, var3 + var4];
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
    
    def test_26(self):
        input = """ 
            goo: function void() {
                return !0 || !11 || 1 || 11;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
    
    def test_27(self):
        input = """ 
            goo: function void(a: array [2] of integer) {
                a[2] = {1,2};
                a = {1,2};
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
    
    def test_28(self):
        input = """a: array [4,1] of void = {{}};
        """
        expect = "Error on line 1 col 18: void"
        self.assertTrue(TestParser.test(input, expect, 228))
    
    def test_29(self):
        input = """a: array [4,1] of boolean = {{}};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_30(self):
        input = """a: array [4+6,9-8] of boolean = {{}};
        """
        expect = "Error on line 1 col 11: +"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_31(self):
        input = """
        main: function void() {
            a[2+3] = {1,2,3,4,5};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
    
    def test_32(self):
        input = """
        main: function void() {
            a[0],a[1] = 1,2;
        }
        """
        expect = "Error on line 3 col 16: ,"
        self.assertTrue(TestParser.test(input, expect, 232))
    
    def test_33(self):
        input = """
            fact: function void(out a: integer) inherit foo {
                /* do sth */
            } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))
    
    def test_34(self):
        input = """out n: integer;
        """
        expect = "Error on line 1 col 0: out"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_35(self):
        input = """
            fact: function void(out a: integer) {
                /* do sth */
                {
                    // TODO
                }
            } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    
    def test_36(self):
        input = """n: break = 2;"""
        expect = "Error on line 1 col 3: break"
        self.assertTrue(TestParser.test(input, expect, 236))
    
    def test_37(self):
        input = """continue;
        """
        expect = "Error on line 1 col 0: continue"
        self.assertTrue(TestParser.test(input, expect, 237))
    
    def test_38(self):
        input = """fact: function void(out a: integer) {"""
        expect = "Error on line 1 col 37: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 238))
    
    def test_39(self):
        input = """preventDefault();"""
        expect = "Error on line 1 col 0: preventDefault"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_40(self):
        input = """
            goo: function void() {
                while a != 10 {}
            } 
        """
        expect = "Error on line 3 col 22: a"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_41(self):
        input = """var1: continue = 1;
        """
        expect = "Error on line 1 col 6: continue"
        self.assertTrue(TestParser.test(input, expect, 241))
    
    def test_42(self):
        input = """var1: integer = -3;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))
    
    def test_43(self):
        input = """
            goo: function void() {
                for (i = 1, i < 10, i = i + 1) {
                    readInteger(i);
                }
            }
        """
        expect = "Error on line 3 col 38: ="
        self.assertTrue(TestParser.test(input, expect, 243))
    
    def test_44(self):
        input = """
            main: function void() {
                do (a != 10) while {
                    a = a - 1;
                }
            }
        """
        expect = "Error on line 3 col 19: ("
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_45(self):
        input = """
            a: integer = 6;
            main: function void() {
                a: 3;
            }
        """
        expect = "Error on line 4 col 19: 3"
        self.assertTrue(TestParser.test(input, expect, 245))
    
    def test_46(self):
        input = """
            fact: function void(out inherit a: integer) {
                /* do sth */
                {
                    // TODO
                }
            } 
        """
        expect = "Error on line 2 col 36: inherit"
        self.assertTrue(TestParser.test(input, expect, 246))
    
    def test_47(self):
        input = """arr: array [2] of integer = -{1,2};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
    
    def test_48(self):
        input = """arr: array [2] of integer = ;"""
        expect = "Error on line 1 col 28: ;"
        self.assertTrue(TestParser.test(input, expect, 248))
    
    def test_49(self):
        input = """x: integer, y: float;"""
        expect = "Error on line 1 col 10: ,"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_50(self):
        input = """
            main: function void() {
                x = goo() + -goo();
            } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_51(self):
        input = """
            main: function void() {
                do  {
                    a = a - 1;
                }
                while (a != 10)
            }
        """
        expect = "Error on line 7 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 251))
    
    def test_52(self):
        input = """
            main: function void() {
                do  {
                    a = a - 1;
                }
                while (a != 10) {
                    a = a * 2;
                }
            }
        """
        expect = "Error on line 6 col 32: {"
        self.assertTrue(TestParser.test(input, expect, 252))
    
    def test_53(self):
        input = """
            main: function void() {
                do  {
                    break a;
                }
                while (a != 10);
            }
        """
        expect = "Error on line 4 col 26: a"
        self.assertTrue(TestParser.test(input, expect, 253))
    
    def test_54(self):
        input = """
            main: function void() {
                do  {
                    cont() a;
                }
                while (a != 10);
            }
        """
        expect = "Error on line 4 col 27: a"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_55(self):
        input = """
            main: function void() {
                continue();
            }
        """
        expect = "Error on line 3 col 24: ("
        self.assertTrue(TestParser.test(input, expect, 255))
    
    def test_56(self):
        input = """
            main: function void() {
                a: string = "!@#$%^&*()";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))
    
    def test_57(self):
        input = """
            main: function void() {
                a: array [2] of integer = {1*2+5-8 || 10, 1000 && 1010};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
    
    def test_58(self):
        input = """
            main: function void() {
                while(a != 0) {
                    do {
                        a = a + 1;
                    }
                    while(a != 10);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))
    
    def test_59(self):
        input = """
            main: function void() {
                while(a != 0) {
                    do {
                        if(a == 5) {
                            a = a + 1;
                        }
                    }
                    while(a != 10);
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    # def test_60(self):
    #     input = """
    #         main: function void() {
    #             readInteger();
    #             readInteger();
    #             readInteger();
    #         } readInteger();
    #     """
    #     expect = "Error on line 6 col 14: readInteger"
    #     self.assertTrue(TestParser.test(input, expect, 260))

    def test_61(self):
        input = """
            main: function void() {
                readinteger();
                readinteger();
                readinteger();
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))
    
    # def test_62(self):
    #     input = """
    #         a: float;
    #         main: function void() {
    #             a = a + readFloat();
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 262))
    
    def test_63(self):
        input = """
            a: float;
            main: function integer(a) {
                a = a + 1;
            }
        """
        expect = "Error on line 3 col 36: )"
        self.assertTrue(TestParser.test(input, expect, 263))
    
    def test_64(self):
        input = """
            main: function integer(a: float) {
                a += 1;
            }
        """
        expect = "Error on line 3 col 18: +"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_65(self):
        input = """
            foo: function integer(a: integer) {
                bar: function integer(b: integer) {
                    /* TO DO */
                }
            }
        """
        expect = "Error on line 3 col 21: function"
        self.assertTrue(TestParser.test(input, expect, 265))
    
    def test_66(self):
        input = """
            foo: function integer(a: integer) {
                return foo(bar(a),b);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))
    
    # def test_67(self):
    #     input = """
    #         foo: function integer(a: integer) {
    #             return foo(printInteger(a),b);
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 267))
    
    def test_68(self):
        input = """
            main: function void() {
                x: array* [2] of integer;
            }
        """
        expect = "Error on line 3 col 24: *"
        self.assertTrue(TestParser.test(input, expect, 268))
    
    def test_69(self):
        input = """
            main: function void() {
                do a = 1;
                while (a != 0);
            }
        """
        expect = "Error on line 3 col 19: a"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_70(self):
        input = """
            main: function void() {
                while((a != b) && (b != c) && (c!= 0)) {
                    /*TODO */
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_71(self):
        input = """
            main: function void() {
                while(a != b && b != c && c!= 0) {
                    /*TODO */
                }
            }
        """
        expect = "Error on line 3 col 34: !="
        self.assertTrue(TestParser.test(input, expect, 271))
    
    def test_72(self):
        input = """
            main: function void() {
                while(a > b || -b) {
                    /*TODO */
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
    
    def test_73(self):
        input = """
            main: function void() {
                for(i = 0, (i < 10) && (i != a), i + 3) {
                    /* TODO */
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_74(self):
        input = """
            main: function void() {
                for(i = 0, (i < 10) && (i != a), i + 3) i = i + 1;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
    
    def test_75(self):
        input = """
            main: function void() {
                for(i = 0, (i < 10) && (i != a), i + 3)
                    /* TODO */
            }
        """
        expect = "Error on line 5 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 275))
    
    def test_76(self):
        input = """
            main: function void() {
                while(a + b != 10)
                    a = a + 1;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    
    def test_77(self):
        input = """
            main: function void() {
                if (a != 10)
                    if (a != 9)
                        if (a != 8)
                            if (a != 7)
                                return a;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
    
    def test_78(self):
        input = """
            main: function void() {
                a = b = foo();
            }
        """
        expect = "Error on line 3 col 22: ="
        self.assertTrue(TestParser.test(input, expect, 278))
    
    def test_79(self):
        input = """
            main: function void() {
                a = (b == foo());
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
    
    def test_80(self):
        input = """
            main: function void() {
                a = b :: foo();
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
    
    def test_81(self):
        input = """
            main: function void() {
                _ = _ <= _;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))
    
    def test_82(self):
        input = """
            main: function void() {
                while (True)
                    a: string = "ab" + "c";
            }
        """
        expect = "Error on line 4 col 21: :"
        self.assertTrue(TestParser.test(input, expect, 282))
    
    def test_83(self):
        input = """
            main: function void() {
                a: string = "ab" + "c";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_84(self):
        input = """
            main: function void() {
                while(a != 0)
                    do a = 1;
                    while (a != 10);
            }
        """
        expect = "Error on line 4 col 23: a"
        self.assertTrue(TestParser.test(input, expect, 284))
    
    def test_85(self):
        input = """
            fac: function integer(){
                a: float = 1_12.0e10;
                return;
            }        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))
    
    def test_86(self):
        input = """
            main: function void() {
                continue main;
            }
        """
        expect = "Error on line 3 col 25: main"
        self.assertTrue(TestParser.test(input, expect, 286))
    
    def test_87(self):
        input = """
            main: function void(a == b) {
            }
        """
        expect = "Error on line 2 col 34: =="
        self.assertTrue(TestParser.test(input, expect, 287))
    
    def test_88(self):
        input = """
            a: integer = (3 != 1) + 6;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_89(self):
        input = """
            a: integer = (3 >= 4) || (1 <= 2);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_90(self):
        input = """
            a: integer = 3 >= 4 (|| 1 <= 2);
        """
        expect = "Error on line 2 col 32: ("
        self.assertTrue(TestParser.test(input, expect, 290))
    
    def test_91(self):
        input = """
            main: function void() {
                a = [1,3] - 1.2;
            }
        """
        expect = "Error on line 3 col 20: ["
        self.assertTrue(TestParser.test(input, expect, 291))
    
    def test_92(self):
        input = """1.e10: float ;
        """
        expect = "Error on line 1 col 0: 1.e10"
        self.assertTrue(TestParser.test(input, expect, 292))
    
    def test_93(self):
        input = """
            main: function void() {
                return break;
            }
        """
        expect = "Error on line 3 col 23: break"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_94(self):
        input = """
            main: function void() {
                break {
                    a = a - 1;
                };
            }
        """
        expect = "Error on line 3 col 22: {"
        self.assertTrue(TestParser.test(input, expect, 294))
    
    def test_95(self):
        input = """main: void function() {}
        """
        expect = "Error on line 1 col 6: void"
        self.assertTrue(TestParser.test(input, expect, 295))
    
    def test_96(self):
        input = """x: void = 3;"""
        expect = "Error on line 1 col 3: void"
        self.assertTrue(TestParser.test(input, expect, 296))
    
    def test_97(self):
        input = """x: out = a;"""
        expect = "Error on line 1 col 3: out"
        self.assertTrue(TestParser.test(input, expect, 297))
    
    def test_98(self):
        input = """main: function out() {}"""
        expect = "Error on line 1 col 15: out"
        self.assertTrue(TestParser.test(input, expect, 298))

    # def test_99(self):
    #     input = """
    #         main: function void() {
    #             for (a[0] = 0, a[0] < 10, a[0] + 1)
    #                 for (b = 0, b < 10, b + 1)
    #                     super(a[b] + b[a]);
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 299))

    # def test_(self):
    #     input = "a: integer = - ! - foo();"
    #     expect = 'successful'
    #     self.assertTrue(TestParser.test(input, expect, 300))