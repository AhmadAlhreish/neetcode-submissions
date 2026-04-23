from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_hash:
                return [num_hash[complement], i]
            else:
                num_hash[n] = i