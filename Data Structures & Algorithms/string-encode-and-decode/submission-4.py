# answer soln
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:

        final_response = ""

        # creating the encoded pattern
        for string in strs:
            final_response += str(len(string)) + '#' + string

        return final_response

    def decode(self, s: str) -> List[str]:
        
        # checking for empty
        if not s:
            return []

        final_arr = []

        # first number
        counter = int(s[0])
        index = 0

        while index < len(s):

            length_str = ""

            # if the int is longer than 2 characters
            while s[index].isdigit():
                length_str += s[index]
                index += 1

            # skipping the hash
            index+=1
            
            # extracting the word
            word = s[index: (index + int(length_str))]

            # including the word to the final_arr
            final_arr.append(word)

            # skipping the index
            index = index + int(length_str)

        
        # print(index)
        return final_arr