class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)
        for i in range(length // 2):
            old = s[length-i-1]
            s[length-i-1] = s[i]
            s[i] = old
            

def main():
    solution = Solution()
    solution.reverseString(["a", "b", "c", "d"])

if __name__=="__main__":
    main()