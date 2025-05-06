# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None: return None
        list_len = 0
        tail = None
        temp = head
        while temp is not None:
            list_len += 1
            tail = temp
            temp = temp.next
        k = k % list_len
        if k == 0: return head
        k = list_len - k
        while k > 0:
            temp = head
            head = head.next
            tail.next = temp
            temp.next = None
            tail = tail.next
            k -= 1
        return head
