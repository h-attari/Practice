# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        fast_head = head
        while fast_head is not None and fast_head.next is not None:
            head = head.next
            fast_head = fast_head.next.next
        return head