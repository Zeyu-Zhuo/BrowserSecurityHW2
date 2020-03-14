#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(arr,left,right):
            pivot = arr[right]
            start = left
            for i in range(left,right+1):
                if arr[i] < pivot:
                    arr[i],arr[start] = arr[start],arr[i]
                    start += 1
            arr[start],arr[right] = arr[right],arr[start]
            return start
        def quicksort(arr,left,right):
            if left < right:
                index = partition(arr,left,right)
                quicksort(arr,left,index-1)
                quicksort(arr,index + 1,right)
        quicksort(nums,0,len(nums) - 1)
        return nums
# @lc code=end

