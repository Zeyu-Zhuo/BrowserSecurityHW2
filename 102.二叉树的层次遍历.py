#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        arr = [root]
        res1 = []
        arr2 = []
        while arr:
            res1 = []
            while arr:
                node = arr.pop(0)
                res1.append(node.val)
                if node.left:
                    arr2.append(node.left)
                if node.right:
                    arr2.append(node.right)
            arr = arr2
            arr2 = []
            
            res.append(res1)
        return res
# @lc code=end

