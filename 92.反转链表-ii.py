#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        if not head:
           return None
        prehead = ListNode(-1)
        prehead.next = head
        curr = prehead
        for i in range(m - 1):
            curr = curr.next
        h1 = curr
        h2 = curr.next
        for i in range(n - m + 1):
            curr = curr.next
            t1 = curr.next
        pre = h1
        curr = h2
        while curr != t1:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr =temp
        h1.next = pre
        h2.next = t1
        return prehead.next

a = [3,5]
head = ListNode(a[0])
curr = head
for i in range(1,len(a)):
    new = ListNode(a[i])
    curr.next = new
    curr = curr.next
s = Solution()
s.reverseBetween(head,1,2)

        
# @lc code=end

