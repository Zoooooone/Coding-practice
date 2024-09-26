class TreeNode:
    def __init__(self, val=0):
        self.left = -1
        self.right = -1
        self.val = val
        
    
class SegmentTree:
    def __init__(self, nums):
        self.size = len(nums)
        self.tree = [TreeNode() for _ in range(self.size * 4)]
        self.nums = nums
        if self.size > 0:
            self.build(0, 0, self.size - 1)
    
    def build(self, index, left, right):
        self.tree[index].left = left
        self.tree[index].right = right
        if left == right:
            self.tree[index].val = self.nums[left]
            return
        
        mid = left + (right - left) // 2
        left_index = index * 2 + 1
        right_index = index * 2 + 2
        self.build(left_index, left, mid)
        self.build(right_index, mid + 1, right)
