class Node:

    def __init__(self, val):
        self.val = val
        self.children = []


def lowestCommonAncestor(root, employees):
    stack = [root]
    parent = {root.val: None}

    # keep storing parent pointers until we find p and q
    while stack:

        node = stack.pop()
        for child in node.children:
            parent[child.val] = node
            stack.append(child)

    # now we have found both p and q
    # get all ancestors of p using parent and add to a set
    ancestors = set()
    p = employees[0]

    while p:
        ancestors.add(p.val)
        p = parent[p.val]

    for q in employees[1:]:
        # now we go through parents of q
        # and check if it is in ancestors
        while q and q.val not in ancestors:
            q = parent[q.val]

    return q.val


node1 = Node(3)
node2 = Node(5)
node3 = Node(1)
node1.children = [node2, node3]
node4 = Node(6)
node5 = Node(9)
node6 = Node(13)
node2.children = [node4, node5, node6]
node7 = Node(10)
node8 = Node(25)
node9 = Node(50)
node3.children = [node7, node8, node9]
node10 = Node(7)
node11 = Node(4)
node6.children = [node10, node11]
root = node1

# lowestCommonAncestor(root,[Node(6),Node(9),Node(7)])
# lowestCommonAncestor(root,[Node(4),Node(7)])
print(lowestCommonAncestor(root, [Node(6), Node(7), Node(50)]))
