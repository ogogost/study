class Fraction:
    delim = 0
    denom = 0

    def __init__(self, delim, denom):
        self.delim = delim
        self.denom = denom

    def plus(self, other):
        a = self.delim
        b = self.denom
        c = other_delim
        d = other_denom
        return Fraction(a * d + c * b, b * d )


    def minus(self, other):
        a = self.delim
        b = self.denom
        c = other_delim
        d = other_denom

        result_delim = (a * d) - (c * b)
        result_denom = b * d
        return

    def mul(self, other):
        a = self.delim
        b = self.denom
        c = other_delim
        d = other_denom

        result_delim = a * c
        result_denom = b * d
        return

    def div(self, other):
        a = self.delim
        b = self.denom
        c = other_delim
        d = other_denom

        result_delim = a * d
        result_denom = b * c
        return

    def to_float(self, other):
        a = self.delim
        b = self.denom
        c = other_delim
        d = other_denom

        return

    def __str__(self, other):

