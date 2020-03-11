#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        arr1 = [root]
        while arr1:
            res1 = []
            arr2 = []
            while arr1:
                node = arr1.pop(0) 
                res1.append(node.val)
                if node.left:
                    arr2.append(node.left)
                if node.right:
                    arr2.append(node.right)
            arr1 = arr2
            arr2 = []
            res.insert(0,res1)
        return res

# @lc code=end

