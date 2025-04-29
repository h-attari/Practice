# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None: return l2
        if l2 is None: return l1
        temp_sum = l1.val + l2.val
        l1 = l1.next
        l2 = l2.next
        carry = 0
        result = ListNode(temp_sum % 10)
        if temp_sum > 9:
            carry = 1
        temp_node = result
        while l1 is not None and l2 is not None:
            temp_sum = l1.val + l2.val + carry
            if temp_sum > 9:
                carry = 1
                temp_node.next = ListNode(temp_sum % 10)
            else:
                temp_node.next = ListNode(temp_sum)
                carry = 0
            l1 = l1.next
            l2 = l2.next
            temp_node = temp_node.next
        while l1 is not None:
            temp_sum = l1.val + carry
            if temp_sum > 9:
                carry = 1
                temp_node.next = ListNode(temp_sum % 10)
            else:
                temp_node.next = ListNode(temp_sum)
                carry = 0
            temp_node = temp_node.next
            l1 = l1.next
        while l2 is not None:
            temp_sum = l2.val + carry
            if temp_sum > 9:
                carry = 1
                temp_node.next = ListNode(temp_sum % 10)
            else:
                temp_node.next = ListNode(temp_sum)
                carry = 0
            temp_node = temp_node.next
            l2 = l2.next
        if carry == 1:
            temp_node.next = ListNode(1)
        return result
        