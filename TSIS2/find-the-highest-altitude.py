class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = 0
        mx = 0
        for i in gain:
            n += i
            if(mx < n):
                mx = n
        return mx
