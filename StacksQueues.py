from collections import deque
from typing import List

class TreeNode:
     """A Binary Tree with Left/Right Nodes"""
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class StacksQueues:
    def __init__(self):
        pass

    def isValidPair(self,s1,s2):
        """Helper Function for isvalid, Checks if s1, s2 are a valid bracket pair"""
        if (s1 == '(' and s2 == ')'):
            return True
        if (s1 == '[' and s2 == ']'):
            return True
        if (s1 == '{' and s2 == '}'):
            return True
        return False

    def isValid(self, s: str) -> bool:
        """Checks if s contains valid ({[]}) pair in correct order"""
        st = []

        for char in s:
            if (len(st) != 0):
                e = st[-1]
                if (self.isValidPair(e,char)):
                    st.pop()
                    continue
            st.append(char)
        return (len(st)==0)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """Runs a BFS Traversal, Returning a 2D Array representing notes at each level of the tree.
           One dimension representing each level, and it's array representing nodes at that level.
           q is a queue of child nodes, starting from the root, down to the end.
        """

        result = []
        if(root is None):
            return result

        q = deque([root])
        while(q):
            n = len(q)
            level = []
            for i in range(0,n):
                f = q.popleft()
                level.append(f.val)

                if (f.left is not None):
                    q.append(f.left)
                if (f.right is not None):
                    q.append(f.right)

            if(len(level) > 0):
                result.append(level[:])
                level.clear()
        return result

    def TestRecursive(self):
        tree = TreeNode(1)
        tree.left = TreeNode(2)
        tree.right = TreeNode(3)
        tree.left.left = TreeNode(4)
        tree.left.right = TreeNode(5)
        print("Pre Order Traversal is", self.RecursiveTraversal(tree, "PRE"))
        print("Post Order Traversal is", self.RecursiveTraversal(tree, "POST"))
        print("In Order Traversal is",self.RecursiveTraversal(tree,"IN"))

    def RecursiveTraversal(self, root: TreeNode, strategy: str) -> List[int]:
        """Returns a list with the order traversal of elements in the tree
           Uses a strategy type pattern with parameters strategy = {PRE,POST,IN}
           For respective order traversals
        """

        result = []
        if (root):
            if strategy == 'POST':
                if (root.left is not None):
                    result = result + self.RecursiveTraversal(root.left,strategy)
                if (root.right is not None):
                    result = result + self.RecursiveTraversal(root.right,strategy)
                result.append(root.val)
            elif strategy == 'PRE':
                result.append(root.val)
                if (root.left is not None):
                    result = result + self.RecursiveTraversal(root.left,strategy)
                if (root.right is not None):
                    result = result + self.RecursiveTraversal(root.right,strategy)
            elif strategy == 'IN':
                if (root.left is not None):
                    result = result + self.RecursiveTraversal(root.left,strategy)
                result.append(root.val)
                if (root.right is not None):
                    result = result + self.RecursiveTraversal(root.right,strategy)
        return result