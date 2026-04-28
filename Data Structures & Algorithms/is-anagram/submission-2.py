class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return true if anagram else false
        #use dictionary to store each letter of the string

        count_char = {}

        if len(s) != len(t):
            return False

        for char in s:
            count_char[char] = count_char.get(char, 0) + 1
        for char in t:
            count_char[char] = count_char.get(char, 0) - 1
            #checking if char count is equeal between s and t
            if count_char[char] < 0:
                return False
        return True