class Solution:
    def reverse(self, x: int) -> int:
        
        flip_str = str(x)

        # checking if it is minus remove the minus
        if x<0:
            flip_str = flip_str[1:]
            flip_str = flip_str[::-1]
            reverse_val = int(flip_str)
            reverse_val=-reverse_val

        else:
            flip_str = flip_str[::-1]
            reverse_val = int(flip_str)

        illegal_val = 2**31

        # checkinf if the reverser is larger than a 32bit int
        if reverse_val>illegal_val-1 or -illegal_val>reverse_val:
            return 0
        else:
            return reverse_val