# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        q = deque([root])
        levelOrder = []
        while q:
            level = []
            for _ in range(len(q)):
                node1 = q.popleft()
                level.append(node1.val)

                if node1.left:
                    q.append(node1.left)
                if node1.right:
                    q.append(node1.right)

            levelOrder.append(level)

        return levelOrder