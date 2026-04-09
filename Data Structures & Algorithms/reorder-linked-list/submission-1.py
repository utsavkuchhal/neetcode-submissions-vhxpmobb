# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        print(head.val)
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def find_middle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.find_middle(head)
        list1 = head
        list2 = mid
        reverse_list = self.reverse(list2)
        print(list2.val)
        dummy = ListNode(-1)
        curr = dummy
        count = 0
        while list1 and reverse_list:
            if count % 2 == 0:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = reverse_list
                reverse_list = reverse_list.next
            count += 1
            curr = curr.next
        head = dummy.next        



        