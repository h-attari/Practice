# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        linked_list_len = 0
        temp = head
        while temp is not None:
            temp = temp.next
            linked_list_len += 1
        mid = linked_list_len // 2
        if mid == 0:
            return None
        index = 0
        result_linked_list = ListNode(head.val)
        temp = result_linked_list
        while head is not None:
            if index+1 == mid:
                head = head.next
            temp.next = head.next
            temp = temp.next
            head = head.next
            index += 1
        return result_linked_list