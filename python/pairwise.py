from itertools import pairwise

nums = list(range(10))
s = "abcdefg"
dic = {"a": 1, "b": 2, "c": 3, "d": 4}

for x, y in pairwise(nums):
    print("list: ", (x, y))

for s1, s2 in pairwise(s):
    print("str: ", s1, s2)

for k, v in pairwise(dic):
    print("dict: ", k, v)
