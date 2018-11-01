from gramfuzz.fields import Def, Ref, And, Or, Join, STAR, String, Opt
from config import MAX_STRING_LENGTH, MAX_CLASS_MEMBERS, MAX_BLOCK_STATEMENTS, MAX_POSTFIX_OPS, MAX_ARGUMENTS, \
    MAX_ARRAY_DECL_DIMENSION, MAX_CLASSES, MAX_EXPRESSION_REPEAT

INTEGER_LITERAL = And(
    String(charset='123456789', min=1, max=1),
    String(charset=String.charset_num, min=0, max=9),
)

IDENT = And(
    String(charset=String.charset_alpha + "_", min=1, max=1),
    String(charset=String.charset_alphanum + "_", max=MAX_STRING_LENGTH - 1),
)


class TokenDef(Def):
    cat = "token"


class TokenRef(Ref):
    cat = "token"


TokenDef("identifier ",
         IDENT)

TokenDef("integer literal ",
         INTEGER_LITERAL)

TokenDef("class", "class ")
TokenDef("{", " {\n")
TokenDef("}", "\n}")
TokenDef("(", "(")
TokenDef(")", ")")
TokenDef("[", "[")
TokenDef("]", "]")
TokenDef(";", ";")
TokenDef("public", "public ")
TokenDef("static", "static ")
TokenDef("int", "int")
TokenDef("boolean", "boolean")
TokenDef("void", "void")
TokenDef("String", "String")
TokenDef("throws", "throws ")
TokenDef("=", " = ")
TokenDef("||", " || ")
TokenDef("&&", " && ")
TokenDef("==", " == ")
TokenDef("!=", " != ")
TokenDef("<", " < ")
TokenDef("<=", " <= ")
TokenDef(">", " > ")
TokenDef(">=", " >= ")
TokenDef("+", " + ")
TokenDef("-", " - ")
TokenDef("*", " * ")
TokenDef("/", " / ")
TokenDef("%", " % ")
TokenDef("!", "!")
TokenDef(".", ".")
TokenDef(",", ", ")
TokenDef("null", "null")
TokenDef("false", "false")
TokenDef("true", "true")
TokenDef("this", "this")
TokenDef("new", "new ")
TokenDef("while", "while ")
TokenDef("if", "if ")
TokenDef("else", "else ")
TokenDef("return", "return")

Def("Program",
    Join(
        Ref("ClassDeclaration"),
        sep="\n\n",
        max=MAX_CLASSES
    ),
    cat="minijava")

Def("ClassDeclaration",
    And(
        TokenRef("class"),
        TokenRef("identifier "),
        TokenRef("{"),
        STAR(
            Ref("ClassMember"),
            sep="\n",
            max=MAX_CLASS_MEMBERS,
        ),
        TokenRef("}"),
    ))

Def("ClassMember",
    Or(
        Ref("Field"),
        Ref("Method"),
        Ref("MainMethod"),
    ))

Def("Field",
    And(
        TokenRef("public"),
        Ref("Type"),
        " ",
        TokenRef("identifier "),
        TokenRef(";"),
    ))

Def("MainMethod",
    And(
        TokenRef("public"),
        TokenRef("static"),
        TokenRef("void"),
        " ",
        TokenRef("identifier "),
        TokenRef("("),
        TokenRef("String"),
        TokenRef("["),
        TokenRef("]"),
        " ",
        TokenRef("identifier "),
        TokenRef(")"),
        " ",
        Opt(Ref("MethodRest")),
        Ref("Block"),
    ))

Def("Method",
    And(
        TokenRef("public"),
        Ref("Type"),
        " ",
        TokenRef("identifier "),
        TokenRef("("),
        Opt(Ref("Parameters")),
        TokenRef(")"),
        " ",
        Opt(Ref("MethodRest")),
        Ref("Block"),
    ))

Def("MethodRest",
    And(
        TokenRef("throws"),
        TokenRef("identifier "),
    ))

Def("Parameters",
    Or(
        Ref("Parameter"),
        And(
            Ref("Parameter"),
            TokenRef(","),
            Ref("Parameter"),
        )
    ))

Def("Parameter",
    And(
        Ref("Type"),
        " ",
        TokenRef("identifier "),
    ))

Def("Type",
    Or(
        And(
            Ref("Type"),
            TokenRef("["),
            TokenRef("]"),
        ),
        Ref("BasicType"),
    ))

Def("BasicType",
    Or(
        TokenRef("int"),
        TokenRef("boolean"),
        TokenRef("void"),
        TokenRef("identifier "),
    ))

Def("Statement",
    Or(
        Ref("Block"),
        Ref("EmptyStatement"),
        Ref("IfStatement"),
        Ref("ExpressionStatement"),
        Ref("WhileStatement"),
        Ref("ReturnStatement"),
    ))

Def("Block",
    And(
        TokenRef("{"),
        STAR(
            Ref("BlockStatement"),
            sep="\n",
            max=MAX_BLOCK_STATEMENTS,
        ),
        TokenRef("}"),
    ))

Def("BlockStatement",
    Or(
        Ref("Statement"),
        Ref("LocalVariableDeclarationStatement"),
    ))

Def("LocalVariableDeclarationStatement",
    And(
        Ref("Type"),
        " ",
        TokenRef("identifier "),
        Opt(
            And(
                TokenRef("="),
                Ref("Expression"),
            )
        ),
        TokenRef(";"),
    ))

Def("EmptyStatement",
    TokenRef(";"))

Def("WhileStatement",
    And(
        TokenRef("while"),
        TokenRef("("),
        Ref("Expression"),
        TokenRef(")"),
        " ",
        Ref("Statement"),
    ))

Def("IfStatement",
    And(
        TokenRef("if"),
        TokenRef("("),
        Ref("Expression"),
        TokenRef(")"),
        " ",
        Ref("Statement"),
        Opt(
            And(
                TokenRef("else"),
                Ref("Statement"),
            )
        )
    ))

Def("ExpressionStatement",
    And(
        Ref("Expression"),
        TokenRef(";"),
    ))

Def("ReturnStatement",
    And(
        TokenRef("return"),
        " ",
        Opt(
            Ref("Expression"),
        ),
        TokenRef(";"),
    ))

Def("Expression",
    And(
        Ref("LogicalOrExpression"),
        STAR(
            And(
                TokenRef("="),
                Ref("LogicalOrExpression"),
            ),
            sep="",
            max=MAX_EXPRESSION_REPEAT,
        ),
    ))

Def("LogicalOrExpression",
    And(
        Ref("LogicalAndExpression"),
        STAR(
            And(
                TokenRef("||"),
                Ref("LogicalAndExpression"),
            ),
            sep="",
            max=MAX_EXPRESSION_REPEAT,
        ),
    ))

Def("LogicalAndExpression",
    And(
        Ref("EqualityExpression"),
        STAR(
            And(
                TokenRef("&&"),
                Ref("EqualityExpression"),
            ),
            sep="",
            max=MAX_EXPRESSION_REPEAT,
        ),
    ))

Def("EqualityExpression",
    And(
        Ref("RelationalExpression"),
        STAR(
            And(
                Or(
                    TokenRef("=="),
                    TokenRef("!="),
                ),
                Ref("RelationalExpression"),
            ),
            sep="",
            max=MAX_EXPRESSION_REPEAT,
        ),
    ))

Def("RelationalExpression",
    And(
        Ref("AdditiveExpression"),
        STAR(
            And(
                Or(
                    TokenRef("<"),
                    TokenRef("<="),
                    TokenRef(">"),
                    TokenRef(">="),
                ),
                Ref("AdditiveExpression"),
            ),
            sep="",
            max=MAX_EXPRESSION_REPEAT,
        ),
    ))

Def("AdditiveExpression",
    And(
        Ref("MultiplicativeExpression"),
        STAR(
            And(
                Or(
                    TokenRef("+"),
                    TokenRef("-"),
                ),
                Ref("MultiplicativeExpression"),
            ),
            sep="",
            max=MAX_EXPRESSION_REPEAT,
        ),
    ))

Def("MultiplicativeExpression",
    And(
        Ref("UnaryExpression"),
        STAR(
            And(
                Or(
                    TokenRef("*"),
                    TokenRef("/"),
                    TokenRef("%"),
                ),
                Ref("UnaryExpression"),
            ),
            sep="",
            max=MAX_EXPRESSION_REPEAT,
        ),
    ))

Def("UnaryExpression",
    Or(
        Ref("PostfixExpression"),
        And(
            Or(
                TokenRef("!"),
                TokenRef("-"),
            ),
            Ref("UnaryExpression"),
        )
    ))

Def("PostfixExpression",
    And(
        Ref("PrimaryExpression"),
        STAR(
            Ref("PostfixOp"),
            sep="",
            max=MAX_POSTFIX_OPS,
        )
    ))

Def("PostfixOp",
    Or(
        Ref("MethodInvocation"),
        Ref("FieldAccess"),
        Ref("ArrayAccess"),
    ))

Def("MethodInvocation",
    And(
        TokenRef("."),
        TokenRef("identifier "),
        TokenRef("("),
        Ref("Arguments"),
        TokenRef(")"),
    ))

Def("FieldAccess",
    And(
        TokenRef("."),
        TokenRef("identifier "),
    ))

Def("ArrayAccess",
    And(
        TokenRef("["),
        Ref("Expression"),
        TokenRef("]"),
    ))

Def("Arguments",
    Opt(
        Ref("Expression"),
        STAR(
            And(
                TokenRef(","),
                Ref("Expression"),
            ),
            sep="",
            max=MAX_ARGUMENTS,
        )
    ))

Def("PrimaryExpression",
    Or(
        TokenRef("null"),
        TokenRef("false"),
        TokenRef("true"),
        TokenRef("integer literal "),
        TokenRef("identifier "),
        And(
            TokenRef("identifier "),
            TokenRef("("),
            Ref("Arguments"),
            TokenRef(")"),
        ),
        TokenRef("this"),
        And(
            TokenRef("("),
            Ref("Expression"),
            TokenRef(")"),
        ),
        Ref("NewObjectExpression"),
        Ref("NewArrayExpression"),
    ))

Def("NewObjectExpression",
    And(
        TokenRef("new"),
        TokenRef("identifier "),
        TokenRef("("),
        TokenRef(")"),
    ))

Def("NewArrayExpression",
    And(
        TokenRef("new"),
        Ref("BasicType"),
        TokenRef("["),
        Ref("Expression"),
        TokenRef("]"),
        STAR(
            TokenRef("["),
            TokenRef("]"),
            sep="",
            max=MAX_ARRAY_DECL_DIMENSION,
        ),
    ))
