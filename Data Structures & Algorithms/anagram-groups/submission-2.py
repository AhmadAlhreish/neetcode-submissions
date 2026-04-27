class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_count = {}

        for string in strs:
            key = tuple(sorted(string))
            if key not in hash_count:
                hash_count[key] = []
            hash_count[key].append(string)
        return list(hash_count.values())