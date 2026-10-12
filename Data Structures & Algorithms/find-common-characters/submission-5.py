class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        # creating a dict based off the first word
        first_word = Counter(words[0])

        for word in words:

            # create a counter for each word
            curr_counter = Counter(word)

            for char in first_word:
                
                # add in
                first_word[char] = min(curr_counter[char], first_word[char])
        
        answer = []

        for key, number in first_word.items():
            for i in range(number):
                answer.append(key)

        return answer