from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        sorted_by_freq = sorted(freq.keys(), key=lambda x: -freq[x])
        ans = 0
        count = 0

        for c in sorted_by_freq:
            ans += freq[c] * ((count // 8) + 1)
            count += 1
        
        return ans
