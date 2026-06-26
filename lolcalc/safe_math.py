import ast
import operator as op

# Allowed operators
OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
}

def safe_eval(expr: str):
    """
    Safely evaluate a math expression using Python's AST.
    Only allows numbers and math operators. No variables, no function calls,
    no attribute access, no names, no statements.
    """

    def _eval(node):
        # Literal number: 2, 3.5, etc.
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value

        # Unary operator: -3
        if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
            return OPS[type(node.op)](_eval(node.operand))

        # Binary operator: 3 + 4, 5 * 6, etc.
        if isinstance(node, ast.BinOp) and type(node.op) in OPS:
            return OPS[type(node.op)](_eval(node.left), _eval(node.right))

        # Anything else is forbidden
        raise ValueError("Invalid or unsafe expression")

    try:
        tree = ast.parse(expr, mode="eval")
        return _eval(tree.body)
    except Exception:
        raise ValueError("Invalid or unsafe expression")
