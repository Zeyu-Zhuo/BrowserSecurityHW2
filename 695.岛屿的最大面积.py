#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        column = len(grid[0])
        if not row or not column:
            return 0
        visited = [[False] * column for _ in range(row)]
        positions = [[-1,0],[1,0],[0,1],[0,-1]]
        def getsize(x:int,y:int):
            visited[x][y] = True
            arr = [[x,y]]
            size = 1
            while arr:
                x,y = arr.pop()
                print(x,y)
                for position in positions:
                    x1 = x + position[0]
                    y1 = y + position[1]
                    if 0<= x1 < row and 0<=y1 < column and not visited[x1][y1] and grid[x1][y1]:
                        visited[x1][y1] = True
                        arr.append([x1,y1])
                        size += 1
            return size
        res = 0
        for i in range(row):
            for j in range(column):
                if not visited[i][j] and grid[i][j] == 1:
                    res = max(res,getsize(i,j))
                    print('===============================')
        
        return res
s = Solution()
res = s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]])
print(res)
# @lc code=end

