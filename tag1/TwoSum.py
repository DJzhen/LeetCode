"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

class Solution(object):
    def __init__(self, sums, target):
        self.sums = sums
        self.target = target

    def twoSum(self):
        for i in range(0, len(self.sums)):
            for j in range(i, len(self.sums)):
                if self.sums[i] + self.sums[j] == self.target:
                    return [i, j]

if __name__ == '__main__':
    sums = (2, 7, 11, 15)
    target = 9
    ts = Solution(sums, target)
    print(ts.twoSum())


