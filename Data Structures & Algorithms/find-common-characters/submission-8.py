from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        # create a counter based of the first word
        d = Counter(words[0])

        for word in words:
            # create a map of each word
            temp_d = Counter(word)

            # update the min
            for char in d.keys():
                d[char] = min(d[char], temp_d[char])

        
        answer = []

        for ch, count in d.items():
            for _ in range(count):
                answer.append(ch)
        
        return answer