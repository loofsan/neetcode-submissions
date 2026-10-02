# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if not self.isSametree(root, subRoot):
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        
        return True
    
    def isSametree(self, node1, node2):
        if not node1 and not node2:
            return True
        
        if not node1 or not node2 or node1.val != node2.val:
            return False
        
        return (self.isSametree(node1.left, node2.left) and self.isSametree(node1.right, node2.right))
