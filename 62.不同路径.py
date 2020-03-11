#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 1
        dp = [[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j-1]
        
        return dp[n - 1][m - 1]

s = Solution()
res = s.uniquePaths(1,2)
print(res)
# @lc code=end

