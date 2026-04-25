class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Step 2: Sort by frequency (descending) and take top k
        # sorted returns list of keys sorted by their frequency values
        result = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        
        # Step 3: Return first k elements
        return result[:k]