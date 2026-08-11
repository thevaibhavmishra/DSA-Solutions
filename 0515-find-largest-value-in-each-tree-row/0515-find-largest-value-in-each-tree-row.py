# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        max_values = defaultdict(lambda: float('-inf'))
        def fun(root, level=0, max_values=max_values):
            if not root: return
            max_values[level] = root.val if root.val > max_values[level] else max_values[level]
            fun(root.left, level + 1, max_values)
            fun(root.right, level + 1, max_values)
        
        fun(root)
        return list(max_values.values())