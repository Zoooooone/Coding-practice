class TreeNode:
    def __init__(self, val=0):
        self.left = -1
        self.right = -1
        self.val = val
        

class SegmentTree:
    def __init__(self, nums, function):
        self.size = len(nums)
        self.tree = [TreeNode() for _ in range(self.size * 4)]
        self.nums = nums
        self.function = function
        if self.size > 0:
            self.build(0, 0, self.size - 1)
    
    def build(self, index, left, right):
        self.tree[index].left = left
        self.tree[index].right = right
        if left == right:
            self.tree[index].val = self.nums[left]
            return
        
        mid = left + (right - left) // 2
        left_index, right_index = index * 2 + 1, index * 2 + 2
        self.build(left_index, left, mid)
        self.build(right_index, mid + 1, right)
        self.pushup(index)

    def pushup(self, index):
        left_index, right_index = index * 2 + 1, index * 2 + 2
        self.tree[index].val = self.function(self.tree[left_index].val, self.tree[right_index].val)

    def update_point(self, i, val):
        self.nums[i] = val
        self.__update_point(i, val, 0, 0, self.size - 1)

    def __update_point(self, i, val, index, left, right):
        if self.tree[index].left == self.tree[index].right:
            self.tree[index].val = val
            return
        
        mid = left + (right - left) // 2
        left_index, right_index = index * 2 + 1, index * 2 + 2
        if i <= mid:
            self.__update_point(i, val, left_index, left, mid)
        else:
            self.__update_point(i, val, right_index, mid + 1, right)
        self.pushup(index)

    def query_interval(self, q_left, q_right):
        return self.__query_interval(q_left, q_right, 0, 0, self.size - 1)

    def __query_interval(self, q_left, q_right, index, left, right):
        if q_left <= left and q_right >= right:
            return self.tree[index].val
        if q_left > right or q_right < left:
            return float("inf")
        
        mid = left + (right - left) // 2
        left_index, right_index = index * 2 + 1, index * 2 + 2
        res_left, res_right = float("inf"), float("inf")
        if q_left <= mid:
            res_left = self.__query_interval(q_left, q_right, left_index, left, mid)
        if q_right > mid:
            res_right = self.__query_interval(q_left, q_right, right_index, mid + 1, right)
        return self.function(res_left, res_right)


if __name__ == "__main__":
    nums = [1, 5, 3, 7, 3, 2, 5, 7]
    segment_tree = SegmentTree(nums, min)
    print(segment_tree.query_interval(1, 5))
    segment_tree.update_point(5, 6)
    print(segment_tree.query_interval(1, 5))
