#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        def helper(curr):
            if len(curr) == length:
                res.append(curr[:])
                return
            for i in nums:
                if i not in curr:
                    helper(curr + [i])
        helper([])
        return res
# @lc code=end

