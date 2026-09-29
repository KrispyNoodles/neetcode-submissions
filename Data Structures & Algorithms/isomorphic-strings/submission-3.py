class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # creating a dict
        dict_s = {}

        # creating an additional set to use instead of values
        set_s = set()

        for i in range(len(s)):
            
            # map the t to s
            character_s = s[i]
            character_t = t[i]

            # if the character is not assigned, check if it has been assignef before if not assign it
            if character_s not in dict_s:

                # checking if character_t has been assigned previously before
                if character_t in set_s:
                    return False

                dict_s[character_s] = character_t
                set_s.add(character_t)

            # if it has been assigned before check if the charcter matches
            if dict_s[character_s] == character_t:
                continue
            else:
                return False
            
        return True
