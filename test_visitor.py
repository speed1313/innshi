import pytest
import visitor


def is_same_tree(tree1, tree2):
    if isinstance(tree1, visitor.Leaf) and isinstance(tree2, visitor.Leaf):
        return True
    if isinstance(tree1, visitor.Branch) and isinstance(tree2, visitor.Branch):
        return (
            tree1.value == tree2.value
            and is_same_tree(tree1.left, tree2.left)
            and is_same_tree(tree1.right, tree2.right)
        )
    return False


def test_delete():
    tree = visitor.Branch(
        visitor.Branch(visitor.Leaf(), 1, visitor.Leaf()),
        2,
        visitor.Branch(visitor.Leaf(), 100, visitor.Leaf()),
    )
    tree = visitor.delete(tree, 1)
    assert is_same_tree(
        tree,
        visitor.Branch(
            visitor.Leaf(), 2, visitor.Branch(visitor.Leaf(), 100, visitor.Leaf())
        ),
    )
    tree = visitor.delete(tree, 2)
    assert is_same_tree(tree, visitor.Branch(visitor.Leaf(), 100, visitor.Leaf()))


def test_insert():
    tree = visitor.Leaf()
    tree = visitor.insert(tree, 1)
    tree = visitor.insert(tree, 2)
    tree = visitor.insert(tree, 3)
    assert is_same_tree(
        tree,
        visitor.Branch(
            visitor.Leaf(),
            1,
            visitor.Branch(
                visitor.Leaf(), 2, visitor.Branch(visitor.Leaf(), 3, visitor.Leaf())
            ),
        ),
    )


def test_sum():
    tree = visitor.Branch(
        visitor.Branch(visitor.Leaf(), 1, visitor.Leaf()),
        2,
        visitor.Branch(visitor.Leaf(), 100, visitor.Leaf()),
    )
    assert tree.accept(visitor.Sum()) == 103


def test_walk():
    tree = visitor.Branch(
        visitor.Branch(visitor.Leaf(), 1, visitor.Leaf()),
        2,
        visitor.Branch(visitor.Leaf(), 100, visitor.Leaf()),
    )
    tree.accept(visitor.Walk())
    assert True
