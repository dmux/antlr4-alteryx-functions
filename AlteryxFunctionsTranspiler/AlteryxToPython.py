from AlteryxFunctionsTranspiler.AlteryxFunctionsVisitor import AlteryxFunctionsVisitor


class AlteryxToPythonVisitor(AlteryxFunctionsVisitor):
    def visitProg(self, ctx):
        return self.visit(ctx.expr())

    def visitIfExpr(self, ctx):
        condition = self.visit(ctx.condition())
        true_expr = self.visit(ctx.expr(0))
        false_expr = self.visit(ctx.expr(1))
        return f"({true_expr} if {condition} else {false_expr})"

    def visitIifExpr(self, ctx):
        condition = self.visit(ctx.condition())
        true_expr = self.visit(ctx.expr(0))
        false_expr = self.visit(ctx.expr(1))
        return f"({true_expr} if {condition} else {false_expr})"

    def visitSwitchExpr(self, ctx):
        expression = self.visit(ctx.expression())
        cases = [
            (self.visit(pair.expression(0)), self.visit(pair.expr()))
            for pair in ctx.casePair()
        ]
        default = self.visit(ctx.expr())
        switch_code = " + ".join(
            [f"({result} if {expression} == {case} else 0)" for case, result in cases]
        )
        return f"({switch_code} if not any([{expression} == {case} for case, _ in [{cases}]]) else {default})"

    def visitConversionExpr(self, ctx):
        function = ctx.conversionFunction().getText()
        expression = self.visit(ctx.expression())
        # Mapeando funções para Python
        conversion_map = {
            "TOBOOLEAN": "bool",
            "TODATE": "str",  # Conversão a datetime pode ser customizada
            "TONUMBER": "float",
            "ToNumber": "float",  # Garantindo tratamento para ToNumber
            "TOSTRING": "str",
        }
        python_function = conversion_map.get(function, "str")  # Padrão para str
        return f"{python_function}({expression})"
    
    def handle_operators(self, condition):
        condition = condition.replace('AND', 'and').replace('OR', 'or')
        return condition

    def visitCondition(self, ctx):
        return self.visit(ctx.expression())

    def visitExpression(self, ctx):
        if ctx.TEXT():
            return ctx.TEXT().getText()
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        if ctx.BOOLEAN():
            return ctx.BOOLEAN().getText()
        if ctx.expr():
            return f"({self.visit(ctx.expr())})"
        


