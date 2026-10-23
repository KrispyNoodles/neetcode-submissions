class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        answer=0

        for word in words:
            m = Counter(word)
            mc = Counter(chars)

            for key, value in m.items():
                if mc[key]<m[key]:
                    break
            else:
                answer+=len(word)
            # checking all values in count positive
            
            
        return answer
            