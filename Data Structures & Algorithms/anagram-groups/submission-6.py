from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_map = defaultdict(list)
        
        # creating a dict
        for word in strs:
            sort_word = sorted(word)
            # join them back
            sort_word = "".join(sort_word)
            word_map[sort_word].append(word)
        
        answer = []

        for i in word_map.values():
            answer.append(i)
        
        return answer
