# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        
        def helper(root):
            if not root.right: return root.left
            if not root.left: return root.right
            lastRight = findLastRight(root.left)
            lastRight.right = root.right
            return root.left
        

        def findLastRight(root):
            while root.right:
                root = root.right
            return root
        temp = root
        while temp:
            if temp.val > key:
                if temp.left and temp.left.val == key:
                    temp.left = helper(temp.left)
                    return root
                else:
                    temp = temp.left
            elif temp.val < key:
                if temp.right and temp.right.val == key:
                    temp.right = helper(temp.right)
                    return root
                else:
                    temp = temp.right
            else:
                return helper(temp)
        return root