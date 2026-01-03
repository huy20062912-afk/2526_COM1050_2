# Exercise 345. Reverse Vowels of a String
class Solution:
    def reverseVowels(self, s: str) -> str:
        Vowels = 'AEIOUaeiou'
        left = 0
        right = len(s) - 1
        result_list = list(s)
        while left < right:
            if result_list[left] not in Vowels:
                left += 1
            if result_list[right] not in Vowels:
                right -= 1
            if result_list[left] in Vowels and result_list[right] in Vowels:
                result_list[left], result_list[right] = result_list[right], result_list[left]
                left += 1
                right -= 1
        return ''.join(result_list)