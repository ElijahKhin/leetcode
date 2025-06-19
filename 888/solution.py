from typing import List

class Solution:
     
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sa = sum(aliceSizes)
        sb = sum(bobSizes)
        if sa >= sb:
            bsum = sa
            ssum = sb
            small = bobSizes
            big = aliceSizes
        else:
            bsum = sb
            ssum = sa
            small = aliceSizes
            big = bobSizes


        val = (ssum - bsum) // 2
        small.sort()
        big.sort()
        for i in range(len(small)):
            for j in range(len(big)):
                if small[i] - big[j] == val:
                    if sa >= sb:
                        return [big[j], small[i]]
                    else:
                        return [small[i], big[j]]

def test_1():
    sol = Solution()
    aliceSizes, bobSizes = [1,1], [2,2]
    output = [1,2]
    res = sol.fairCandySwap(aliceSizes, bobSizes)

    assert res == output

def test_2():
    sol = Solution()
    aliceSizes, bobSizes = [1,2], [2,3]
    output = [1,2]
    res = sol.fairCandySwap(aliceSizes, bobSizes)

    assert res == output

def test_3():
    sol = Solution()
    aliceSizes, bobSizes = [2], [1,3]
    output = [2,3]
    res = sol.fairCandySwap(aliceSizes, bobSizes)

    assert res == output
