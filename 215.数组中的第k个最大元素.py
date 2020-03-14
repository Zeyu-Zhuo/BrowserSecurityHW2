#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(arr: List[int],left: int,right: int,pivot: int):
            value = arr[pivot]
            start = left
            for i in range(left,right):
                if arr[i]<value:
                    arr[i],arr[start] = arr[start],arr[i]
                    start += 1
            arr[pivot],arr[start] = arr[start],arr[pivot]    
            return start
        def select(left,right,k_smallest):
            if left == right:
                return nums[left]
            
            
        

# @lc code=end

