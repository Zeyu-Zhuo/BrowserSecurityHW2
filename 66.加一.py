#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits))[::-1]:
            digits[i] += 1
            digits[i] = digits[i] % 10
            if digits[i]:
                return digits
        
        if not digits[0]:
            digits.insert(0,1)
        return digits 
# @lc code=end

