from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = dict(items1)
        
        for key, val in items2:
            if d.get(key, 0) != 0:
                d[key] += val
            else:
                d[key] = val
        return sorted(d.items())

if __name__ == "__main__":
    items1 = [[2,9],[24,4],[11,1],[16,3],[1,4],[28,3],[23,8],[3,3]]
    items2 = [[7,6],[12,7],[9,5],[22,4],[6,3],[17,1]]
    output = [[1,7],[2,4],[7,1]]
    sol = Solution()
    res = sol.mergeSimilarItems(items1, items2)
    print(res)
    print(res == output)
     

