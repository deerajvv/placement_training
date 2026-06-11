class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self,node,data):
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self.insert(node.left,data)
        elif data > node.data:
            node.right = self.insert(node.right,data)
        return node
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
b1=BST()
b1.root=b1.insert(b1.root,5)
b1.root=b1.insert(b1.root,3)
b1.root=b1.insert(b1.root,1)
b1.root=b1.insert(b1.root,2)

b1.inorder(b1.root)