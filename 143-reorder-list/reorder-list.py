# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_linked_list(self, head):
        prev, cur = None, head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        head2 = self.reverse_linked_list(slow.next)
        slow.next = None
        head1 = head
        while head1 is not None and head2 is not None:
            temp1, temp2 = head1.next, head2.next
            head1.next = head2
            head2.next = temp1
            head1, head2 = temp1, temp2
        