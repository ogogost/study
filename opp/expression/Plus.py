from opp.expression.Expression import Expression
from opp.expression.Const import Const
from opp.expression.Div import Div
from opp.expression.Mul import Mul
from opp.expression.Minus import Minus


class Plus(Expression):
    def __init__(self, left=None, right=None):
        super().__init__(left, right)
        
    def calc(self):
        return self.left.calc() + self.right.calc()

    def str_to_tree(expr):
        """
        :type expr: str
        """
        expr.strip()
        index = expr.find('+')
        result_class = Const
        if index != -1:
           result_class = Plus
        else:
            index = expr.fing('-')
            if index != -1:
                result_class = Minus
            else:
                index = expr.find('*')
                if index != -1:
                    result_class = Mul
                else:
                    index = expr.find('/')
                    if index != -1:
                        result_class = Div
        if index != -1:
            left = str_to_tree(expr[:index])
            right = str_to_tree(expr[index + 1:])
            return result_class(left, right)
        return Const(int(expr))

print(str_to_tree('6/2 + 3 * 4 + 300/10').calc())

# str_to_tree('1+1')

print()

six = Const(6)
two = Const(2)
three = Const(3)
four = Const(4)

div = Div(six, two)
mul = Mul(three, four)

plus = Plus(div, mul)

print(plus.calc())