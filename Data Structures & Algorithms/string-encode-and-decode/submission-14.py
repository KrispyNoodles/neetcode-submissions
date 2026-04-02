class Solution:

    def encode(self, strs: List[str]) -> str:

        # trying to get len#string
        # as a repeated pattern
        encoded_arr = []

        for string in strs:
            encoded_arr.append(str(len(string)))
            encoded_arr.append('#')
            encoded_arr.append(string)

        encoded_arr = "".join(encoded_arr)

        return encoded_arr


    def decode(self, s: str) -> List[str]:

        final_answer = []
        index = 0

        # looping through the index
        while index < len(s):

                length = ""

                # checking the length of the string
                # because it might be 1 or 2 or even 3 long
                while s[index].isdigit():
                    length += s[index]

                    # shift it after it has been retrieved to the length
                    index += 1
                
                # length is next char, this is assuming the length is 0-9 (DOES NOT WORK)
                # length = int(s[index+1])

                # retrieving the string as a slice of the entire string
                # start is the current index +2 to the length
                string = s[index+1:index+1+int(length)]

                # append it to the final_answer
                final_answer.append(string)
                
                # new current index is last + 1
                # there is no need to increment the index since this already shifts by 1
                index = index+1+int(length)
                    
        return final_answer

# time complexity of O(n) 
# because there is only a max while loop of size n

# space complexity of O(n) 
# because as the size of the array increases, the space needed increases too as well