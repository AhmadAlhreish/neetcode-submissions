class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for string in strs:
            key = tuple(sorted(string))
            if key not in count:
                count[key] = [string]
            else:
                count[key].append(string)
        return list(sorted(count.values()))
            
