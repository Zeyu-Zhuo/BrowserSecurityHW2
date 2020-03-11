#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        helpDict = {} 
        for i in nums:
            if i in helpDict:
                helpDict[i]+=1
            else:
                helpDict[i] = 1
        for key in helpDict:
            
        
# @lc code=end

