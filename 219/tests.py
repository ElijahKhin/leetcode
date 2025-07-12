from solution import Solution

def test_1():
    nums = [1,2,3,1]
    k = 3 
    output = 1 
    sol = Solution()
    res = sol.containsNearbyDuplicate(nums,k)
    assert res == output

def test_2():
    nums = [1,0,1,1] 
    k = 1 
    output = 1
    sol = Solution()
    res = sol.containsNearbyDuplicate(nums,k)
    assert res == output

def test_3():
    nums = [1,2,3,1,2,3]
    k = 2 
    output = 0 
    sol = Solution()
    res = sol.containsNearbyDuplicate(nums,k)
    assert res == output
