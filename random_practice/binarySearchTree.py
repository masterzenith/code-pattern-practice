# Binary search tree
class binarySearchTree:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        # check if there is no root
        if (self.val == None):
            self.val = val
        # check where to insert
        else:
            # check for duplicate then stop and return
            if val == self.val:
                return 'no duplicates allowed in BST'
            # check if value to be inserted < currentNode's value
            if (val < self.val):
                # check if there is a left node to currentNode if true then recurse
                if (self.left):
                    self.left.insert(val)
                # insert where left of currentNode when currentNode.left=None
                else:
                    self.left = binarySearchTree(val)
            # same steps as above here the condition we check is value to be inserted > currentNode's value
            else:
                if (self.right):
                    self.right.insert(val)
                else:
                    self.right = binarySearchTree(val)

    def breadthFirstSearch(self):
        currentNode = self
        bfs_list = []
        queue = []
        queue.insert(0, currentNode)
        while (len(queue) > 0):
            currentNode = queue.pop()
            bfs_list.append(currentNode.val)
            if (currentNode.left):
                queue.insert(0, currentNode.left)
            if (currentNode.right):
                queue.insert(0, currentNode.right)
        return bfs_list

    # In-order means first left child, then parent, at last right child
    def depth_first_search_inorder(self):
        return self.traverseInOrder([])

    def traverseInOrder(self, lst):
        if (self.left):
            self.left.traverseInOrder(lst)
        lst.append(self.val)
        if (self.right):
            self.right.traverseInOrder(lst)
        return lst

    # Pre-order means first parent, then left child, at last right child
    def depth_first_search_preorder(self):
        return self.traversePreOrder([])

    def traversePreOrder(self, lst):
        lst.append(self.val)
        if (self.left):
            self.left.traversePreOrder(lst)
        if (self.right):
            self.right.traversePreOrder(lst)
        return lst

    # Post order means first left child, then right child, at last parent
    def depth_first_search_postorder(self):
        return self.traversePostOrder([])

    def traversePostOrder(self, lst):
        if (self.left):
            self.left.traversePostOrder(lst)
        if (self.right):
            self.right.traversePostOrder(lst)
        lst.append(self.val)
        return lst

    def find_node_and_it_parent(self, val, parent=None):
        # returning the node and its parent so we can delete the node and reconstruct the tree from its parent
        if val == self.val:
            return self, parent
        if (val < self.val):
            if (self.left):
                return self.left.find_node_and_it_parent(val, self)
            else:
                return 'Not found'
        else:
            if (self.right):
                return self.right.find_node_and_it_parent(val, self)
            else:
                return 'Not found'
    # deleting a node means we have to rearrange some part of the tree
    def delete(self, val):
        # check if the value we want to delete is in the tree
        if (self.find_node_and_it_parent(val) == 'Not Found'):
            return 'Node is not in Tree'
        # we get the node we want to delete and its parent-node from find_node_and_its_parent method
        deleteing_node, parent_node = self.find_node_and_it_parent(val)
        #check how many children nodes does the node we are going to delte have by traversePreOrder from the deleteing_node
        nodes_effected = deleteing_node.traversePreOrder([])
        if (len(nodes_effected) == 1):
            if (parent_node.left.val == deleteing_node.val) :
                parent_node.left = None
            else:
                parent_node.right = None
            return 'successfully deleted'
        else:
            # if the node we want to delete doesn't have any parent mean
            if (parent_node == None):
                nodes_effected.remove(deleteing_node.val)
                self.left = None
                self.right = None
                self.val = None
                # construction of new tree
                for node in nodes_effected:
                    self.insert(node)
                return 'Successfully deleted'
            nodes_effected = parent_node.traversePreOrder([])
            if (parent_node.left == deleteing_node):
                parent_node.left = None
            else:
                parent_node.right = None
            nodes_effected.remove(deleteing_node.val)
            nodes_effected.remove(parent_node.val)
            for node in nodes_effected:
                self.insert(node)
        return 'successfully deleted'

bst = binarySearchTree()
bst.insert(7)
bst.insert(4)
bst.insert(9)
bst.insert(0)
bst.insert(5)
bst.insert(8)
bst.insert(13)
print('In order: ', bst.depth_first_search_inorder())
print('Pre order: ', bst.depth_first_search_preorder())
print('Post order: ', bst.depth_first_search_postorder())

print(bst.delete(5))
print(bst.delete(9))
print(bst.delete(7))

# after deleting
print('In order: ', bst.depth_first_search_inorder())