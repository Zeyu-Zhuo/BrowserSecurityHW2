#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        arr = []
        maxv = float('-inf')
        while arr or root:
            while root:
                arr.append(root)
                root = root.left
            root = arr.pop()
            if root.val <= maxv:
                return False
            maxv = root.val
            root = root.right
        return True
# @lc code=end

