# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge_list(self, a: ListNode, b: ListNode):
        dummy = ListNode(-1)
        curr = dummy
        while a and b:
            if a.val <= b.val:
                curr.next = a
                a = a.next
            else:
                curr.next = b
                b = b.next
            curr = curr.next
        if a:
            curr.next = a
        if b:
            curr.next = b
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        prev = lists[0]
        for index in range(1, n):
            temp = self.merge_list(prev, lists[index])
            prev = temp
        return prev