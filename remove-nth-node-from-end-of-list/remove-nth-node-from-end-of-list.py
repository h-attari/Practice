# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = 0
        temp = head
        while temp is not None:
            list_len += 1
            temp = temp.next
        if list_len == 1:
            return None
        remove_index = list_len - n
        if remove_index == 0:
            head = head.next
        else:
            temp = head
            for _ in range(remove_index-1):
                temp = temp.next
            temp.next = temp.next.next
        return head