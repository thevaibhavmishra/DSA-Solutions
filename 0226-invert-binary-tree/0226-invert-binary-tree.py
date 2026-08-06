# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invert(root):
    if not root: return root
    temp = root.left
    root.left = invert(root.right)
    root.right = invert(temp)
    return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return invert(root)