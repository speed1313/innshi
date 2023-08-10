# base class for functions
class Function:
    def apply(self, n: int) -> int:
        return n

class PlusOne(Function):
    def apply(self, n: int) -> int:
        return n + 1
class Double(Function):
    def apply(self, n: int) -> int:
        return n * 2

def map_f(n_list: list, f: Function) -> list:
    if len(n_list) == 0:
        return []
    else:
        result = [] * len(n_list)
        for i in n_list:
            result.append(f.apply(i))
        return result

def map_lambda(n_list, f):
    if len(n_list) == 0:
        return []
    else:
        result = [] * len(n_list)
        for i in n_list:
            result.append(f(i))
        return result


print(map_f([1,2,3], Double()))
print(map_f([1,2,3], PlusOne()))

print(map_lambda([1,2,3], lambda x: x*2))
def plus(n):
    return n + 1
print(map_lambda([1,2,3], plus))