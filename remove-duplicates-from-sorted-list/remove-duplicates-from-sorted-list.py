# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        duplicates = [head.val]
        temp = result = ListNode(head.val)
        head = head.next
        while head is not None:
            if head.val not in duplicates:
                temp.next = ListNode(head.val)
                duplicates.append(head.val)
                temp = temp.next
            head = head.next
        return result
