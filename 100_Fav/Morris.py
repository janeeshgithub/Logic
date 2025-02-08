class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getInorder(self, root):
        """
        Morris Inorder Traversal (Space-Optimized)

        - Performs inorder traversal without recursion or stack.
        - Uses the concept of threading in binary trees.
        - Time Complexity: O(n), Space Complexity: O(1).

        Args:
        root (TreeNode): Root of the binary tree.

        Returns:
        List[int]: Inorder traversal of the binary tree.
        """
        inorder = []
        cur = root

        while cur:
            # Case 1: If left child is None, visit current node and move right.
            if not cur.left:
                inorder.append(cur.val)
                cur = cur.right
            else:
                # Find the rightmost node (predecessor) in the left subtree
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right

                # If the rightmost node's right is None, create a temporary link
                if prev.right is None:
                    prev.right = cur  # Establish a temporary thread
                    cur = cur.left  # Move left
                else:
                    # If the thread already exists, remove it and visit the current node
                    prev.right = None  # Remove the thread
                    inorder.append(cur.val)  # Visit the node
                    cur = cur.right  # Move right

        return inorder


# Example Usage
if __name__ == "__main__":
    # Constructing the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)

    sol = Solution()
    inorder = sol.getInorder(root)

    # Printing the inorder traversal
    print("Morris Inorder Traversal:", inorder)
