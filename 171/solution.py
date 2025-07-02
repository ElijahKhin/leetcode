class Solution:
    def titleToNumber(self, columnTitle: int) -> str:
        base = len(columnTitle)
        res = 0
        for ch in columnTitle:
            res += (ord(ch) - 65 + 1) * 26**(base-1)
            base -= 1
        return res


def test_1():
    columnTitle = 'A'
    output = 1
    sol = Solution()
    res = sol.titleToNumber(columnTitle)
    assert res == output

def test_2():
    columnTitle = 'AB'
    output = 28
    sol = Solution()
    res = sol.titleToNumber(columnTitle)
    assert res == output

def test_3():
    columnTitle = 'ZY'
    output = 701
    sol = Solution()
    res = sol.titleToNumber(columnTitle)
    assert res == output
