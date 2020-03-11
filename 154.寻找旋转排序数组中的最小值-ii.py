#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        head = 0
        tail = len(nums) - 1
        while head <= tail:
            middle = head + (tail - head)//2
            if nums[middle]>nums[tail]:
                head = middle + 1
            elif nums[middle] < nums[head]:
                tail = middle
            else:
                tail -= 1
        return nums[head]
# @lc code=end

