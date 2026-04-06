from collections import deque
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        tocheck = deque()
        sol = set()
        tocheck.append((nums, []))
        while tocheck:
            curr = tocheck.popleft() # (remaining to add, subset in making)
            sol.add(tuple(sorted(curr[1])))
            if curr[0]:
                tocheck.append((curr[0][:-1], curr[1]))
                tocheck.append((curr[0][:-1], curr[1] + [curr[0][-1]]))
        return list(sol)
        
        