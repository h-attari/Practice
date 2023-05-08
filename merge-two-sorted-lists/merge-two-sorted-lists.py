# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None or list2 is None:
            return list1 if list2 is None else list2
        
        result = ListNode()
        if list2.val < list1.val:
            result.val = list2.val
            list2 = list2.next
        else:
            result.val = list1.val
            list1 = list1.next
        temp = result

        while list1 is not None and list2 is not None:
            temp.next = ListNode()
            temp = temp.next
            if list2.val < list1.val:
                temp.val = list2.val
                list2 = list2.next
            else:
                temp.val = list1.val
                list1 = list1.next
        
        temp.next = list1 if list1 is not None else list2
        return result
        