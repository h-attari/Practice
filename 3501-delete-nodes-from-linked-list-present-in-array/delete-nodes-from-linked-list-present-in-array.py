# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        while head.val in nums:
            head = head.next
        temp = head
        while temp.next is not None:
            if temp.next.val in nums:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
        