#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        res = [0,1,3,2]
        for i in range(2,n):
            res = res + [x + pow(2,i) for x in res[::-1]]
        return res
# @lc code=end

