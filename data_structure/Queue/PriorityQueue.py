class Heapq:
    def __init__(self, nums: list):
        self.nums = nums
        self.heapify()

    def heapAdjust(self, index: int, end: int):
        left, right = index * 2 + 1, index * 2 + 2
        while True:
            min_index = index
            if left <= end and self.nums[left] < self.nums[min_index]:
                min_index = left
            if right <= end and self.nums[right] < self.nums[min_index]:
                min_index = right
            if min_index == index:
                break
            self.nums[index], self.nums[min_index] = self.nums[min_index], self.nums[index]
            index = min_index
            left, right = index * 2 + 1, index * 2 + 2

    def heapify(self):
        size = len(self.nums)
        for i in range((size - 2) // 2, -1, -1):
            self.heapAdjust(i, size - 1)

    def heappush(self, val: int):
        self.nums.append(val)
        i = len(self.nums) - 1
        while (i - 1) // 2 >= 0:
            parent = (i - 1) // 2
            if self.nums[parent] > self.nums[i]:
                self.nums[parent], self.nums[i] = self.nums[i], self.nums[parent]
                i = parent
            else:
                break

    def heappop(self):
        if not self.nums:
            raise Exception("Priority queue is empty.")
        top = self.nums[0]
        last = self.nums.pop()
        if self.nums:
            self.nums[0] = last
            self.heapAdjust(0, len(self.nums) - 1)
        return top
