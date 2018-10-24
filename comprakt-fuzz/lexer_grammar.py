from gramfuzz.fields import *
from minijava_grammar import IDENT, INTEGER_LITERAL, TokenDef, TokenRef
from config import COMMENTS_ENABLED

TokenDef("identifier ",
         IDENT)

TokenDef("integer literal ",
         INTEGER_LITERAL)

TokenDef("!=", "!=")
TokenDef("!", "!")
TokenDef("(", "(")
TokenDef(")", ")")
TokenDef("*=", "*=")
TokenDef("*", "*")
TokenDef("++", "++")
TokenDef("+=", "+=")
TokenDef("+", "+")
TokenDef(",", ",")
TokenDef("-=", "-=")
TokenDef("--", "--")
TokenDef("-", "-")
TokenDef(".", ".")
TokenDef("/=", "/=")
TokenDef("/", "/")
TokenDef(":", ":")
TokenDef(";", ";")
TokenDef("<<=", "<<=")
TokenDef("<<", "<<")
TokenDef("<=", "<=")
TokenDef("<", "<")
TokenDef("==", "==")
TokenDef("=", "=")
TokenDef(">=", ">=")
TokenDef(">>=", ">>=")
TokenDef(">>>=", ">>>=")
TokenDef(">>>", ">>>")
TokenDef(">>", ">>")
TokenDef(">", ">")
TokenDef("?", "?")
TokenDef("%=", "%=")
TokenDef("%", "%")
TokenDef("&=", "&=")
TokenDef("&&", "&&")
TokenDef("&", "&")
TokenDef("[", "[")
TokenDef("]", "]")
TokenDef("^=", "^=")
TokenDef("^", "^")
TokenDef("{", "{")
TokenDef("}", "}")
TokenDef("~", "~")
TokenDef("|=", "|=")
TokenDef("||", "||")
TokenDef("|", "|")

OP_SEP = Or(
    TokenRef("!="),
    TokenRef("!"),
    TokenRef("("),
    TokenRef(")"),
    TokenRef("*="),
    TokenRef("*"),
    TokenRef("++"),
    TokenRef("+="),
    TokenRef("+"),
    TokenRef(","),
    TokenRef("-="),
    TokenRef("--"),
    TokenRef("-"),
    TokenRef("."),
    TokenRef("/="),
    TokenRef("/"),
    TokenRef(":"),
    TokenRef(";"),
    TokenRef("<<="),
    TokenRef("<<"),
    TokenRef("<="),
    TokenRef("<"),
    TokenRef("=="),
    TokenRef("="),
    TokenRef(">="),
    TokenRef(">>="),
    TokenRef(">>>="),
    TokenRef(">>>"),
    TokenRef(">>"),
    TokenRef(">"),
    TokenRef("?"),
    TokenRef("%="),
    TokenRef("%"),
    TokenRef("&="),
    TokenRef("&&"),
    TokenRef("&"),
    TokenRef("["),
    TokenRef("]"),
    TokenRef("^="),
    TokenRef("^"),
    TokenRef("{"),
    TokenRef("}"),
    TokenRef("~"),
    TokenRef("|="),
    TokenRef("||"),
    TokenRef("|"),
)

TokenDef("abstract", "abstract")
TokenDef("assert", "assert")
TokenDef("boolean", "boolean")
TokenDef("break", "break")
TokenDef("byte", "byte")
TokenDef("case", "case")
TokenDef("catch", "catch")
TokenDef("char", "char")
TokenDef("class", "class")
TokenDef("const", "const")
TokenDef("continue", "continue")
TokenDef("default", "default")
TokenDef("double", "double")
TokenDef("do", "do")
TokenDef("else", "else")
TokenDef("enum", "enum")
TokenDef("extends", "extends")
TokenDef("false", "false")
TokenDef("finally", "finally")
TokenDef("final", "final")
TokenDef("float", "float")
TokenDef("for", "for")
TokenDef("goto", "goto")
TokenDef("if", "if")
TokenDef("implements", "implements")
TokenDef("import", "import")
TokenDef("instanceof", "instanceof")
TokenDef("interface", "interface")
TokenDef("int", "int")
TokenDef("long", "long")
TokenDef("native", "native")
TokenDef("new", "new")
TokenDef("null", "null")
TokenDef("package", "package")
TokenDef("private", "private")
TokenDef("protected", "protected")
TokenDef("public", "public")
TokenDef("return", "return")
TokenDef("short", "short")
TokenDef("static", "static")
TokenDef("strictfp", "strictfp")
TokenDef("super", "super")
TokenDef("switch", "switch")
TokenDef("synchronized", "synchronized")
TokenDef("this", "this")
TokenDef("throws", "throws")
TokenDef("throw", "throw")
TokenDef("transient", "transient")
TokenDef("true", "true")
TokenDef("try", "try")
TokenDef("void", "void")
TokenDef("volatile", "volatile")
TokenDef("while", "while")

KEYWORDS = Or(
    TokenRef("abstract"),
    TokenRef("assert"),
    TokenRef("boolean"),
    TokenRef("break"),
    TokenRef("byte"),
    TokenRef("case"),
    TokenRef("catch"),
    TokenRef("char"),
    TokenRef("class"),
    TokenRef("const"),
    TokenRef("continue"),
    TokenRef("default"),
    TokenRef("double"),
    TokenRef("do"),
    TokenRef("else"),
    TokenRef("enum"),
    TokenRef("extends"),
    TokenRef("false"),
    TokenRef("finally"),
    TokenRef("final"),
    TokenRef("float"),
    TokenRef("for"),
    TokenRef("goto"),
    TokenRef("if"),
    TokenRef("implements"),
    TokenRef("import"),
    TokenRef("instanceof"),
    TokenRef("interface"),
    TokenRef("int"),
    TokenRef("long"),
    TokenRef("native"),
    TokenRef("new"),
    TokenRef("null"),
    TokenRef("package"),
    TokenRef("private"),
    TokenRef("protected"),
    TokenRef("public"),
    TokenRef("return"),
    TokenRef("short"),
    TokenRef("static"),
    TokenRef("strictfp"),
    TokenRef("super"),
    TokenRef("switch"),
    TokenRef("synchronized"),
    TokenRef("this"),
    TokenRef("throws"),
    TokenRef("throw"),
    TokenRef("transient"),
    TokenRef("true"),
    TokenRef("try"),
    TokenRef("void"),
    TokenRef("volatile"),
    TokenRef("while"),
)

WHITESPACES = Or(" ", "\n", "\r", "\t")

if COMMENTS_ENABLED:
    COMMENT = And(
        "/*",
        Join(
            Or(
                IDENT,
                WHITESPACES,
                Opt("/*"),
            ),
            sep=" ",
            max=10,
        ),
        Opt("*/")
    )
else:
    COMMENT = String(min=0, max=0)

Def("TokenString",
    Join(
        Or(
            TokenRef("identifier "),
            TokenRef("integer literal "),
            COMMENT,
            WHITESPACES,
            KEYWORDS,
            OP_SEP,
        ),
        sep=" ",
        max=100,
    ),
    cat="minijava_lex")
