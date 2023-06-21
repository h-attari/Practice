# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_intersection_value(self, node_1: ListNode, node_2: ListNode) -> Optional[ListNode]:
        while node_1 is not None and node_2 is not None:
            if node_1 == node_2:
                return node_1
            else:
                node_1 = node_1.next
                node_2 = node_2.next
        return None
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A_len, B_len = 0, 0
        A_temp, B_temp = headA, headB
        while A_temp is not None or B_temp is not None:
            if A_temp is not None:
                A_len += 1
                A_temp = A_temp.next
            if B_temp is not None:
                B_len += 1
                B_temp = B_temp.next
        result = None
        len_diff = abs(A_len - B_len)
        if A_len > B_len:
            for _ in range(len_diff):
                headA = headA.next
            result = self.get_intersection_value(headA, headB)
        elif B_len > A_len:
            for _ in range(len_diff):
                headB = headB.next
            result = self.get_intersection_value(headB, headA)
        else:
            result = self.get_intersection_value(headA, headB)
        return result