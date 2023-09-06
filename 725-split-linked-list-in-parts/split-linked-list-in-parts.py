# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = [None] * k
        if head is None:
            return result
        
        len_list = 0
        temp = head
        while temp != None:
            len_list += 1
            temp = temp.next

        parts = [len_list // k] * k
        remaining = len_list % k
        for index in range(remaining):
            parts[index] += 1

        for index in range(len(parts)):
            cur = head
            result[index] = cur
            for counter in range(parts[index]):
                head = head.next
                if counter == parts[index]-1:
                    cur.next = None
                cur = cur.next
        return result