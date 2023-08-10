
class Const:
    def __init__(self, i):
        self.i = i

class Variable:
    def __init__(self, x):
        self.x = x

class Add:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Mult:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Parser:
    def __init__(self, program):
        self.program = program
        self.loc = 0
    def peek(self):
        if self.loc > len(self.program):
            return None
        self.loc += 1
        return self.loc

    def expr(self):
        lh = self.mul()
        while (self.loc < len(self.program)):
            if self.program[self.loc] == "+":
                if self.peek() == None:
                    return lh
                rh = self.mul()
                lh = Add(lh, rh)
            else:
                break
        return lh

    def mul(self):
        lh = self.primary()

        if self.loc >= len(self.program):
            print("here")
        while (self.loc < len(self.program)):
            if self.program[self.loc] == "*":
                if self.peek() == None:
                    return lh
                rh = self.primary()
                lh = Mult(lh, rh)
            else:
                break
        return lh

    def primary(self):
        self.peek()
        return self.program[self.loc - 1]


program = [Const(4), "*", Variable("x"), "+", Const(5)]

def print_exp(exp):
    if isinstance(exp, Const):
        print(exp.i)
    elif isinstance(exp, Variable):
        print(exp.x)
    elif isinstance(exp, Add):
        print_exp(exp.x)
        print("+")
        print_exp(exp.y)
    elif isinstance(exp, Mult):
        print_exp(exp.x)
        print("*")
        print_exp(exp.y)
    else:
        print("error")
exp = Parser(program).expr()
print(exp.x)
print(exp.y)
print_exp(exp)



def simplifyZero(exp):
    if isinstance(exp, Add):
        if isinstance(simplifyZero(exp.x), Const) and simplifyZero(exp.x).i == 0:
            return simplifyZero(exp.y)
        if isinstance(simplifyZero(exp.y), Const) and simplifyZero(exp.y).i == 0:
            return simplifyZero(exp.x)
        return Add(simplifyZero(exp.x), simplifyZero(exp.y))
    if isinstance(exp, Mult):
        if isinstance(simplifyZero(exp.x), Const) and simplifyZero(exp.x).i == 0:
            return Const(0)
        if isinstance(simplifyZero(exp.y), Const) and simplifyZero(exp.y).i == 0:
            return Const(0)
        return Mult(simplifyZero(exp.x), simplifyZero(exp.y))
    if isinstance(exp, Const):
        return exp
    if isinstance(exp, Variable):
        return exp

print("simplifyZero")
program = [Const(4), "*", Variable("x"), "+", Const(0)]
print_exp(simplifyZero(Parser(program).expr()))

print("example2")
program = [Const(0), "*", Variable("x"), "+", Const(5)]
print_exp(simplifyZero(Parser(program).expr()))





def is_same(exp1, exp2):
    if exp1.__class__ != exp2.__class__:
        return False
    else:
        if isinstance(exp1, Const):
            return exp1.i == exp2.i
        if isinstance(exp1, Variable):
            return exp1.x == exp2.x
        if isinstance(exp1, Add):
            return is_same(exp1.x, exp2.x) and is_same(exp1.y, exp2.y)
        if isinstance(exp1, Mult):
            return is_same(exp1.x, exp2.x) and is_same(exp1.y, exp2.y)
        return False

def test_simplify():
    exp = Add(Const(4), Mult(Const(0), Variable("x")))
    assert is_same(simplifyZero(exp), Const(4))
    exp = Add(Const(4), Mult(Const(1), Variable("x")))
    assert is_same(simplifyZero(exp), exp)
    exp = Mult(Const(0), Variable("x"))
    assert is_same(simplifyZero(exp), Const(0))
