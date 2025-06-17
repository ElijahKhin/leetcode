import pytest
from typing import List

class Solution:
    def Merge(self, arr, l, m, r):
        sl = m - l
        sr = r - m
        lhs = [0] * sl
        rhs = [0] * sr

        for i in range(sl):
            lhs[i] = arr[l+i]
        for i in range(sr):
            rhs[i] = arr[m+i]
        
        i = j = 0
        k = l
        while i < sl and j < sr: 
            if lhs[i] < rhs[j]:
                arr[k] = rhs[j]
                j += 1
            else:
                arr[k] = lhs[i]
                i += 1
            k += 1
        while i < sl:
            arr[k] = lhs[i]
            k += 1
            i += 1
        while j < sr:
            arr[k] = rhs[j]
            k += 1
            j += 1
    
    def MergeSort(self, arr, l, r):
        if r - l > 1:
            m = l + (r - l) // 2
            self.MergeSort(arr, l, m)
            self.MergeSort(arr, m, r)
            self.Merge(arr, l, m, r)

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hand = {}
        for i in range(len(score)):
            hand[score[i]] = i
        self.MergeSort(score, 0, len(score))
        answer = [0] * len(score)
        for i, score in enumerate(score):
            if i == 0:
                answer[hand[score]] = "Gold Medal" 
            elif i == 1:
                answer[hand[score]] = "Silver Medal" 
            elif i == 2:
                answer[hand[score]] = "Bronze Medal" 
            else:
                answer[hand[score]] = str(i + 1)
        return answer

def test_1():
    sol = Solution()
    score1 = [5,4,3,2,1]
    output1 = ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
    assert(sol.findRelativeRanks(score1) == output1)

def test_2():
    sol = Solution()
    score2 = [10,3,8,9,4]
    output2 = ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
    assert(sol.findRelativeRanks(score2) == output2)

if __name__ == "__main__":
    pass

