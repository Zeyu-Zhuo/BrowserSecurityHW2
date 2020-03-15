#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        def helper(curr,choose):
            if len(curr) == length:
                res.append(curr[:])
            this = []
            for i in range(0,length):
                if nums[i] not in this and i not in choose:
                    this.append(nums[i])
                    helper(curr+[nums[i]],choose + [i])
        helper([],[])
        return res

# @lc code=end

