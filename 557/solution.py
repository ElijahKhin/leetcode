class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ans = []
        for word in words:
            word = word[::-1]
            ans.append(word)
        return ' '.join(ans)


                


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    sol = Solution()
    print(sol.reverseWords(s))


