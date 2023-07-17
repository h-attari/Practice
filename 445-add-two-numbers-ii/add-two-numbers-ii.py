# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def create_linked_list(self, result_num: str) -> Optional[ListNode]:
    result = ListNode(int(result_num[0]))
    temp = result
    for digit in result_num[1:]:
      temp.next = ListNode(int(digit))
      temp = temp.next
    return result

  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    num1, num2 = "", ""
    while l1 is not None or l2 is not None:
      if l1 is not None:
        num1 += str(l1.val)
        l1 = l1.next
      if l2 is not None:
        num2 += str(l2.val)
        l2 = l2.next
    result_num = int(num1) + int(num2)
    return self.create_linked_list(str(result_num))