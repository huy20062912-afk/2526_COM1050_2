# Exercise 290: Word Pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_to_word = {}
        word_to_char = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        for c, w in zip(pattern, s):
            if c not in char_to_word and w not in word_to_char:
                char_to_word[c]=w
                word_to_char[w]=c
            elif c in char_to_word and char_to_word[c] != w:
                return False
            elif w in word_to_char and word_to_char[w] != c:
                return False
            else:
                continue
        return True