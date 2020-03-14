#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if not nums:
            return 0
        if length<3:
            return max(nums)
        dp = [0]*length
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2,length):
            dp[i] = max(nums[i]+dp[i - 2],dp[i-1])
        return dp[-1]
s = Solution()
s.rob([1,2,3,1])
# @lc code=end

