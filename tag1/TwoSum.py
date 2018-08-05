class Solution(object):
    def __init__(self, sums, target):
        self.sums = sums
        self.target = target

    def twoSum(self):
        for i in range(0, len(self.sums)):
            for j in range(i, len(self.sums)):
                if self.sums[i] + self.sums[j] == self.target:
                    return i, j

if __name__ == '__main__':
    sums = (2, 7, 11, 15)
    target = 9
    ts = Solution(sums, target)
    print(ts.twoSum())


