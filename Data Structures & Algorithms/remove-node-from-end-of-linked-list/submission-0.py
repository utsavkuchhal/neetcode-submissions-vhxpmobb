# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for i in range(n):
            fast = fast.next
        dummy = ListNode(-1)
        dummy.next = head
        prev, slow = dummy, head
        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next
        prev.next = slow.next
        return dummy.next