class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        # creating a dict based off the first word
        first_word = Counter(words[0])

        for word in words:

            # create a counter for each word
            curr_counter = Counter(word)

            # take the min_between the two
            for char in first_word:
                first_word[char] = min(curr_counter[char], first_word[char])

        answer = []
        
        for char in first_word:
            for number in range(first_word[char]):
                answer.append(char)

        return answer
