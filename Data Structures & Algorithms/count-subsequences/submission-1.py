class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        patterns = {} # letters : [patterns]
        seenpatterns = {} # patterns : counts
        seenpatterns[""] = 1
        
        for i in range(len(t)):
            if t[i] not in patterns:
                patterns[t[i]] = [t[:i + 1]]
            else:
                patterns[t[i]].append(t[:i + 1])
            seenpatterns[t[:i + 1]] = 0
        for c in s:
            if c in patterns:
                for pattern in reversed(patterns[c]):
                    seenpatterns[pattern] += seenpatterns[pattern[:-1]]
        for key in seenpatterns:
            print(key, seenpatterns[key])
        return seenpatterns[t]

        