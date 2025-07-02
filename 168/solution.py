class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        clm = columnNumber
        while clm > 0:
            rem = clm % 26
            if rem == 0: rem = 26
            res += chr(65 + rem - 1)
            clm -= rem
            clm //= 26
        return res[::-1]

def test_1():
    columnNumber = 1
    output = 'A'
    sol = Solution()
    res = sol.convertToTitle(columnNumber)
    assert res == output

def test_2():
    columnNumber = 28
    output = 'AB'
    sol = Solution()
    res = sol.convertToTitle(columnNumber)
    assert res == output

def test_3():
    columnNumber = 701
    output = 'ZY'
    sol = Solution()
    res = sol.convertToTitle(columnNumber)
    assert res == output
