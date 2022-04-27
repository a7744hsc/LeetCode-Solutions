#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k<=0:
            return head

        slow,fast = head,head
        length = 1
        for i in range(k):
            if not fast.next:
                fast = head
                break
            else:
                length +=1
                fast = fast.next
        if k>=length:
            new_k = k%length
            for i in range(new_k):
                fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next if slow.next else head
        slow.next = None
        if new_head != head:
            fast.next = head
        return new_head
        
# @lc code=end

