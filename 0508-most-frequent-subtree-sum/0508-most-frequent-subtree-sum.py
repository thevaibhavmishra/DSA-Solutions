# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.sums = defaultdict(int)
        def dfs(root):
            if not root: return 0
            s = dfs(root.left) + root.val + dfs(root.right)
            self.sums[s] +=1
            return s
        dfs(root)
        mx = max(self.sums.values())
        res = list(map(lambda x: x[0], filter(lambda x: x[1] == mx, self.sums.items())))
        return res

        