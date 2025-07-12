from typing import List

class Solution:
        def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
            items1.sort()
            items2.sort()
            n1 = len(items1)
            n2 = len(items2)
            i = j = 0
            res = []
            while i < n1 and j < n2: 
                if items1[i][0] == items2[j][0]:
                    val = items1[i][1] + items2[j][1]
                    res.append([items1[i][0], val]) 
                    i += 1 
                    j += 1
                else:
                    res.append(min(items1[i], items2
                    break
            while i < n1:
                res.append(items1[i]) 
                i += 1
            while j < n2:
                res.append(items2[j]) 
                j += 1
            return res



if __name__ == "__main__":
    items1 = [[1,1],[4,5],[3,8]]
    items2 = [[3,1],[1,5]]
    output = [[1,6],[3,9],[4,5]]
    sol = Solution()
    res = sol.mergeSimilarItems(items1, items2)
    print(res)
    print(res == output)
     

