class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self, nums: list):
        if not nums:
            return 
        self.head = ListNode(nums[0])
        cur = self.head
        for num in nums[1:]:
            cur.next = ListNode(num)
            cur = cur.next

    def length(self) -> int:
        count, cur = 0, self.head
        while cur:
            count += 1
            cur = cur.next
        return count
    
    def find(self, val: int) -> ListNode:
        cur = self.head
        while cur:
            if cur.val == val:
                return cur
            cur = cur.next
        return None
    
    def getVal(self, index: int) -> int:
        cur = self.head
        count = 0
        while cur and count < index:
            cur = cur.next
            count += 1
        if not cur or index < 0:
            return "Error"
        return cur.val
    
    def insertFront(self, val: int):
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def insertRear(self, val: int):
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)

    def insertInside(self, index: int, val: int):
        prev, cur = None, self.head
        count = 0
        while cur and count < index:
            prev, cur = cur, cur.next
            count += 1
        if not cur or index == 0:
            return "Error"
        node = ListNode(val)
        prev.next = node
        node.next = cur

    def update(self, index: int, val: int):
        cur = self.head
        count = 0
        while cur and count < index:
            cur = cur.next
            count += 1
        if not cur:
            return "Error"
        cur.val = val

    def deleteFront(self):
        if self.head:
            self.head = self.head.next

    def deleteRear(self):
        if not self.head:
            return "Error"
        if not self.head.next:
            self.head = None
            return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None

    def deleteInside(self, index: int):
        prev, cur = None, self.head
        count = 0
        while cur and count < index:
            prev, cur = cur, cur.next
            count += 1
        if not cur or index == 0:
            return "Error"
        prev.next = cur.next
