class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = []
        l2 = []
        for i in s:
            l1.append(ord(i))
        for i in t:
            l2.append(ord(i))
        l1.sort()
        l2.sort()
        print(l1)
        print(l2)
        if l1 == l2:
            return True
        else:
            return False

        
s = "rat"
t = "car"
tst = Solution()
print(tst.isAnagram(s,t))

