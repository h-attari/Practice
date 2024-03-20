# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node_before_a, node_after_b = None, None
        
        temp = list1
        count = 0
        while count <= b:
            if count == a-1:
                node_before_a = temp
            temp = temp.next
            count += 1
        node_after_b = temp

        temp = list2
        while temp.next is not None:
            temp = temp.next
        
        node_before_a.next = list2
        temp.next = node_after_b

        return list1
