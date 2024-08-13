class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        searchMin = 0
        searchMax = 46341
        while True:
            search = (searchMin + searchMax) // 2
            if (searchMax - searchMin) == 1:
                return False
                
            sq = search * search
            if sq > num:
                searchMax = search
            elif sq < num:
                searchMin = search
            elif sq == num:
                return True

def main():
    solution = Solution()
    print(solution.isPerfectSquare(256))

if __name__=="__main__":
    main()