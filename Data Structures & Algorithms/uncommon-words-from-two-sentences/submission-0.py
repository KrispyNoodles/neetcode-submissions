class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        pass

        split_1 = s1.split()
        split_2 = s2.split()
        
        dict_1 = Counter(split_1)
        dict_2 = Counter(split_2)

        answer = []

        for word, value in dict_1.items():
            if word not in dict_2 and value==1:
                answer.append(word)

        for word, value in dict_2.items():
            if word not in dict_1 and value==1:
                answer.append(word)
                
        return answer
