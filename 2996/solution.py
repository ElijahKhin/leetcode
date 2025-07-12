from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [(0, 0)] * n
        pref[0] = (1, nums[0])
        cnt = 1
        for i in range(1,n):
            if nums[i] - nums[i - 1] == 1:
                cnt += 1
                pref[i] = (cnt, pref[i-1][1] + nums[i])
            else:
                break
        mm = max(pref)[1]
        st = set(nums)
        while mm in st:
            mm += 1
        return mm





def main() -> None:
    nums = [37,1,2,9,5,8,5,2,9,4]
    output = 38
    sol = Solution()
    print(sol.missingInteger(nums))

if __name__ == "__main__":
    main()
