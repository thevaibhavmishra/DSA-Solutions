# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

def detect(root, d):
    if not root: return
    d[root.val] += 1
    detect(root.left, d)
    detect(root.right, d)

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int)
        detect(root, d)
        mx = max(d.values())
        res = list(map(lambda x: x[0], filter(lambda x: x[1] == mx, d.items())))
        return res
