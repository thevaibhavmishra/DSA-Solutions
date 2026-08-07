# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
boolValues = (False, True, lambda a, b: a or b, lambda a, b: a and b)

def dfs(root):
    if not root.left and not root.right: return boolValues[root.val]
    return boolValues[root.val](dfs(root.left), dfs(root.right))

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return dfs(root)