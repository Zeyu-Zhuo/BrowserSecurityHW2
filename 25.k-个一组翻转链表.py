#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode: 
        def helper(pre,num):
            k = 0
            head = pre
            res = head.next
            after = pre.next
            while pre and k<=num:
                k += 1
                temp = after.next
                after.next = pre
                pre = after
                after = temp
                
            head.next = after
            return res
        
        helphead = ListNode(0)
        helphead.next = head
        helper(helphead,k)
        return helper(helphead,k)
        
s = Solution()
s.reverseKGroup([1,2,3,4,5],2)
        
# @lc code=end

