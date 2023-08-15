# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None
        list1, list2 = None, None
        temp1, temp2 = None, None
        
        while head != None:
            if head.val < x:
                if list1 is None:
                    list1 = ListNode(head.val)
                    temp1 = list1
                else:
                    temp1.next = ListNode(head.val)
                    temp1 = temp1.next
            else:
                if list2 is None:
                    list2 = ListNode(head.val)
                    temp2 = list2
                else:
                    temp2.next = ListNode(head.val)
                    temp2 = temp2.next
            head = head.next
        
        if temp1 is not None:
            temp1.next = list2
            return list1
        else:
            return list2