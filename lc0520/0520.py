class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        
        firstUppercase = word[0].isupper()
        remainingHasUppercase = False
        remainingHasLowercase = False
        for c in word[1:]:
            if c.isupper():
                remainingHasUppercase = True
            else:
                remainingHasLowercase = True
            if remainingHasUppercase and remainingHasLowercase:
                return False
        
        # Because all scenarios where remainingHasUppercase and remaininHasLowercase both
        # are True by this point would return early, we don't need to check here
        case1 = firstUppercase and remainingHasUppercase
        case2 = not firstUppercase and remainingHasLowercase
        case3 = firstUppercase and remainingHasLowercase
        return case1 or case2 or case3

def main():
    solution = Solution()
    print(solution.detectCapitalUse("Lmao"))

if __name__=="__main__":
    main()