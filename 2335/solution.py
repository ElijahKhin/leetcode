from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        cnt = 0
        while sum(amount) != 0:
            amount.sort(reverse=True)
            cnt += 1
            amount[0] -= 1
            if amount[1] != 0:
                amount[1] -= 1
        return cnt



if __name__ == "__main__":
    amount = [5,0,0]
    output = 5
    sol = Solution()
    res = sol.fillCups(amount)
    print(res)
    print(res == output)
