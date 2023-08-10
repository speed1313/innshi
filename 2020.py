
class Polynomial:
    def __init__(self, coeffs: list[int]):
        self.coeffs = coeffs
    def add(self, other: 'Polynomial'):
        result = [0] * max(len(self.coeffs), len(other.coeffs))
        for i in range(len(self.coeffs)):
            result[i] += self.coeffs[i]
        for i in range(len(other.coeffs)):
            result[i] += other.coeffs[i]
        print(result)
        return Polynomial(result)
    def mult(self, other: 'Polynomial'):
        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result[i+j] += self.coeffs[i] * other.coeffs[j]
        return Polynomial(result)
    def div(self, other: 'Polynomial'):
        
    def __str__(self) -> str:
        return " + ".join(reversed([f"{self.coeffs[i]}x^{i}" for i in range(len(self.coeffs))]))

p1 = Polynomial([1,2,3,0,2])
print(p1)
p2 = Polynomial([1,2,3,4])
print(p2)
print(p1.add(p2))
print(p1.mult(p2))
