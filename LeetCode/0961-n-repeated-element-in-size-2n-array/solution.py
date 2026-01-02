from typing import List


# 1. Case1: 길이 2인 subarray에 major element가 있는 경우
# - 인접 두 칸에 major가 있다는 것
# 2. Case2: 모든 길이 2 subarray에 major가 정확히 1개씩 있는 경우
# - 인접 두 칸에 major가 절대 2개가 없다 = 모든 major가 불연속
# - 이 때, major로 시작하는 길이 4인 subarray는 major가 2개 있다는 것이 확실함
# Detail)
# major로 시작하는 4칸: [M, ?, ?, ?]
# 인접 불가 가정:
# - 위치 0: M (major)
# - 위치 1: X (non-major여야 함, 연속 불가하므로)
# - 위치 2, 3: 둘 중 적어도 하나는 M이어야 함
# 전체 배열: 2N칸, major N개, non-major N개
# 만약 [M, X, X, X] 패턴이 반복된다면:
# - major 1개당 non-major 3개 필요한데, 실제로 1:1 비율이므로 가정에 모순
# 따라서 [M, X, X, X]가 계속될 수 없고, 4칸 안에 반드시 major가 2개 들어감
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for k in range(1, 4):
            for i in range(len(nums) - k):
                if nums[i] == nums[i + k]:
                    return nums[i]

        return 0
