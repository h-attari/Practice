class MyLinkedListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        if index >= self.len:
            return -1
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.val

    def addAtHead(self, val: int) -> None:
        self.head = MyLinkedListNode(val, self.head)
        self.len += 1
        return

    def addAtTail(self, val: int) -> None:
        if self.len == 0:
            self.addAtHead(val)
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = MyLinkedListNode(val, None)
        self.len += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.len:
            self.addAtTail(val)
            return
        temp = self.head
        for _ in range(index-1):
            temp = temp.next
        temp.next = MyLinkedListNode(val, temp.next)
        self.len += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len:
            return
        if index == 0:
            self.head = self.head.next
            self.len -= 1
            return
        temp = self.head
        for _ in range(index-1):
            temp = temp.next
        temp.next = temp.next.next
        self.len -= 1
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)