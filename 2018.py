class Variable:
    def __init__(self, x):
        self.x = x

class If_stmt:
    def __init__(self, cond, then, else_):
        self.cond = cond
        self.then = then
        self.else_ = else_

class Let_stmt:
    def __init__(self, var, bind_exp, inner_exp):
        self.var = var
        self.bind_exp = bind_exp
        self.inner_exp = inner_exp

class Add:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Sub:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def eval(exp, env):
    match exp:
        case Add():
            return eval(exp.x, env) + eval(exp.y, env)
        case Sub():
            return eval(exp.x, env) - eval(exp.y, env)
        case Variable():
            for i in reversed(env):
                if exp.x in i:
                    return i[exp.x]
            print("Unbound variable:", exp.x)
            return
        case If_stmt():
            e = eval(exp.cond, env)
            if e == True:
                return eval(exp.then, env)
            else:
                return eval(exp.else_, env)
        case Let_stmt():
            e = eval(exp.bind_exp, env)
            env.append({exp.var: e})
            inner_e = eval(exp.inner_exp, env)
            env.pop()
            return inner_e
        case _:
            return exp

import random
x = random.choice([True, False])
exp = Let_stmt("x", x, If_stmt(Variable("x"), Add(2,3), 3))
env = []
print(eval(exp, env))



print(env)


env_table = { "x": 2}



def test_eval():
    exp = Let_stmt("x", True, If_stmt(Variable("x"), Add(2,3), 3))
    env = []
    assert eval(exp, env) == 5