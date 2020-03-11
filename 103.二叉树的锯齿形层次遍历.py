#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        arr1 = [root]
        arr2 = []
        res = []
        dirct = True
        while arr1:
            res1 = []
            if dirct:
                for i in arr1:
                    res1.append(i.val)
                    if i.left:
                        arr2.append(i.left)
                    if i.right:
                        arr2.append(i.right)

            else:
                for i in range(len(arr1))[::-1]:
                    res1.append(arr1[i].val)
                    if arr1[i].right:
                        arr2.insert(0,arr1[i].right)
                    if arr1[i].left:
                        arr2.insert(0,arr1[i].left)
            dirct = not dirct
            res.append(res1)
            arr1 = arr2
            arr2 = []
                    
        return res

# @lc code=end

