#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        n = 1 << size
        res = []
        for i in range(n):
            cur = []
            for j in range(size):
                if i >> j & 1:
                    cur.append(nums[j])
            res.append(cur)
        return res


s = Solution()
s.subsets([1,2,3])
# @lc code=end

