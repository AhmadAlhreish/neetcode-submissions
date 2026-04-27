class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_count = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in hash_count:
                return [hash_count[complement], i]
            hash_count[n] = i
        