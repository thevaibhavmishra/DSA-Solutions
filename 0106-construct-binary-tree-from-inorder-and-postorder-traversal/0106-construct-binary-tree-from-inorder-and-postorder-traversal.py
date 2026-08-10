# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder = deque(postorder)
        def fun(preorder, inorder):
            if not inorder: return None
            ind = inorder.index(postorder.pop())
            node = TreeNode(inorder[ind])
            node.right = fun(postorder, inorder[ind+1:])
            node.left = fun(postorder, inorder[:ind])
            return node
        
        return fun(postorder, inorder)