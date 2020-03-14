#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        if length<3:
            return max(nums)
        dp = [0] * length
        dp[1] = nums[1]
        dp[0] = 0
        for i in range(2,length):
            dp[i] = max(nums[i]+dp[i - 2],dp[i-1])
        maxval = dp[-1]
        dp = [0] * length
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2,length - 1):
            dp[i] = max(nums[i]+dp[i - 2],dp[i-1])
        maxval = max(maxval,dp[-2])
        return maxval

s = Solution()
s.rob([2,7,9,3,1])

# @lc code=end

