#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#

# @lc code=start
from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        length = len(nums)
        if length<2:
            return 0
        
        maxval = max(nums)
        minval = min(nums)
        if minval == maxval:
            return 0
        gap = (maxval - minval)//(length - 1)
        if gap == 0:
            gap = 1
        bucketnum  = (maxval - minval)//gap + 1
        bucket = [[float('inf'),float('-inf')] for _ in range(bucketnum)]
        for num in nums:
            bucket_index = (num - minval) // gap 
            bucket[bucket_index][0] = min(bucket[bucket_index][0],num)
            bucket[bucket_index][1] = max(bucket[bucket_index][1],num)
        
        res = float('-inf')
        lastmaxval = bucket[0][1]
        for i in range(1,bucketnum):
            if bucket[i][0]!=float('inf'):
                res = max(res,bucket[i][0] - lastmaxval)
                lastmaxval = bucket[i][1]
        return res
# @lc code=end

