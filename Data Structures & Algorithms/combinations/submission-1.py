class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        current = []
        chosen = set()

        def backtrack(lim=0):
            if len(current) == k:
                combinations.append(list(current))
                return
            
            for i in range(lim+1, n+1):
                current.append(i)
                backtrack(i)
                current.pop()
        
        backtrack()
        return combinations
