from typing import List


class Solution:
    """
    Bitwise Operation Approach

    Intuition
    1. 1을 더하는 연산(x+1)을 bitwise operation 관점으로 보기
        - LSB->MSB 방향에서 첫 번째 0 bit을 1로 flip
        - 그 전에 나타나는 모든 1 bit을 0으로 flip
        - ex) 10011 -> 10100
    2. x | (x+1)의 의미
        - LSB->MSB 방향에서 첫번째 0 bit을 1로 flip하는 연산
        - ex) 10011 | (10100) = 10111
    3. x | (x+1) = n을 만족하는 x의 후보들
        - n에서 LSB->MSB 방향 첫번째 0 bit 이전 1 bit 중 하나를 0으로 만들면 x임
        - ex) 10111 -> x: 10011 or 10101 or 10110
    3. x | (x+1) = n을 만족하는 최소의 x
        - n에서 LSB->MSB 방향 첫번째 0 bit 위치를 pos로 정의
        - (pos - 1)을 0 bit으로 flip한 값이 최소인 x이다.
    """

    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        """
        Implementation
        pos를 찾는 방법
        - 현재 bit 위치를 추적할 변수 d
        - n & d 가 0이 아닐 때까지 d를 1씩 left shift한다
        - res는 n에서 d를 뺀 값이 됨
        """
        for i in range(len(nums)):
            res = -1
            d = 1
            while (nums[i] & d) != 0:
                res = nums[i] - d
                d <<= 1
            nums[i] = res

        return nums

    def minBitwiseArrayV2(self, nums: List[int]) -> List[int]:
        """
        Implementation
        (pos - 1)의 1 bit을 flip하기
        1. rightmost zero를 찾기 위한 과정 = rightmost one을 이용한 트릭
            - ~n : rightmost zero -> 1
            - n + 1 : rightmost zero -> 1
            - (n+1) & ~n : 이러면 pos 위치만 1 bit이 되고 나머지는 0
        2. 실제 찾고싶은 위치는 pos - 1 이므로, right shift 추가
        3. 해당 값을 뒤집어서 n과 AND 연산
        """
        res = []
        for n in nums:
            if n & 1:
                res.append(n & ~(((n + 1) & ~n) >> 1))
            else:
                res.append(-1)
        return res
