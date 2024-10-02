class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create(self, nums: list):
        if not nums:
            return
        self.head = ListNode(nums[0])
        cur = self.head
        for num in nums[1:]:
            node = ListNode(num)
            cur.next = node
            node.prev = cur
            cur = node
        self.tail = cur

    def insertFront(self, val: int):
        node = ListNode(val)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insertRear(self, val: int):
        node = ListNode(val)
        if not self.tail:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def deleteFront(self) -> bool:
        if not self.head:
            return False
        if not self.head.next:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return True

    def deleteRear(self) -> bool:
        if not self.tail:
            return False
        if not self.tail.prev:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return True

    def displayForward(self):
        if not self.head:
            print("The list is empty.")
            return
        cur = self.head
        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        print()

    def displayBackward(self):
        if not self.tail:
            print("The list is empty.")
            return
        cur = self.tail
        while cur:
            print(cur.val, end=" ")
            cur = cur.prev
        print()
