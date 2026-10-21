class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        answer = []

        for index, word in enumerate(words):
            # temp
            words_copy = words.copy()
            words_copy.remove(word)

            for temp_word in words_copy:
                # if any inside then do it
                if word in temp_word:
                    answer.append(word)
                    break

        return answer