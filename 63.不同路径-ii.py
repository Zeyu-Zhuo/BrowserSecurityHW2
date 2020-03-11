#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m < 1:
            return 0
        n = len(obstacleGrid[0])
        if n < 1:
            return 0
        if 1 == obstacleGrid[0][0]:
            return 0
        dp = [[0]*n for _ in range(m)]  # 外层不能使用*，否则会浅拷贝内层，赋值会带来问题，初始化为０，可以避免额外的赋值
        for i in range(0, m):
            for j in range(0, n):
                if 0 == i and 0 == j:
                    dp[i][j] = 1
                elif 0 == i and 0 != j:
                    if 0 == obstacleGrid[i][j]:
                        dp[i][j] = dp[i][j - 1]
                elif 0 != i and 0 == j:
                    if 0 == obstacleGrid[i][j]:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if 0 == obstacleGrid[i][j]:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
# @lc code=end

