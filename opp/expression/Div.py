from opp.expression.Expression import Expression

class Div(Expression):
    def __init__(self, left=None, right=None):
        super().__init__(left, right)

    def calc(self):
        return self.left.calc() / self.right.calc()
