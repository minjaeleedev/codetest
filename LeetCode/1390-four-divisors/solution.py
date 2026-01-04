from typing import List


# n - len(nums)
# M - max(nums[i])
# time complexity
# 1. sieve initialization - O(sqrt M log log M)
# 2. divisor calculation - O(sqrt M / log M) - number of primes below M
# total - O(n sqrt M / log M + sqrt M log log M)
# space complexity: O(M)
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        primes, cache = self.init_with_sieve()

        def four_divisor(n: int) -> int:
            if cache[n] != -1:
                return cache[n]

            temp = n
            prime_factor = 0
            s = 1 + n  # 1, self
            for p in primes:
                if p * p > n:
                    break

                if temp % p:
                    # p is not prime factor
                    continue

                e = 0  # exponential
                while temp % p == 0:
                    temp = temp // p
                    e += 1

                prime_factor += 1

                # case1: n is p^3 (like 27 -> 1,3,9,27)
                if temp == 1 and e == 3 and prime_factor == 1:
                    cache[n] = 1 + p + p**2 + p**3
                    return cache[n]

                # n is p^2*q or p^3*q etc. n is not four divisor.
                if e > 1:
                    cache[n] = 0
                    return cache[n]

                s += p

            if temp > 1:
                # case2: n is p*q (like 21 -> 1,3,7,21)
                prime_factor += 1
                s += temp

            cache[n] = s if prime_factor == 2 else 0
            return cache[n]

        res = 0
        for n in nums:
            s = four_divisor(n)
            res += s

        return res

    def init_with_sieve(self):
        N = 317  # sqrt 100000
        is_prime = [True] * N
        cache = [-1] * 100001
        primes = []
        is_prime[0] = is_prime[1] = False
        cache[0] = cache[1] = 0
        p = 2
        while p * p <= N:
            if is_prime[p]:
                cache[p] = 0
                primes.append(p)
                i = p * p
                # sieve
                while i < N:
                    is_prime[i] = False
                    i += p

            p += 1 + (p & 1)  # jump to next odd number

        j = int((N**0.5 + 1)) | 1
        while j < N:
            if is_prime[j]:
                cache[p] = 0
                primes.append(j)

            j += 2

        return primes, cache
