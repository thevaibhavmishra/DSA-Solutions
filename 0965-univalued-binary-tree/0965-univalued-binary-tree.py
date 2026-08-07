# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dfs(root, k):
    if not root: return True
    if root.val != k: return False
    return dfs(root.left, k) and dfs(root.right, k)

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return dfs(root, root.val)