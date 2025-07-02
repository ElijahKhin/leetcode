from solution import Solution

def test0():
    word0 = "abbccdd"
    word1 = "abcd"
    word2 = "abccccccd"
    word3 = "a"
    output0 = 4
    output1 = 4
    output2 = 4
    output3 = 1
    sol = Solution()
    res0 = sol.getNumberOfElements(word0)
    res1 = sol.getNumberOfElements(word1)
    res2 = sol.getNumberOfElements(word2)
    res3 = sol.getNumberOfElements(word3)
    assert res0 == output0 
    assert res1 == output1 
    assert res2 == output2 
    assert res3 == output3 

def test00():
    word = "abbccdd"
    output0 = (0,1,2,3,4,5,6)
    output1 = (1,2,3)
    output2 = (2,3,4)
    output3 = (4,5,6)
    sol = Solution()
    res0 = sol.getTupleKey(0, len(word))
    res1 = sol.getTupleKey(1, len(word[1:4]))
    res2 = sol.getTupleKey(2, len(word[2:5]))
    res3 = sol.getTupleKey(4, len(word[4:7]))
    assert res0 == output0
    assert res1 == output1
    assert res2 == output2
    assert res3 == output3

def test1():
    word = "aabbccdd"
    k = 7 
    output = 5
    sol = Solution()
    res = sol.possibleStringCount(word, k)
    assert res == output

def test2():
    word = "aabbccdd"
    k = 8 
    output = 1
    sol = Solution()
    res = sol.possibleStringCount(word, k)
    assert res == output

def test3():
    word = "aaabbb"
    k = 3
    output = 8
    sol = Solution()
    res = sol.possibleStringCount(word, k)
    assert res == output
