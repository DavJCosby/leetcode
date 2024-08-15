class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)
        for i in range(length // 2):
            old = s[length-i-1]
            s[length-i-1] = s[i]
            s[i] = old
            

def main():
    for i in range(4):
        print(i)
    solution = Solution()
    print(solution.isPerfectSquare(256))