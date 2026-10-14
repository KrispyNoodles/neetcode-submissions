from collections import Counter

class Solution:

    def commonChars(self, words: List[str]) -> List[str]:
        
        # lets make the first word in the dict the dict
        d = Counter(words[0])

        for word in words:

            # build a counter for each word and then compare the min
            temp_d = Counter(word)

            for key in d.keys():
                # update the key to be the min of both
                d[key] = min(d[key], temp_d[key])
        
        answer= []

        # building the answer
        for key, values in d.items():

            for _ in range(values):
                answer.append(key)

        return answer
