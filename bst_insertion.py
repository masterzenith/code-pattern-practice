class Node:
    def __init__(self, key):
        self.data = key
        self.left = self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end= ' ')
    inorder(root.right)

def insert(root, key):
    curr = root
    parent = None
    if root is None:
        return Node(key)
    while curr:
        parent = curr
        if key < curr.data:
            curr = curr.left
        else:
            curr = curr.right
    if key < parent.data:
        parent.left = Node(key)
    else:
        parent.right = Node(key)
    return root

def constructBST(keys):
    root = None
    for key in keys:
        root = insert(root, key)
    return root


if __name__ == '__main__':
    keys = [15, 10, 20, 8, 12, 16, 25]
    root = constructBST(keys)
    inorder(root)