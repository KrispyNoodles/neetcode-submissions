class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split()
        if len(pattern)!=len(s):
            return False

        wordtochar = {}
        chartoword = {}

        for char, word in zip(pattern ,s):

            if char in chartoword and chartoword[char]!=word:
                return False

            if word in wordtochar and wordtochar[word]!=char:
                return False

            # add both doods in
            wordtochar[word]=char
            chartoword[char]=word
        
        return True
