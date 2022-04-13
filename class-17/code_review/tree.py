class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
    
    def pre_order(self):
        output = []
        def _traverse(_root):
            output.append(_root.value)
            if _root.left is not None:
                _traverse(_root.left)
            if _root.right is not None:
                _traverse(_root.right)
            return output
        return _traverse

    def find_max(self):
        _max = self.root.value
        def _traverse(node):
            nonlocal _max
            # compare current value with _max
            _max = node.value if node.value > _max else _max
            # recursivley call closure function for
            if node.left:
                _traverse(node.left)
            if node.right:
                _traverse(node.right)
        
        _traverse(self.root)

        return  _max
        




def create_tree():
    tree=Tree()
    tree.root=Node(5)
    tree.root.left=Node(8)
    tree.root.right=Node(12)
    tree.root.left.left=Node(-2)
    tree.root.left.right=Node(6)
    tree.root.right.left=Node(1)
    return tree


if __name__ == "__main__":
    tree = create_tree()
    traverse = tree.pre_order()
    print(traverse(tree.root))