from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        cnt = 0
        for fruit in fruits:
            for basket in baskets:
                if fruit <= basket:
                    baskets.remove(basket)
                    cnt += 1
                    break
        return len(fruits) - cnt


        
        
if __name__ == "__main__":
    fruits = [1,3,6]
    baskets = [2,5,2]
    output = 1 
    sol = Solution()
    res = sol.numOfUnplacedFruits(fruits, baskets)
    print(res == output)
