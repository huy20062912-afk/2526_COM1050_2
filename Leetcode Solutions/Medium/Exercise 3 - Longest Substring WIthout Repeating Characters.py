# Exercise 3: Longest substring without repeating characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        final_result = 0
        for right in range(len(s)):
            current_char = s[right]
            if current_char in char_map and char_map[current_char] >= left:
                left = char_map[current_char] + 1
            char_map[current_char] = right
            window_length = right - left + 1
            final_result = max(final_result, window_length)
        return final_result