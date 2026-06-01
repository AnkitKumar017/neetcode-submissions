# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None
        res = 0
        q = deque([root])
        ans = root.val

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.val>=ans:
                    res+=1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res



        