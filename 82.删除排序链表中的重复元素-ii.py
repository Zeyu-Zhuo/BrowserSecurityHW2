#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
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
        prehead = ListNode(-1)
        prehead.next = head
        before = prehead
        curr = head
        after = curr.next
        while after:
            if curr.val == after.val:
                value = curr.val
                thenext = after.next
                while thenext:
                    if thenext.val == value:
                        thenext = thenext.next
                    else:
                        break
                if thenext:
                    before.next = thenext
                else:
                    before.next = None
                    break
                
                curr = thenext
                after = thenext.next
            else:
                curr = after
                before = before.next
                after = after.next

        return prehead.next
            
# @lc code=end

