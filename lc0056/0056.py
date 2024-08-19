from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        
        rebuild = []
        rebuild.append(intervals[0])

        top = rebuild[-1]
        for interval in intervals:
            if interval[0] <= top[1]:
                top[1] = max(interval[1], top[1])
            else:
                rebuild.append(interval)
                top = rebuild[-1]
        return rebuild
    

def main():
    solution = Solution()
    print(solution.merge([[-3, -2], [-1, 0], [1, 4], [4, 5], [3, 7]]))

if __name__=="__main__":
    main()