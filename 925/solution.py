class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        nl = len(name)
        nr = len(typed)
        l = r = 0
        for l in range(nl):
            if name[l] == typed[r]:
                l += 1
                r += 1
                if l < nl and name[l] != name[l+1]:
                    while r < nr and typed[r] == typed[r-1]:
                        r += 1
            else:
                print("here1")
                return False
        if r != nr:
            print("here4")
            return False
        return True


if __name__ == "__main__":
    name = "leelee"
    typed = "lleeelee"
    sol = Solution()
    print(sol.isLongPressedName(name, typed))
