def fib(n: int, a: int, b: int) -> int:
    if n == 1:
        return b
    else:
        return fib(n-1, b, a+b)

# print(fib(40222, 1, 1))


class Double:

    def apply(self, n : int) -> int:
        return n * 2

f = Double()
result = f.apply(5)
print(result)
def sum(n: int, f: Double) -> int:
    if n == 0:
        return 0
    else:
        return f.apply(n) + sum(n-1, f)

print(sum(2, f))



