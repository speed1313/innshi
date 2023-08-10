class Instruction:
    def __init__(self, name: str, arg: None | int | list['Instruction'] = None):
        self.name=name
        self.arg=arg


def eval(insts: list[Instruction], stack: list[int]):
    for _, i in enumerate(insts):
        match i.name:
            case "plus":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            case "push":
                if isinstance(i.arg, int):
                    stack.append(i.arg)
            case "dup":
                stack.append(stack[-1])
            case "minus":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            case "pop":
                stack.pop()
            case "whilenz":
                while stack[-1]!=0:
                    # if the type of i.arg is list, then it is a list of instructions
                    if isinstance(i.arg, list):
                        eval(i.arg,stack)

            case "whilegt1":
                while len(stack)>1:
                    if isinstance(i.arg, list):
                        eval(i.arg,stack)
            case _:
                print("Unkown instruction:", i.name)
                return



stack: list[int] = []
Insts = [Instruction("push",5), Instruction("dup"), Instruction("minus"), Instruction("pop")]
eval(Insts,stack)
print(stack)
stack = [10]
Insts = [Instruction("whilenz", [Instruction("dup"), Instruction("push",1), Instruction("minus")]),Instruction("whilegt1",[Instruction("plus")])]
eval(Insts,stack)

print(stack)


def test_eval():
    stack = []
    Insts = [Instruction("push",5), Instruction("dup"), Instruction("minus"), Instruction("pop")]
    eval(Insts,stack)
    assert stack == []
    stack = [10]
    Insts = [Instruction("whilenz", [Instruction("dup"), Instruction("push",1), Instruction("minus")]),Instruction("whilegt1",[Instruction("plus")])]
    eval(Insts,stack)
    assert stack == [55]