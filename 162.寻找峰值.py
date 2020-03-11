#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return 0
        head = 0
        tail = size
        while head < tail:
            middle = head + (tail - head)//2
            if nums[middle]>tail:
                head = middle
            elif nums[middle] < head:
                tail = middle
# @lc code=end

