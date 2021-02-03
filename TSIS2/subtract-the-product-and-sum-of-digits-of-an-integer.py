class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        sm = 0
        pd = 1
        for i in n:
            i = int(i)
            sm += i
            pd *= i

        return pd-sm
