# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        #we'll do a recursive call from the base of the right sub tree and check if that is balanced.
        #In this way we do not need to return to same node multiple times.

        #our function will return a list [True/False,height of the subtree]

        def dfs(root):

            if not root: return [True,0]

            left,right = dfs(root.left),dfs(root.right)

            balanced = (left[0] and right[0] and 
                        abs(left[1]-right[1])<=1)

            return [balanced, 1+max(left[1],right[1])]

        return dfs(root)[0]
        