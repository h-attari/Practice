class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or self.head is None:
            return -1
        head = self.head
        for _ in range(index):
            head = head.next
        return head.val

    def addAtHead(self, val: int) -> None:
        self.head = ListNode(val, self.head)
        self.size += 1
        return

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = ListNode(val)
        else:
            head = self.head
            while head.next is not None:
                head = head.next
            head.next = ListNode(val)
        self.size += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            head = self.head
            for _ in range(index-1):
                head = head.next
            prev_node = head
            next_node = head.next
            prev_node.next = ListNode(val, next_node)
            self.size += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            if index == 0:
                self.head = self.head.next
            else:
                head = self.head
                for _ in range(index-1):
                    head = head.next
                head.next = head.next.next if head.next else None
            self.size -= 1
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)