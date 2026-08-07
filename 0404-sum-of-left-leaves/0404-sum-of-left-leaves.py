# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def findSum(root, isLeft):
    if not root: return 0
    if not root.left and not root.right:
        return root.val if isLeft else 0
    return findSum(root.left, True) + findSum(root.right, False)

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return findSum(root, False)