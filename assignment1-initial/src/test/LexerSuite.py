import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_00(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test('$abc', 'Error Token $', 100))
    
    def test_01(self):
        self.assertTrue(TestLexer.test('"I \f wish \n you \r a good day \t\t\t\t"', 'Unclosed String: I \f wish ', 101))
    
    def test_02(self):
        self.assertTrue(TestLexer.test("/*do sth*/", "<EOF>", 102))

    def test_03(self):
        self.assertTrue(TestLexer.test("//TODO", "<EOF>", 103))
    
    def test_04(self):
        self.assertTrue(TestLexer.test("/*dosth", "/,*,dosth,<EOF>", 104))

    def test_05(self):
        self.assertTrue(TestLexer.test("WriteLn", "WriteLn,<EOF>", 105))
    
    def test_06(self):
        self.assertTrue(TestLexer.test("__", "__,<EOF>", 106))

    def test_07(self):
        self.assertTrue(TestLexer.test("0a", "0,a,<EOF>", 107))

    def test_08(self):
        self.assertTrue(TestLexer.test('"\\a"', "Illegal Escape In String: \\a", 108))
    
    def test_09(self):
        self.assertTrue(TestLexer.test('"\\n" "\n"', "\\n,Unclosed String: ", 109))
    
    def test_10(self):
        self.assertTrue(TestLexer.test('"\t"', '\t,<EOF>', 110))

    def test_11(self):
        self.assertTrue(TestLexer.test('//cmt/*', '<EOF>', 111))
    
    def test_12(self):
        self.assertTrue(TestLexer.test('\" \\a \"', 'Illegal Escape In String:  \\a', 112))
    
    def test_13(self):
        self.assertTrue(TestLexer.test('main: function void() {}', 'main,:,function,void,(,),{,},<EOF>', 113))
    
    def test_14(self):
        self.assertTrue(TestLexer.test('"', 'Unclosed String: ', 114))

    def test_15(self):
        self.assertTrue(TestLexer.test('{1, "HCM \n U \b T", true}', '{,1,,,Unclosed String: HCM ', 115))
    
    def test_16(self):
        self.assertTrue(TestLexer.test('a=5; // A C++ style comment', 'a,=,5,;,<EOF>', 116))
    
    def test_17(self):
        self.assertTrue(TestLexer.test('123012_12', '12301212,<EOF>', 117))
    
    def test_18(self):
        self.assertTrue(TestLexer.test('"This is a string containing tab \\t"', 'This is a string containing tab \\t,<EOF>', 118))
    
    def test_19(self):
        input = """
        /* hehe
                hehehe 
                        hehehehehe */
        """
        self.assertTrue(TestLexer.test(input, '<EOF>', 119))

    def test_20(self):
        self.assertTrue(TestLexer.test('12_3.e-10', '123.e-10,<EOF>', 120))

    def test_21(self):
        self.assertTrue(TestLexer.test('.45e11', '.45e11,<EOF>', 121))
    
    def test_22(self):
        self.assertTrue(TestLexer.test('123.45', '123.45,<EOF>', 122))
    
    def test_23(self):
        self.assertTrue(TestLexer.test('123.', '123.,<EOF>', 123))
    
    def test_24(self):
        self.assertTrue(TestLexer.test('123.45E-6', '123.45E-6,<EOF>', 124))

    def test_25(self):
        self.assertTrue(TestLexer.test('.E11', '.E11,<EOF>', 125))
    
    def test_26(self):
        self.assertTrue(TestLexer.test('"HCMUT \n University"', 'Unclosed String: HCMUT ', 126))
    
    def test_27(self):
        self.assertTrue(TestLexer.test("\"He asked me: \\\" Where is John? \\\" \n", "Unclosed String: He asked me: \\\" Where is John? \\\" ", 127))
    
    def test_28(self):
        self.assertTrue(TestLexer.test('"\w"', "Illegal Escape In String: \w", 128))
    
    def test_29(self):
        self.assertTrue(TestLexer.test('1__1', '1,__1,<EOF>', 129))

    def test_30(self):
        input = """
            \a \b \c \d \e \f \g \h \i \j \k
            """
        self.assertTrue(TestLexer.test(input, "Error Token \a", 130))

    def test_31(self):
        self.assertTrue(TestLexer.test('"Test string: ', 'Unclosed String: Test string: ', 131))
    
    def test_32(self):
        self.assertTrue(TestLexer.test('123_45_6.7_89E10e11', '123456.7,_89E10e11,<EOF>', 132))
    
    def test_33(self):
        self.assertTrue(TestLexer.test('"\\ "', 'Illegal Escape In String: \ ', 133))
    
    def test_34(self):
        self.assertTrue(TestLexer.test('"This is \ " a string \\" containing \\" \b \\""', 'Illegal Escape In String: This is \ ', 134))

    def test_35(self):
        self.assertTrue(TestLexer.test("\"This \\' is a \\' string", "Unclosed String: This \\' is a \\' string", 135))
    
    def test_36(self):
        self.assertTrue(TestLexer.test('0000.00000e0', '0,0,0,0.00000e0,<EOF>', 136))
    
    def test_37(self):
        input = """ 
            \n\n\n\n \t \b \r \f
        """
        self.assertTrue(TestLexer.test(input, '<EOF>', 137))
    
    def test_38(self):
        self.assertTrue(TestLexer.test('printInteger(3+2);', 'printInteger,(,3,+,2,),;,<EOF>', 138))
    
    def test_39(self):
        self.assertTrue(TestLexer.test('return n * fact(3);', 'return,n,*,fact,(,3,),;,<EOF>', 139))

    def test_40(self):
        input = """
            \n \n \n \"\t\t\t\t\" \t \t \t \b \b
        """
        self.assertTrue(TestLexer.test(input, '				,<EOF>', 140))

    def test_41(self):
        input = """
            "\"\"\"\"\"\"\"\"\""
        """
        self.assertTrue(TestLexer.test(input, ',,,,,Unclosed String: ', 141))
    
    def test_42(self):
        self.assertTrue(TestLexer.test('3+1-5*6/7%8', '3,+,1,-,5,*,6,/,7,%,8,<EOF>', 142))
    
    def test_43(self):
        self.assertTrue(TestLexer.test('// Comments combined /**/ Result', '<EOF>', 143))
    
    def test_44(self):
        self.assertTrue(TestLexer.test('"Another comment // say something"', 'Another comment // say something,<EOF>', 144))

    def test_45(self):
        self.assertTrue(TestLexer.test('arr[1+1,2+2]', 'arr,[,1,+,1,,,2,+,2,],<EOF>', 145))
    
    def test_46(self):
        input = """
            fac: function integer(){
                a: float = 1_12.0e10;
                return;
            }        
        """
        self.assertTrue(TestLexer.test(input, 'fac,:,function,integer,(,),{,a,:,float,=,112.0e10,;,return,;,},<EOF>', 146))
    
    def test_47(self):
        self.assertTrue(TestLexer.test('"\"', ',<EOF>', 147))
    
    def test_48(self):
        self.assertTrue(TestLexer.test('"""', ',Unclosed String: ', 148))
    
    def test_49(self):
        self.assertTrue(TestLexer.test('"\\"', 'Unclosed String: \\"', 149))

    def test_50(self):
        self.assertTrue(TestLexer.test('"I\'m a student"', 'Error Token "', 150))

    def test_51(self):
        self.assertTrue(TestLexer.test('1+2"2==2"', '1,+,2,2==2,<EOF>', 151))
    
    def test_52(self):
        self.assertTrue(TestLexer.test('Try a comment: /* do somthing */ */ */ /* ;', 'Try,a,comment,:,*,/,*,/,/,*,;,<EOF>', 152))
    
    def test_53(self):
        self.assertTrue(TestLexer.test('Try a comment: /* /* do sth */ /*', 'Try,a,comment,:,/,*,<EOF>', 153))
    
    def test_54(self):
        self.assertTrue(TestLexer.test('"', 'Unclosed String: ', 154))

    def test_55(self):
        self.assertTrue(TestLexer.test('expression: !((1+2)*arr[2,1])', 'expression,:,!,(,(,1,+,2,),*,arr,[,2,,,1,],),<EOF>', 155))
    
    def test_56(self):
        self.assertTrue(TestLexer.test('\"Aiyo whassup \\b bro \\n "', 'Aiyo whassup \\b bro \\n ,<EOF>', 156))
    
    def test_57(self):
        self.assertTrue(TestLexer.test('__ab__ 1__ab', '__ab__,1,__ab,<EOF>', 157))
    
    def test_58(self):
        self.assertTrue(TestLexer.test('while (a < n) a++;', 'while,(,a,<,n,),a,+,+,;,<EOF>', 158))
    
    def test_59(self):
        self.assertTrue(TestLexer.test('\"True\" + \"False\"\"', 'True,+,False,Unclosed String: ', 159))

    def test_60(self):
        input = """ 
            foo(x, y: integer) {
                do {
                    a = 1;
                }
                while (a != 0)
            }
        """ 
        self.assertTrue(TestLexer.test(input, 'foo,(,x,,,y,:,integer,),{,do,{,a,=,1,;,},while,(,a,!=,0,),},<EOF>', 160))

    def test_61(self):
        self.assertTrue(TestLexer.test('123 && 110', '123,&&,110,<EOF>', 161))
    
    def test_62(self):
        input = """
            auto break boolean do else false float for function if integer return string true while for out continue of inherit array
        """
        self.assertTrue(TestLexer.test(input, 'auto,break,boolean,do,else,false,float,for,function,if,integer,return,string,true,while,for,out,continue,of,inherit,array,<EOF>', 162))
    
    def test_63(self):
        self.assertTrue(TestLexer.test('truetruetruefalsefalse', 'truetruetruefalsefalse,<EOF>', 163))
    
    def test_64(self):
        self.assertTrue(TestLexer.test('0x123', '0,x123,<EOF>', 164))

    def test_65(self):
        self.assertTrue(TestLexer.test('=====', '==,==,=,<EOF>', 165))
    
    def test_66(self):
        self.assertTrue(TestLexer.test('()[]{};', '(,),[,],{,},;,<EOF>', 166))
    
    def test_67(self):
        self.assertTrue(TestLexer.test('>>=<<=::||!!', '>,>=,<,<=,::,||,!,!,<EOF>', 167))
    
    def test_68(self):
        self.assertTrue(TestLexer.test('x,y: array [2,3] of integer', 'x,,,y,:,array,[,2,,,3,],of,integer,<EOF>', 168))
    
    def test_69(self):
        self.assertTrue(TestLexer.test('a, b, c, d: integer = 3, 4, 6;', 'a,,,b,,,c,,,d,:,integer,=,3,,,4,,,6,;,<EOF>', 169))

    def test_70(self):
        self.assertTrue(TestLexer.test('"\\\\\\\\\\\\\\\\\r"', 'Unclosed String: \\\\\\\\\\\\\\\\', 170))

    def test_71(self):
        self.assertTrue(TestLexer.test('rrrrrr"\\r"', 'rrrrrr,\\r,<EOF>', 171))
    
    def test_72(self):
        input = """
            {
                r = 2.0E12;
                s = r * r * myPI;
                a[0] = s;
        }
        """
        self.assertTrue(TestLexer.test(input, '{,r,=,2.0E12,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>', 172))
    
    def test_73(self):
        self.assertTrue(TestLexer.test('goo();', 'goo,(,),;,<EOF>', 173))
    
    def test_74(self):
        self.assertTrue(TestLexer.test('break;', 'break,;,<EOF>', 174))

    def test_75(self):
        input = """
            for (i = 1, i < 10, i + 1) {
                writeInt(i);
        }
        """
        self.assertTrue(TestLexer.test(input, 'for,(,i,=,1,,,i,<,10,,,i,+,1,),{,writeInt,(,i,),;,},<EOF>', 175))
    
    def test_76(self):
        self.assertTrue(TestLexer.test("\"How \\b are \\\\ you?\"", "How \\b are \\\\ you?,<EOF>", 176))
    
    def test_77(self):
        self.assertTrue(TestLexer.test('"How \\\ are \\b you?"', 'How \\\ are \\b you?,<EOF>', 177))
    
    def test_78(self):
        self.assertTrue(TestLexer.test('"Troi $"', 'Troi $,<EOF>', 178))
    
    def test_79(self):
        self.assertTrue(TestLexer.test('"$$$"_abc', '$$$,_abc,<EOF>', 179))

    def test_80(self):
        self.assertTrue(TestLexer.test('\"$\"$\"$\"', '$,Error Token $', 180))

    def test_81(self):
        self.assertTrue(TestLexer.test('from google.colab import files', 'from,google,.,colab,import,files,<EOF>', 181))
    
    def test_82(self):
        self.assertTrue(TestLexer.test('"\\B"', 'Illegal Escape In String: \\B', 182))
    
    def test_83(self):
        self.assertTrue(TestLexer.test('!@#$%^&*()', '!,Error Token @', 183))
    
    def test_84(self):
        input = """
            pid PID;
            PID = fork();
        """
        self.assertTrue(TestLexer.test(input, 'pid,PID,;,PID,=,fork,(,),;,<EOF>', 184))

    def test_85(self):
        self.assertTrue(TestLexer.test('1<<>>2', '1,<,<,>,>,2,<EOF>', 185))
    
    def test_86(self):
        self.assertTrue(TestLexer.test('_______ab123cde_.E10F', '_______ab123cde_,.E10,F,<EOF>', 186))
    
    def test_87(self):
        self.assertTrue(TestLexer.test('_ab123cde_456_7.E10F', '_ab123cde_456_7,.E10,F,<EOF>', 187))
    
    def test_88(self):
        input = """
            whille(true) {
                load() ;
            }
        """
        self.assertTrue(TestLexer.test(input, 'whille,(,true,),{,load,(,),;,},<EOF>', 188))
    
    def test_89(self):
        self.assertTrue(TestLexer.test("For example: 'single quote'", "For,example,:,Error Token '", 189))

    def test_90(self):
        input = """
            {
                // say something
            }
        """
        self.assertTrue(TestLexer.test(input, '{,},<EOF>', 190))

    def test_91(self):
        input = """
            //{
                // say something
            /*} */
        """
        self.assertTrue(TestLexer.test(input, '<EOF>', 191))
    
    def test_92(self):
        self.assertTrue(TestLexer.test('inherit out identifier: type', 'inherit,out,identifier,:,type,<EOF>', 192))
    
    def test_93(self):
        self.assertTrue(TestLexer.test('"what if there is a space \\t between a space \t', 'Unclosed String: what if there is a space \\t between a space \t', 193))
    
    def test_94(self):
        self.assertTrue(TestLexer.test('\T', 'Error Token \\', 194))

    def test_95(self):
        input = """
            \\"\"\"\"\"\"\"\"\"
        """
        self.assertTrue(TestLexer.test(input, 'Error Token \\', 195))
    
    def test_96(self):
        self.assertTrue(TestLexer.test('/* a: integer = 5 *7/**/', '<EOF>', 196))
    
    def test_97(self):
        self.assertTrue(TestLexer.test("\"\\'\\'\"", "\\'\\',<EOF>", 197))
    
    def test_98(self):
        self.assertTrue(TestLexer.test('"\\\\"', '\\\\,<EOF>', 198))
    
    def test_99(self):
        input = """
            "Hello ' teacher"
        """
        self.assertTrue(TestLexer.test(input, 'Error Token "', 199))
