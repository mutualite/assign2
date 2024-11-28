from node import Node

def comp_1(node_1, node_2):
    pass

class TreeNode:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None
        self.height = 1  # New nodes are initially added at height 1

class AVLTree:
    def __init__(self, compare_function=None):
        self.root = None
        self.size = 0
        self.comparator = compare_function
        self.L=[]
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left

        return current
    def findnear(self, root, key):
        #print('hi')
        self.path=[]
        if root.key < key and root.right is not None:
            self.path.append(root)
            return self.findnear1(root.right, key)
        if root.key > key and root.left is not None:
            self.path.append(root)
            return self.findnear1(root.left, key)
        if root.key == key:
            self.path.append(root)
        return self.path
        
    def findnear1(self, root, key):
        #print('hi')
        if root.key < key and root.right is not None:
            self.path.append(root)
            return self.findnear1(root.right, key)
        if root.key > key and root.left is not None:
            self.path.append(root)
            return self.findnear1(root.left, key)
        else:
            self.path.append(root)
            return self.path
    def search(self, root, key):
        if not root or root.key == key:
            return root
        if root.key < key:
            return self.search(root.right, key)
        return self.search(root.left, key)
    def delete_node(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete_node(root.left, key)

        elif key > root.key:
            root.right = self.delete_node(root.right, key)

        else:
            if root.left is None or root.right is None:
                temp = root.left if root.left else root.right

                if temp is None:
                    root = None
                else: 
                    root = temp
            else:
                temp = self.min_value_node(root.right)
                root.key = temp.key
                root.right = self.delete_node(root.right, temp.key)

        if root is None:
            return root
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        balance = self.get_balance(root)

        # Balance the tree
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


    def insert(self, root, key):
        # Perform normal BST insertion
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        elif key==root.key:
            return None

        # Update height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get balance factor
        balance = self.get_balance(root)

        # Balance the tree
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)  # Left Left Case

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)  # Right Right Case

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)  # Left Right Case
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            #print('i was here')# Right Left Case
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def in_order(self, root):
        self.L = []  # Initialize L for each traversal call
        self._in_order_helper(root)
        return self.L

    def _in_order_helper(self, root):
        if not root:
            return
        self._in_order_helper(root.left)
        self.L.append(root.key)
        self._in_order_helper(root.right)
