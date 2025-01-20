import logging
from threading import Lock

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None
        self.lock = Lock()
        logging.basicConfig(level=logging.INFO)

    def insert(self, key):
        if not isinstance(key, (int, float)):
            raise ValueError("Only numerical values are allowed.")
        with self.lock:
            if self.root is None:
                self.root = TreeNode(key)
                logging.info(f"Inserted root node: {key}")
            else:
                self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
                logging.info(f"Inserted {key} to the left of {node.val}")
            else:
                self._insert(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = TreeNode(key)
                logging.info(f"Inserted {key} to the right of {node.val}")
            else:
                self._insert(node.right, key)
        else:
            logging.warning(f"Duplicate key {key} ignored.")

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=' ')
            self.inorder(node.right)

# Example usage with logging
bt = BinaryTree()
bt.insert(8)
bt.insert(3)
bt.insert(10)
bt.insert(3)  # Duplicate, should be ignored
bt.insert(6)

print("Inorder traversal of the binary tree:")
bt.inorder(bt.root)
