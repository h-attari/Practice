# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = None
        while head is not None:
            if head.val != val:
                if result is None:
                    result = ListNode(head.val)
                    temp = result
                else:
                    temp.next = ListNode()
                    temp = temp.next
                    temp.val = head.val
            head = head.next 
        return result
        