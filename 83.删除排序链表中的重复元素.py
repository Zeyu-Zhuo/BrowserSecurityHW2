#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        pre = head
        after = pre.next
        have = set()
        have.add(pre.val)
        while after:
            if after.val not in have:
                have.add(after.val)
                pre = pre.next
                after = after.next
            else:
                pre.next = after.next
                after = pre.next
        return head
# @lc code=end

