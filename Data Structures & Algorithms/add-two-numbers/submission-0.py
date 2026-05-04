# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r_l1 = l1
        r_l2 = l2
        dummy = ListNode(-1)
        result = dummy
        carry = 0
        while r_l1 and r_l2:
            val = r_l1.val + r_l2.val + carry
            digit, carry = val % 10, val // 10
            dummy.next = ListNode(digit)
            r_l1 = r_l1.next
            r_l2 = r_l2.next
            dummy = dummy.next

        while r_l1:
            val = r_l1.val + carry
            digit, carry = val % 10, val // 10
            dummy.next = ListNode(digit)
            r_l1 = r_l1.next
            dummy = dummy.next

        while r_l2:
            val = r_l2.val + carry
            digit, carry = val % 10, val // 10
            dummy.next = ListNode(digit)
            r_l2 = r_l2.next
            dummy = dummy.next

        if carry:
            dummy.next = ListNode(carry)
            dummy = dummy.next

        return result.next
