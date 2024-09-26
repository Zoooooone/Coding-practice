import typing


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def create(nums: list) -> ListNode:
    if not nums:
        return None

    queue = []
    root = ListNode(nums[0])
    queue.append(root)
    i = 1

    while i < len(nums):
        node = queue.pop(0)
        if nums[i] is not None:
            node.next = ListNode(nums[i])
            queue.append(node.next)
        i += 1

    return root


lst = list(range(10))
link1 = create(lst)
p = link1
res = []

while p:
    res.append(p.val)
    p = p.next

print(res)
