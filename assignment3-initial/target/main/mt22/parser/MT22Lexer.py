# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01da\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\6\2\u0091\n\2\r\2\16\2\u0092")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\7\t\u00a7\n\t\f\t\16\t\u00aa\13\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\7\t\u00b2\n\t\f\t\16\t\u00b5\13")
        buf.write("\t\5\t\u00b7\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#")
        buf.write("\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3")
        buf.write(")\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\69\u0172\n9\r9\169\u0173")
        buf.write("\3:\3:\7:\u0178\n:\f:\16:\u017b\13:\3;\3;\5;\u017f\n;")
        buf.write("\3;\3;\3<\3<\3=\3=\3=\5=\u0188\n=\3=\7=\u018b\n=\f=\16")
        buf.write("=\u018e\13=\5=\u0190\n=\3>\3>\3>\3?\3?\3?\3?\3?\5?\u019a")
        buf.write("\n?\3?\3?\3?\3?\3?\3?\3?\5?\u01a3\n?\3@\3@\3@\3A\3A\3")
        buf.write("A\3A\5A\u01ac\nA\3B\3B\7B\u01b0\nB\fB\16B\u01b3\13B\3")
        buf.write("B\3B\3B\3C\3C\7C\u01ba\nC\fC\16C\u01bd\13C\3D\3D\7D\u01c1")
        buf.write("\nD\fD\16D\u01c4\13D\3D\5D\u01c7\nD\3D\3D\3E\3E\3E\3F")
        buf.write("\3F\7F\u01d0\nF\fF\16F\u01d3\13F\3F\3F\3F\3G\3G\3G\3\u00a8")
        buf.write("\2H\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write("\2s\2u\2w\2y\2{:};\177\2\u0081\2\u0083<\u0085=\u0087>")
        buf.write("\u0089\2\u008b?\u008d@\3\2\r\5\2\n\f\16\17\"\"\4\2\f\f")
        buf.write("\17\17\3\2\62;\4\2GGgg\4\2--//\3\2\63;\n\2$$))^^ddhhp")
        buf.write("pttvv\7\2\f\f\17\17$$))^^\5\2C\\aac|\6\2\62;C\\aac|\4")
        buf.write("\3\f\f\17\17\2\u01e4\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0083\3\2\2\2")
        buf.write("\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\3\u0090\3\2\2\2\5\u0096\3\2\2\2\7\u0098\3\2\2")
        buf.write("\2\t\u009a\3\2\2\2\13\u009c\3\2\2\2\r\u009e\3\2\2\2\17")
        buf.write("\u00a0\3\2\2\2\21\u00b6\3\2\2\2\23\u00ba\3\2\2\2\25\u00bf")
        buf.write("\3\2\2\2\27\u00c5\3\2\2\2\31\u00cd\3\2\2\2\33\u00d0\3")
        buf.write("\2\2\2\35\u00d5\3\2\2\2\37\u00db\3\2\2\2!\u00e1\3\2\2")
        buf.write("\2#\u00e5\3\2\2\2%\u00ee\3\2\2\2\'\u00f1\3\2\2\2)\u00f9")
        buf.write("\3\2\2\2+\u0100\3\2\2\2-\u0107\3\2\2\2/\u010c\3\2\2\2")
        buf.write("\61\u0111\3\2\2\2\63\u0117\3\2\2\2\65\u011b\3\2\2\2\67")
        buf.write("\u0124\3\2\2\29\u0127\3\2\2\2;\u012f\3\2\2\2=\u0135\3")
        buf.write("\2\2\2?\u0137\3\2\2\2A\u0139\3\2\2\2C\u013b\3\2\2\2E\u013d")
        buf.write("\3\2\2\2G\u013f\3\2\2\2I\u0141\3\2\2\2K\u0144\3\2\2\2")
        buf.write("M\u0147\3\2\2\2O\u014a\3\2\2\2Q\u014d\3\2\2\2S\u014f\3")
        buf.write("\2\2\2U\u0152\3\2\2\2W\u0154\3\2\2\2Y\u0157\3\2\2\2[\u015a")
        buf.write("\3\2\2\2]\u015c\3\2\2\2_\u015e\3\2\2\2a\u0160\3\2\2\2")
        buf.write("c\u0162\3\2\2\2e\u0164\3\2\2\2g\u0166\3\2\2\2i\u0168\3")
        buf.write("\2\2\2k\u016a\3\2\2\2m\u016c\3\2\2\2o\u016e\3\2\2\2q\u0171")
        buf.write("\3\2\2\2s\u0175\3\2\2\2u\u017c\3\2\2\2w\u0182\3\2\2\2")
        buf.write("y\u018f\3\2\2\2{\u0191\3\2\2\2}\u01a2\3\2\2\2\177\u01a4")
        buf.write("\3\2\2\2\u0081\u01ab\3\2\2\2\u0083\u01ad\3\2\2\2\u0085")
        buf.write("\u01b7\3\2\2\2\u0087\u01be\3\2\2\2\u0089\u01ca\3\2\2\2")
        buf.write("\u008b\u01cd\3\2\2\2\u008d\u01d7\3\2\2\2\u008f\u0091\t")
        buf.write("\2\2\2\u0090\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0090")
        buf.write("\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\u0095\b\2\2\2\u0095\4\3\2\2\2\u0096\u0097\7\"\2\2\u0097")
        buf.write("\6\3\2\2\2\u0098\u0099\7\13\2\2\u0099\b\3\2\2\2\u009a")
        buf.write("\u009b\7\n\2\2\u009b\n\3\2\2\2\u009c\u009d\7\16\2\2\u009d")
        buf.write("\f\3\2\2\2\u009e\u009f\7\17\2\2\u009f\16\3\2\2\2\u00a0")
        buf.write("\u00a1\7\f\2\2\u00a1\20\3\2\2\2\u00a2\u00a3\7\61\2\2\u00a3")
        buf.write("\u00a4\7,\2\2\u00a4\u00a8\3\2\2\2\u00a5\u00a7\13\2\2\2")
        buf.write("\u00a6\u00a5\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a9\3")
        buf.write("\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00a8")
        buf.write("\3\2\2\2\u00ab\u00ac\7,\2\2\u00ac\u00b7\7\61\2\2\u00ad")
        buf.write("\u00ae\7\61\2\2\u00ae\u00af\7\61\2\2\u00af\u00b3\3\2\2")
        buf.write("\2\u00b0\u00b2\n\3\2\2\u00b1\u00b0\3\2\2\2\u00b2\u00b5")
        buf.write("\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4")
        buf.write("\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00a2\3\2\2\2")
        buf.write("\u00b6\u00ad\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\b")
        buf.write("\t\2\2\u00b9\22\3\2\2\2\u00ba\u00bb\7c\2\2\u00bb\u00bc")
        buf.write("\7w\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be\7q\2\2\u00be\24")
        buf.write("\3\2\2\2\u00bf\u00c0\7d\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2")
        buf.write("\7g\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7m\2\2\u00c4\26")
        buf.write("\3\2\2\2\u00c5\u00c6\7d\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8")
        buf.write("\7q\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb")
        buf.write("\7c\2\2\u00cb\u00cc\7p\2\2\u00cc\30\3\2\2\2\u00cd\u00ce")
        buf.write("\7f\2\2\u00ce\u00cf\7q\2\2\u00cf\32\3\2\2\2\u00d0\u00d1")
        buf.write("\7g\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7u\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4\34\3\2\2\2\u00d5\u00d6\7h\2\2\u00d6\u00d7")
        buf.write("\7c\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7u\2\2\u00d9\u00da")
        buf.write("\7g\2\2\u00da\36\3\2\2\2\u00db\u00dc\7h\2\2\u00dc\u00dd")
        buf.write("\7n\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7c\2\2\u00df\u00e0")
        buf.write("\7v\2\2\u00e0 \3\2\2\2\u00e1\u00e2\7h\2\2\u00e2\u00e3")
        buf.write("\7q\2\2\u00e3\u00e4\7t\2\2\u00e4\"\3\2\2\2\u00e5\u00e6")
        buf.write("\7h\2\2\u00e6\u00e7\7w\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9")
        buf.write("\7e\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec")
        buf.write("\7q\2\2\u00ec\u00ed\7p\2\2\u00ed$\3\2\2\2\u00ee\u00ef")
        buf.write("\7k\2\2\u00ef\u00f0\7h\2\2\u00f0&\3\2\2\2\u00f1\u00f2")
        buf.write("\7k\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5")
        buf.write("\7g\2\2\u00f5\u00f6\7i\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8")
        buf.write("\7t\2\2\u00f8(\3\2\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb")
        buf.write("\7g\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe")
        buf.write("\7t\2\2\u00fe\u00ff\7p\2\2\u00ff*\3\2\2\2\u0100\u0101")
        buf.write("\7u\2\2\u0101\u0102\7v\2\2\u0102\u0103\7t\2\2\u0103\u0104")
        buf.write("\7k\2\2\u0104\u0105\7p\2\2\u0105\u0106\7i\2\2\u0106,\3")
        buf.write("\2\2\2\u0107\u0108\7v\2\2\u0108\u0109\7t\2\2\u0109\u010a")
        buf.write("\7w\2\2\u010a\u010b\7g\2\2\u010b.\3\2\2\2\u010c\u010d")
        buf.write("\7x\2\2\u010d\u010e\7q\2\2\u010e\u010f\7k\2\2\u010f\u0110")
        buf.write("\7f\2\2\u0110\60\3\2\2\2\u0111\u0112\7y\2\2\u0112\u0113")
        buf.write("\7j\2\2\u0113\u0114\7k\2\2\u0114\u0115\7n\2\2\u0115\u0116")
        buf.write("\7g\2\2\u0116\62\3\2\2\2\u0117\u0118\7q\2\2\u0118\u0119")
        buf.write("\7w\2\2\u0119\u011a\7v\2\2\u011a\64\3\2\2\2\u011b\u011c")
        buf.write("\7e\2\2\u011c\u011d\7q\2\2\u011d\u011e\7p\2\2\u011e\u011f")
        buf.write("\7v\2\2\u011f\u0120\7k\2\2\u0120\u0121\7p\2\2\u0121\u0122")
        buf.write("\7w\2\2\u0122\u0123\7g\2\2\u0123\66\3\2\2\2\u0124\u0125")
        buf.write("\7q\2\2\u0125\u0126\7h\2\2\u01268\3\2\2\2\u0127\u0128")
        buf.write("\7k\2\2\u0128\u0129\7p\2\2\u0129\u012a\7j\2\2\u012a\u012b")
        buf.write("\7g\2\2\u012b\u012c\7t\2\2\u012c\u012d\7k\2\2\u012d\u012e")
        buf.write("\7v\2\2\u012e:\3\2\2\2\u012f\u0130\7c\2\2\u0130\u0131")
        buf.write("\7t\2\2\u0131\u0132\7t\2\2\u0132\u0133\7c\2\2\u0133\u0134")
        buf.write("\7{\2\2\u0134<\3\2\2\2\u0135\u0136\7-\2\2\u0136>\3\2\2")
        buf.write("\2\u0137\u0138\7/\2\2\u0138@\3\2\2\2\u0139\u013a\7,\2")
        buf.write("\2\u013aB\3\2\2\2\u013b\u013c\7\61\2\2\u013cD\3\2\2\2")
        buf.write("\u013d\u013e\7\'\2\2\u013eF\3\2\2\2\u013f\u0140\7#\2\2")
        buf.write("\u0140H\3\2\2\2\u0141\u0142\7(\2\2\u0142\u0143\7(\2\2")
        buf.write("\u0143J\3\2\2\2\u0144\u0145\7~\2\2\u0145\u0146\7~\2\2")
        buf.write("\u0146L\3\2\2\2\u0147\u0148\7?\2\2\u0148\u0149\7?\2\2")
        buf.write("\u0149N\3\2\2\2\u014a\u014b\7#\2\2\u014b\u014c\7?\2\2")
        buf.write("\u014cP\3\2\2\2\u014d\u014e\7>\2\2\u014eR\3\2\2\2\u014f")
        buf.write("\u0150\7>\2\2\u0150\u0151\7?\2\2\u0151T\3\2\2\2\u0152")
        buf.write("\u0153\7@\2\2\u0153V\3\2\2\2\u0154\u0155\7@\2\2\u0155")
        buf.write("\u0156\7?\2\2\u0156X\3\2\2\2\u0157\u0158\7<\2\2\u0158")
        buf.write("\u0159\7<\2\2\u0159Z\3\2\2\2\u015a\u015b\7*\2\2\u015b")
        buf.write("\\\3\2\2\2\u015c\u015d\7+\2\2\u015d^\3\2\2\2\u015e\u015f")
        buf.write("\7]\2\2\u015f`\3\2\2\2\u0160\u0161\7_\2\2\u0161b\3\2\2")
        buf.write("\2\u0162\u0163\7\60\2\2\u0163d\3\2\2\2\u0164\u0165\7.")
        buf.write("\2\2\u0165f\3\2\2\2\u0166\u0167\7=\2\2\u0167h\3\2\2\2")
        buf.write("\u0168\u0169\7<\2\2\u0169j\3\2\2\2\u016a\u016b\7}\2\2")
        buf.write("\u016bl\3\2\2\2\u016c\u016d\7\177\2\2\u016dn\3\2\2\2\u016e")
        buf.write("\u016f\7?\2\2\u016fp\3\2\2\2\u0170\u0172\t\4\2\2\u0171")
        buf.write("\u0170\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0171\3\2\2\2")
        buf.write("\u0173\u0174\3\2\2\2\u0174r\3\2\2\2\u0175\u0179\7\60\2")
        buf.write("\2\u0176\u0178\t\4\2\2\u0177\u0176\3\2\2\2\u0178\u017b")
        buf.write("\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a")
        buf.write("t\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u017e\t\5\2\2\u017d")
        buf.write("\u017f\t\6\2\2\u017e\u017d\3\2\2\2\u017e\u017f\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180\u0181\5q9\2\u0181v\3\2\2\2")
        buf.write("\u0182\u0183\7a\2\2\u0183x\3\2\2\2\u0184\u0190\7\62\2")
        buf.write("\2\u0185\u018c\t\7\2\2\u0186\u0188\5w<\2\u0187\u0186\3")
        buf.write("\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018b")
        buf.write("\5q9\2\u018a\u0187\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a")
        buf.write("\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u0190\3\2\2\2\u018e")
        buf.write("\u018c\3\2\2\2\u018f\u0184\3\2\2\2\u018f\u0185\3\2\2\2")
        buf.write("\u0190z\3\2\2\2\u0191\u0192\5y=\2\u0192\u0193\b>\3\2\u0193")
        buf.write("|\3\2\2\2\u0194\u0195\5s:\2\u0195\u0196\5u;\2\u0196\u01a3")
        buf.write("\3\2\2\2\u0197\u0199\5y=\2\u0198\u019a\5s:\2\u0199\u0198")
        buf.write("\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019b\3\2\2\2\u019b")
        buf.write("\u019c\5u;\2\u019c\u019d\b?\4\2\u019d\u01a3\3\2\2\2\u019e")
        buf.write("\u019f\5y=\2\u019f\u01a0\5s:\2\u01a0\u01a1\b?\5\2\u01a1")
        buf.write("\u01a3\3\2\2\2\u01a2\u0194\3\2\2\2\u01a2\u0197\3\2\2\2")
        buf.write("\u01a2\u019e\3\2\2\2\u01a3~\3\2\2\2\u01a4\u01a5\7^\2\2")
        buf.write("\u01a5\u01a6\t\b\2\2\u01a6\u0080\3\2\2\2\u01a7\u01ac\n")
        buf.write("\t\2\2\u01a8\u01ac\5\177@\2\u01a9\u01aa\7^\2\2\u01aa\u01ac")
        buf.write("\7$\2\2\u01ab\u01a7\3\2\2\2\u01ab\u01a8\3\2\2\2\u01ab")
        buf.write("\u01a9\3\2\2\2\u01ac\u0082\3\2\2\2\u01ad\u01b1\7$\2\2")
        buf.write("\u01ae\u01b0\5\u0081A\2\u01af\u01ae\3\2\2\2\u01b0\u01b3")
        buf.write("\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2")
        buf.write("\u01b4\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b5\7$\2\2")
        buf.write("\u01b5\u01b6\bB\6\2\u01b6\u0084\3\2\2\2\u01b7\u01bb\t")
        buf.write("\n\2\2\u01b8\u01ba\t\13\2\2\u01b9\u01b8\3\2\2\2\u01ba")
        buf.write("\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2")
        buf.write("\u01bc\u0086\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01c2\7")
        buf.write("$\2\2\u01bf\u01c1\5\u0081A\2\u01c0\u01bf\3\2\2\2\u01c1")
        buf.write("\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2")
        buf.write("\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01c7\t")
        buf.write("\f\2\2\u01c6\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9")
        buf.write("\bD\7\2\u01c9\u0088\3\2\2\2\u01ca\u01cb\7^\2\2\u01cb\u01cc")
        buf.write("\n\b\2\2\u01cc\u008a\3\2\2\2\u01cd\u01d1\7$\2\2\u01ce")
        buf.write("\u01d0\5\u0081A\2\u01cf\u01ce\3\2\2\2\u01d0\u01d3\3\2")
        buf.write("\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d4")
        buf.write("\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d4\u01d5\5\u0089E\2\u01d5")
        buf.write("\u01d6\bF\b\2\u01d6\u008c\3\2\2\2\u01d7\u01d8\13\2\2\2")
        buf.write("\u01d8\u01d9\bG\t\2\u01d9\u008e\3\2\2\2\25\2\u0092\u00a8")
        buf.write("\u00b3\u00b6\u0173\u0179\u017e\u0187\u018c\u018f\u0199")
        buf.write("\u01a2\u01ab\u01b1\u01bb\u01c2\u01c6\u01d1\n\b\2\2\3>")
        buf.write("\2\3?\3\3?\4\3B\5\3D\6\3F\7\3G\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    BLANK = 2
    TAB = 3
    BACKSPACE = 4
    FF = 5
    CR = 6
    NEWLINE = 7
    COMMENT = 8
    AUTO = 9
    BREAK = 10
    BOOLEAN = 11
    DO = 12
    ELSE = 13
    FALSE = 14
    FLOAT = 15
    FOR = 16
    FUNCTION = 17
    IF = 18
    INTEGER = 19
    RETURN = 20
    STRING = 21
    TRUE = 22
    VOID = 23
    WHILE = 24
    OUT = 25
    CONTINUE = 26
    OF = 27
    INHERIT = 28
    ARRAY = 29
    ADDOP = 30
    SUBOP = 31
    MULOP = 32
    DIVOP = 33
    MODOP = 34
    LOG_NOT = 35
    LOG_AND = 36
    LOG_OR = 37
    EQUAL = 38
    NOT_EQUAL = 39
    LESS_THAN = 40
    LESS_EQUAL_THAN = 41
    GREATER_THAN = 42
    GREATER_EQUAL_THAN = 43
    SCOPE = 44
    LP = 45
    RP = 46
    LS = 47
    RS = 48
    PERIOD = 49
    COMMA = 50
    SEMICOLON = 51
    COLON = 52
    LB = 53
    RB = 54
    ASSIGN = 55
    INTLIT = 56
    FLOATLIT = 57
    STRINGLIT = 58
    IDENTIFIER = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61
    ERROR_CHAR = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "' '", "'\t'", "'\b'", "'\f'", "'\r'", "'\n'", "'auto'", "'break'", 
            "'boolean'", "'do'", "'else'", "'false'", "'float'", "'for'", 
            "'function'", "'if'", "'integer'", "'return'", "'string'", "'true'", 
            "'void'", "'while'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
            "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", "'{'", 
            "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "WS", "BLANK", "TAB", "BACKSPACE", "FF", "CR", "NEWLINE", "COMMENT", 
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "VOID", "WHILE", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "LOG_NOT", "LOG_AND", 
            "LOG_OR", "EQUAL", "NOT_EQUAL", "LESS_THAN", "LESS_EQUAL_THAN", 
            "GREATER_THAN", "GREATER_EQUAL_THAN", "SCOPE", "LP", "RP", "LS", 
            "RS", "PERIOD", "COMMA", "SEMICOLON", "COLON", "LB", "RB", "ASSIGN", 
            "INTLIT", "FLOATLIT", "STRINGLIT", "IDENTIFIER", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "WS", "BLANK", "TAB", "BACKSPACE", "FF", "CR", "NEWLINE", 
                  "COMMENT", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", 
                  "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
                  "STRING", "TRUE", "VOID", "WHILE", "OUT", "CONTINUE", 
                  "OF", "INHERIT", "ARRAY", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
                  "MODOP", "LOG_NOT", "LOG_AND", "LOG_OR", "EQUAL", "NOT_EQUAL", 
                  "LESS_THAN", "LESS_EQUAL_THAN", "GREATER_THAN", "GREATER_EQUAL_THAN", 
                  "SCOPE", "LP", "RP", "LS", "RS", "PERIOD", "COMMA", "SEMICOLON", 
                  "COLON", "LB", "RB", "ASSIGN", "INT_PART", "DEC_PART", 
                  "EXP_PART", "UNDERSCORE", "INTFLOAT", "INTLIT", "FLOATLIT", 
                  "ESCAPE_SEQUENCE", "STR_CHAR", "STRINGLIT", "IDENTIFIER", 
                  "UNCLOSE_STRING", "LEGAL_ESCAPE", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[60] = self.INTLIT_action 
            actions[61] = self.FLOATLIT_action 
            actions[64] = self.STRINGLIT_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[69] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text.replace("_", "")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text=self.text.replace("_", "")
     

        if actionIndex == 2:
            self.text=self.text.replace("_", "")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	if self.text[-1] in ['\n', '\r']:
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            	raise ErrorToken(self.text)

     


