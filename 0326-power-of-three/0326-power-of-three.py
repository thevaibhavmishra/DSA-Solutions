class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        s = n
        k = 0
        while s>1:
            s = s//3
            k+=1
        return 3**k == n