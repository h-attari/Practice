# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = head
        for _ in range(k-1):
            fast = fast.next
        temp = fast.val
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        temp, slow.val = slow.val, temp
        fast = head
        for _ in range(k-1):
            fast = fast.next
        fast.val = temp
        return head