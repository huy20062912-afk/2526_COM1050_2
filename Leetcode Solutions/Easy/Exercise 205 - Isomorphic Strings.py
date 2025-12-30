# Exercise 205: Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_to_word = {}
        word_to_char = {}
        for x, y in zip(s,t):
            if x not in char_to_word and y not in word_to_char:
                char_to_word[x] = y
                word_to_char[y] = x
            elif x in char_to_word and char_to_word[x] != y:
                return False
            elif y in word_to_char and word_to_char[y] != x:
                return False
            else:
                continue
        return True