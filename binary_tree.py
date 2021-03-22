import pprint
class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None
        
class  BinarySearchTree(object):
    def __init__(self) -> None:
        self.root = None
        
    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
            return
            
        def _insert(node: Node, value: int) -> Node:
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        _insert(self.root, value)

    def inorder(self) -> None:
        def _inorder(node: None) -> None:
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)
        
    def search(self, value: int) -> bool:        
        def _search(node: None, value: int) -> bool:
            if node is None:
                return False
            if node.value == value:
                return True
            elif node.value > value:
                return _search(node.left, value)
            elif node.value < value:
                return _search(node.right, value)
        _search(self.root, value)
    
    def min_value(self, node: None) -> None:
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def remove(self, value: int) -> None:    
        def _remove(node: None, value: int) -> None:
            if node is None:
                return node
            
            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                
                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)
            return node
        _remove(self.root, value)
    
if __name__ == '__main__':
    binaryTree = BinarySearchTree()
    binaryTree.insert(3)
    binaryTree.insert(6)
    binaryTree.insert(5)
    binaryTree.insert(7)
    binaryTree.insert(1)
    binaryTree.insert(10)
    binaryTree.insert(2)
    binaryTree.inorder()
    binaryTree.remove(6)
    binaryTree.inorder()
    # binaryTree.remove(6)
    # binaryTree.inorder()
    