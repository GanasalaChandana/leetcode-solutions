class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        # 1 -> 2 -> 3 -> 4 -> 5
        # 0.   1.   2.   3.   4.
        if self.head is None or index >= self.length():
            return -1
        else:
            curr, ind = self.head, 0
            while ind < index:
                curr = curr.next
                ind += 1
            return curr.data 
        
    def addAtHead(self, val: int) -> None:
        new_node = Node(val,self.head)
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val, None)
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next
            new_node = Node(val, None)
            itr.next = new_node
            
    def addAtIndex(self, index: int, val: int) -> None:
        # 1 -> 2 -> 3 -> 4 -> 5
        # 0.   1.   2.   3.   4.
        ind, curr = 0, self.head
        if index > self.length():
            return
        else:
            if index == 0:
                new_node = Node(val, curr)
                self.head = new_node
            else:
                while ind < index-1:
                    curr = curr.next
                    ind += 1
                new_node = Node(val, curr.next)
                curr.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        # 1 -> 2 -> 3 -> 4 -> 5
        # 1.   2.   3.   4.   5
        if index >= self.length() or index < 0:
            return
        else:
            curr, ind = self.head, 0
            if index == 0:
                self.head = curr.next
            else:
                while ind < index - 1:
                    curr = curr.next
                    ind += 1
                curr.next = curr.next.next

    def length(self) -> int:
        if self.head is None:
            return 0
        else:
            curr, n = self.head, 0
            while curr.next is not None:
                n += 1
                curr = curr.next
            return n+1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)