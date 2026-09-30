class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        collector = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                collector.append(grid[r][c])

        # finding len
        dup = sum(collector)-sum(set(collector))

        missing = sum(range(len(collector)+1))-sum(set(collector))

        return [dup, missing]