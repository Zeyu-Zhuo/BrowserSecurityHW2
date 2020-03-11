#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        head = nums
        length = len(nums)
        tail = length - 1
        while head <= tail:
            middle = 
# @lc code=end

