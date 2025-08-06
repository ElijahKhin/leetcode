class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True

        ns = len(s)
        nt = len(t)
        if ns > nt:
            return False

        slow = fast = 0 
        while slow < ns and fast < nt:
            if s[slow] == t[fast]:
                slow += 1
            fast += 1
        if slow == ns:
            return True
        return False

if __name__ == "__main__":
    s = "axc"
    t = "ahbgdc"
    sol = Solution()
    print(sol.isSubsequence(s, t))
