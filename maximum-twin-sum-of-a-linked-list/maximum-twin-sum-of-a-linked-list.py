# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow_head, fast_head = head, head.next
        while fast_head.next is not None:
            slow_head = slow_head.next
            fast_head = fast_head.next.next
        
        reverse_head = None
        slow_head = slow_head.next
        while slow_head is not None:
            reverse_head = ListNode(slow_head.val, reverse_head)
            slow_head = slow_head.next
        
        max_sum = 0
        while reverse_head is not None:
            max_sum = max(max_sum, (head.val + reverse_head.val))
            head = head.next
            reverse_head = reverse_head.next
        return max_sum