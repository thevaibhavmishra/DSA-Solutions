# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def findSum(root):
    if not root: return 0
    s = 0
    if root.left and not root.left.left and not root.left.right:
        s += root.left .val
    return findSum(root.left) + findSum(root.right) + s

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return findSum(root)