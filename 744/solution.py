from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target == 'z':
            return letters[0]
        l = 0
        r = len(letters)
        mn = 0
        while l<r:
            m = l + (r-l) // 2
            if letters[m] == target:
                l = m + 1
            elif ord(letters[m]) < ord(target):
                l = m + 1
            else:
                if mn != 0 and ord(letters[mn]) > ord(letters[m]):
                    mn = m 
                elif mn == 0:
                    mn = m
                r = m
        return letters[mn]



if __name__ == "__main__":
    letters = ["c","f","j"]
    target = 'j'
    output = 'c'
    sol = Solution()
    val = sol.nextGreatestLetter(letters, target)
    print(val)
    print(val == output)
