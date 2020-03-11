#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        arr = []
        while arr or root:
            while root:
               arr.append(root)
               root = root.left
            root = arr.pop()
            res.append(root.val)

            root = root.right
        return res
head = TreeNode(1)
right = TreeNode(2)
left = TreeNode(3)
head.right = right
right.left = left
s = Solution()
s.inorderTraversal(head)
# @lc code=end

