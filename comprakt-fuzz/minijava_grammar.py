from gramfuzz.fields import *
from config import *

INTEGER_LITERAL = String(charset=String.charset_num, min=1, max=10)

IDENT = And(
    String(charset=String.charset_alpha + "_", min=1, max=1),
    String(charset=String.charset_alphanum + "_", max=14)
)

Def("Program",
    Join(
        Ref("ClassDeclaration"),
        sep="\n\n",
        max=MAX_CLASSES
    ),
    cat="minijava")

Def("ClassDeclaration",
    And(
        "class ",
        IDENT,
        " {\n",
        Opt(
            Join(
                Ref("ClassMember"),
                sep="\n",
                max=MAX_CLASS_MEMBERS,
            )
        ),
        "\n}"
    ))

Def("ClassMember",
    Or(
        Ref("Field"),
        Ref("Method"),
        Ref("MainMethod"),
    ))

Def("Field",
    And(
        "public ",
        Ref("Type"),
        " ",
        IDENT,
        ";",
    ))

Def("MainMethod",
    And(
        "public static void ",
        IDENT,
        " (String[] ",
        IDENT,
        ") ",
        Opt(Ref("MethodRest")),
        Ref("Block"),
    ))

Def("Method",
    And(
        "public ",
        Ref("Type"),
        " ",
        IDENT,
        " (",
        Opt(Ref("Parameters")),
        ") ",
        Opt(Ref("MethodRest")),
        Ref("Block"),
    ))

Def("MethodRest",
    And(
        "throws ",
        IDENT,
    ))

Def("Parameters",
    Join(
        Ref("Parameter"),
        sep=", ",
        max=MAX_PARAMETERS,
    ))

Def("Parameter",
    And(
        Ref("Type"),
        " ",
        IDENT,
    ))

Def("Type",
    Or(
        And(
            Ref("Type"),
            "[]",
        ),
        Ref("BasicType"),
    ))

Def("BasicType",
    Or(
        "int",
        "boolean",
        "void",
        IDENT
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
        " {\n",
        Join(
            Ref("BlockStatement"),
            sep="\n",
            max=MAX_BLOCK_STATEMENTS,
        ),
        "\n}"
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
        IDENT,
        Opt(
            And(
                " = ",
                Ref("Expression"),
            )
        ),
        ";"
    ))

Def("EmptyStatement",
    ";")

Def("WhileStatement",
    And(
        "while (",
        Ref("Expression"),
        ") ",
        Ref("Statement"),
    ))

Def("IfStatement",
    And(
        "if (",
        Ref("Expression"),
        ") ",
        Ref("Statement"),
        Opt(
            And(
                "else ",
                Ref("Statement"),
            )
        )
    ))

Def("ExpressionStatement",
    And(
        Ref("Expression"),
        ";"
    ))

Def("ReturnStatement",
    And(
        "return",
        Opt(
            Ref("Expression"),
        ),
        ";"
    ))

Def("Expression",
    Ref("AssignmentExpression"))

Def("AssignmentExpression",
    And(
        Ref("LogicalOrExpression"),
        Opt(
            " = ",
            Ref("AssignmentExpression"),
        )
    ))

Def("LogicalOrExpression",
    And(
        Opt(
            Ref("LogicalOrExpression"),
            " ||",
        ),
        Ref("LogicalAndExpression"),
    ))

Def("LogicalAndExpression",
    And(
        Opt(
            Ref("LogicalAndExpression"),
            " &&",
        ),
        Ref("EqualityExpression"),
    ))

Def("EqualityExpression",
    And(
        Opt(
            Ref("EqualityExpression"),
            Or(
                " ==",
                " !=",
            ),
        ),
        Ref("RelationalExpression"),
    ))

Def("RelationalExpression",
    And(
        Opt(
            Ref("RelationalExpression"),
            Or(
                " <",
                " <=",
                " >",
                " >=",
            ),
        ),
        Ref("AdditiveExpression"),
    ))

Def("AdditiveExpression",
    And(
        Opt(
            Ref("AdditiveExpression"),
            Or(
                " +",
                " -",
            ),
        ),
        Ref("MultiplicativeExpression"),
    ))

Def("MultiplicativeExpression",
    And(
        Opt(
            Ref("MultiplicativeExpression"),
            Or(
                " *",
                " /",
                " %",
            ),
        ),
        And(
            " ",
            Ref("UnaryExpression"),
        )
    ))

Def("UnaryExpression",
    Or(
        Ref("PostfixExpression"),
        And(
            Or(
                "!",
                "-",
            ),
            Ref("UnaryExpression"),
        )
    ))

Def("PostfixExpression",
    And(
        Ref("PrimaryExpression"),
        Join(
            Ref("PostfixOp"),
            sep="",
            max=MAX_POSTFIX_OPS,
        ),
    ))

Def("PostfixOp",
    Or(
        Ref("MethodInvocation"),
        Ref("FieldAccess"),
        Ref("ArrayAccess"),
    ))

Def("MethodInvocation",
    And(
        ".",
        IDENT,
        "(",
        Ref("Arguments"),
        ")",
    ))

Def("FieldAccess",
    And(
        ".",
        IDENT,
    ))

Def("ArrayAccess",
    And(
        "[",
        Ref("Expression"),
        "]",
    ))

Def("Arguments",
    Opt(
        Join(
            Ref("Expression"),
            sep=", ",
            max=MAX_ARGUMENTS,
        )
    ))

Def("PrimaryExpression",
    Or(
        "null",
        "false",
        "true",
        INTEGER_LITERAL,
        IDENT,
        And(
            IDENT,
            "(",
            Ref("Arguments"),
            ")",
        ),
        "this",
        And(
            "(",
            Ref("Expression"),
            ")",
        ),
        Ref("NewObjectExpression"),
        Ref("NewArrayExpression"),
    ))

Def("NewObjectExpression",
    And(
        "new ",
        IDENT,
        "()"
    ))

Def("NewArrayExpression",
    And(
        "new ",
        Ref("BasicType"),
        "[",
        Ref("Expression"),
        "]",
        Opt(
            Join(
                "[]",
                sep="",
                max=MAX_ARRAY_DECL_DIMENSION,
            )
        )
    ))
