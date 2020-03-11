#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        prehead = None
        pre = prehead
        after = head
        while after:
            temp = after.next
            after.next = pre
            pre = after
            after= temp
        return pre
            
# @lc code=end

