# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        preorder = deque(preorder)
        def fun(preorder, inorder):
            if not inorder: return None
            ind = inorder.index(preorder.popleft())
            node = TreeNode(inorder[ind])
            node.left = fun(preorder, inorder[:ind])
            node.right = fun(preorder, inorder[ind+1:])
            return node
        
        return fun(preorder, inorder)