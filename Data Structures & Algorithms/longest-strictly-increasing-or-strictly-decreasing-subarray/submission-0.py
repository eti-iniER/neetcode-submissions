class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        inc = 1
        dec = 1
        last = None

        for v in nums:
            if last is not None:
                if v > last:
                    inc += 1
                    dec = 1
                elif v < last:
                    inc = 1
                    dec += 1
                else:
                    inc = dec = 1
            
            last = v
            res = max(res, inc, dec)
        
        return res
