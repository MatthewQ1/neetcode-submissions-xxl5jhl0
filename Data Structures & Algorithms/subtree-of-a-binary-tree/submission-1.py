from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checksamehelper(root, subRoot):
            leftsame = False
            rightsame = False
            if root.val == subRoot.val:
                if root.left is not None:
                    if subRoot.left is not None:
                        leftsame = checksamehelper(root.left, subRoot.left)
                else:
                    leftsame = subRoot.left is None
                if root.right is not None:
                    if subRoot.right is not None:
                        rightsame = checksamehelper(root.right, subRoot.right)
                else:
                    rightsame = subRoot.right is None
            return leftsame and rightsame
                
        bfsqueue = deque()
        bfsqueue.append(root)

        while bfsqueue:
            node = bfsqueue.popleft()
            if node.val == subRoot.val:
                print("hi")
                if checksamehelper(node, subRoot):
                    return True
            if node.left is not None:
                bfsqueue.append(node.left)
            if node.right is not None:
                bfsqueue.append(node.right)
        return False
        
            
            
        