# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def reverse(root):
            if not root:
                return None
            
            temp = root.left
            root.left = root.right
            root.right = temp

            reverse(root.left)
            reverse(root.right)

        x = reverse(p)

        if x==q:
            return True
        else:
            return False
        