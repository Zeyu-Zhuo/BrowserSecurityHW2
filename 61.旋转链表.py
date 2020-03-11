#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if k == 0:
            return head
        tail = head
        num = 1
        while tail.next:
            tail = tail.next
            num += 1

        k = k % num
        if not k:
            return head
        tail = head
        for i in range(k):
            tail = tail.next
        cut = head
        while(tail.next):
            tail = tail.next
            cut = cut.next
        res = cut.next
        cut.next = None
        tail.next = head

        return res


        
# @lc code=end

