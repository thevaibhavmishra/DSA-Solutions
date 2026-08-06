# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def detect(root):
    if not root: return 0, True
    if not root.left and not root.right: return 1, True
    lh, lb = detect(root.left)
    rh, rb = detect(root.right)
    cb = abs(lh - rh) <= 1 and lb and rb
    return max(lh, rh) + 1, cb
    


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return detect(root)[1] == True