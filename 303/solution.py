from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.n_ = len(nums)
        self.nums_ = nums
        self.ps_ = [0] * (self.n_ + 1)
        for i in range(1, self.n_+1):
            self.ps_[i] = self.ps_[i-1] + self.nums_[i-1]
        print(self.ps_)

    def sumRange(self, left: int, right: int) -> int:
        return self.ps_[right + 1] - self.ps_[left]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    query = [0,2]
    q1, q2 = [2,5],[0,5]
    obj = NumArray(nums)
    print(obj.sumRange(query[0], query[1]))
    print(obj.sumRange(q1[0], q1[1]))
    print(obj.sumRange(q2[0], q2[1]))
