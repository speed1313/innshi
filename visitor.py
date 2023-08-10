class Leaf:
    def __init__(self):
        pass
    def accept(self, visitor):
        return visitor.case_leaf(self)

class Branch:
    def __init__(self, left,v, right):
        self.value = v
        self.left = left
        self.right = right
    def accept(self, visitor):
        return visitor.case_branch(self.left, self.value, self.right)


class Find:
    def __init__(self, value):
        self.value = value
    def case_leaf(self, leaf):
        return False
    def case_branch(self, left, v, right):
        if self.value == v:
            return True
        elif self.value < v:
            return left.accept(self)
        else:
            return right.accept(self)

class Walk:
    def __init__(self):
        pass
    def case_leaf(self, leaf):
        pass
    def case_branch(self, left, v, right):
        left.accept(self)
        print(v)
        right.accept(self)

tree = Branch(Branch(Leaf(), 1, Leaf()), 2, Branch(Leaf(), 100, Leaf()))
tree.accept(Walk())

class Sum:
    def __init__(self):
        self.total = 0
    def case_leaf(self, leaf):
        pass
    def case_branch(self, left, v, right):
        self.total += v
        left.accept(self)
        right.accept(self)
        return self.total
print(tree.accept(Sum()))

def insert(tree, n):
    if isinstance(tree, Leaf):
        return Branch(Leaf(), n, Leaf())
    else:
        if n == tree.value:
            return tree
        elif n < tree.value:
            tree.left = insert(tree.left, n)
            return tree
        else:
            tree.right = insert(tree.right, n)
            return tree
def min(tree):
    if isinstance(tree, Leaf):
        return tree
    else:
        if isinstance(tree.left, Leaf):
            return tree.value
        else:
            return min(tree.left)

def delete(tree, n):
    if isinstance(tree, Leaf):
        return tree
    else:
        if n == tree.value:
            if isinstance(tree.left, Leaf):
                return tree.right
            elif isinstance(tree.right, Leaf):
                return tree.left
            else:
                right_min  = min(tree.right)
                tree.value = right_min
                tree.right = delete(tree.right, right_min)
                return tree
        elif n < tree.value:
            return Branch(delete(tree.left, n), tree.value, tree.right)
        else:
            return Branch(tree.left, tree.value, delete(tree.right, n))

tree_2 = insert(tree, 10000)
tree_2 = insert(tree_2, 4)
tree_2.accept(Walk())
tree_2 = delete(tree_2, 10000)
tree_2 = delete(tree_2, 4)
print("after delete")
tree_2.accept(Walk())
