# redo

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        new_dict = defaultdict(list)

        for words in strs:

            # sort the word, now in array
            sorted_word = sorted(words)

            # join back
            sorted_word = "".join(sorted_word)

            new_dict[sorted_word].append(words)
            
        # You may return the output in any order.
        answer = []

        for a in new_dict.values():
            answer.append(a)

        return answer
