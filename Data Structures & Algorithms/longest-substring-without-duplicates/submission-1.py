class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length_without_duplicate = 0
        substring = ""
        for i in s:
            if i in substring:
                substring = substring[substring.index(i)+1:]
            substring = substring+i
            if len(substring)>max_length_without_duplicate:
                max_length_without_duplicate = len(substring)
        return max_length_without_duplicate
            