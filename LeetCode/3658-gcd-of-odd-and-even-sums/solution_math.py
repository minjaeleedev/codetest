class Solution:
    """
    Approach 2: Mathematics

    Observe that gcd(n^2, n(n+1))=n x gcd(n,n+1)

    Since two consecutive integers are always coprime, gcd(n,n+1)=1

    Therefore, gcd(n^2 ,n(n+1))=n
    """

    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
