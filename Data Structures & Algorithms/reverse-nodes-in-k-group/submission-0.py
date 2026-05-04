# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def total_nodes(self, head):
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        total_nodes = self.total_nodes(head)
        total_groups = total_nodes // k
        tail, final_head = None, None
        curr = head
        print(total_groups)
        while curr and total_groups > 0:
            count = 0
            prev = None
            group_head = curr
            total_groups -= 1
            while curr and count < k:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                count += 1

            if not final_head:
                final_head = prev
            
            if tail:
                tail.next = prev
            
            tail = group_head

        tail.next = curr
        return final_head




            
                