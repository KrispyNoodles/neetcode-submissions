class Solution:
    def isPalindrome(self, s: str) -> bool:

        # true for all characters with only 1
        if len(s) == 1:
            return True
        
        # removing all characters
        alphabet_set = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                        'p','q','r','s','t','u','v','w','x','y','z'}
        
        number_set = {'0','1','2','3','4','5','6','7','8','9'}

        # convert all to small caps
        temp_array = []

        # looping through cha
        for characters in s:
            characters = characters.lower()

            if characters in alphabet_set or characters in number_set:
                temp_array.append(characters)
        
        print(temp_array)

        # len of 1 is true
        if len(temp_array)==1:
            return True
                
        elif temp_array == temp_array[::-1]:
            return True
        else:
            return False