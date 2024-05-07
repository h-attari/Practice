# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        num = 0
        while head is not None:
            num = (num * 10) + head.val
            head = head.next
        
        num *= 2
        num_lst = []
        while num > 0:
            num_lst.append(num % 10)
            num = num // 10
        if num_lst == []:
            return ListNode()
        
        head = ListNode(num_lst[-1])
        temp = head
        for num in num_lst[-2::-1]:
            temp.next = ListNode(num)
            temp = temp.next
        
        return head
        