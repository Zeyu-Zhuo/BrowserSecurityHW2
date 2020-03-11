#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 0
        length = len(nums)
        end = length - 1
        while start<end:
            mid = (start + end + 1) >> 1
            ctn = 0
            for i in nums:
                if i < mid:
                    ctn += 1
            if ctn >= mid:
                end = mid - 1
            else:
                start = mid
        return start
s = Solution()
s.findDuplicate([1,3,4,2,2])        
# @lc code=end

