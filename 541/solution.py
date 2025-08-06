class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        l = 0 # + 2*k
        ans = [''] * n
        if n < k:
            r = n - 1
            while l <= r:
                ans[l], ans[r] = s[r], s[l]
                r -= 1
                l += 1
        else:
            while l < n:
                if n - l >= k:
                    i, r = l, l + k - 1
                    while i <= r:
                        ans[i], ans[r] = s[r], s[i]
                        r -= 1
                        i += 1
                    idx = l + k
                    while idx < l + 2*k and idx < n:
                        ans[idx] = s[idx]
                        idx += 1
                else:
                    r = n - 1
                    while l < n:
                        ans[l], ans[r] = s[r], s[l]
                        r -= 1
                        l += 1
                    break
                l += 2 * k

        return ''.join(ans)


if __name__ == "__main__":
    s = "abcdefg"
    k = 8
    sol = Solution()
    print(sol.reverseStr(s, k))
