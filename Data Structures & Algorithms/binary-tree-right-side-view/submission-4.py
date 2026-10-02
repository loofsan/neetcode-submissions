# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        rightSideElements = []
        q = deque([root])
        while q:
            node1 = None
            for i in range(len(q)):
                node1 = q.popleft()
                if node1.left:
                    q.append(node1.left)
                if node1.right:
                    q.append(node1.right)
            
            rightSideElements.append(node1.val)
        
        return rightSideElements
