# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def helper(node):
            leftres = (True, 0)
            rightres = (True, 0)
            if node.left is None and node.right is None:
                return (True, 1)
            if node.left is not None:
                leftres = helper(node.left)
            if node.right is not None:
                rightres = helper(node.right)
            print(leftres, rightres)
            if (not leftres[0]) or (not rightres[0]) or abs(leftres[1] - rightres[1]) > 1:
                return (False, max(leftres[1], rightres[1]))
            return (True, max(leftres[1], rightres[1]) + 1)

        return helper(root)[0]
        