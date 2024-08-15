vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

class Solution:
    def reverseVowels(self, s: str) -> str:
        # store the vowel in the list and it's index in a dictionary
        stringVowels = []
        vowelIndices = {}
        for i in range(len(s)):
            if s[i] in vowels:
                stringVowels.append(s[i])
                vowelIndices[i] = len(stringVowels)-1
        
        stringVowels.reverse()

        # rebuild the string pulling from the reversed vowel list
        # when a vowel is expected
        result = ""
        for i in range(len(s)):
            if i in vowelIndices:
                result += stringVowels[vowelIndices[i]]
            else:
                result += s[i]

        return result

def main():
    solution = Solution()
    print(solution.reverseVowels("whatchuknowaboutrollingdowninthedeep"))

if __name__=="__main__":
    main()