# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp.next != None:
            x, y = temp.val, temp.next.val
            gcd = math.gcd(x, y)
            new_node = ListNode(gcd, temp.next)
            temp.next = new_node
            temp = temp.next.next
        return head