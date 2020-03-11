#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        res = ListNode(-1)
        smaller = res
        bigger = None
        pre = ListNode(-1)
        pre.next = head
        curr = head
        while curr:
            if curr.val < x:
                smaller.next = curr
                smaller = smaller.next
                pre.next = curr.next
                curr = curr.next
                smaller.next = None
            elif not bigger:
                bigger = curr
                curr = curr.next
                pre = pre.next
            else:
                curr = curr.next
                pre = pre.next
        
        smaller.next = bigger
        return res.next

        
# @lc code=end

