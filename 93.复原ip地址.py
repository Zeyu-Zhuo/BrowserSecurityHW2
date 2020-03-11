#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []
        res = []
        def helper(remainStr: str,curr: str,time: int):
            if not remainStr and time == 4:
                res.append(curr[:-1])
                return
            if time >= 4 or not remainStr:
                return
            for i in range(1,4):
                if i<=len(remainStr):
                    if i>=2 and remainStr[0] == '0':
                        continue
                    
                    if -1<int(remainStr[:i])<256:
                        helper(remainStr[i:],curr + remainStr[:i] + '.',time + 1)
                    
                    


        helper(s,"",0)
        return res
s = Solution()
a = s.restoreIpAddresses("010010")
print(a)
# @lc code=end

