# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root):
    if not root: return []
    return dfs(root.left) + [root.val] + dfs(root.right)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return dfs(root)