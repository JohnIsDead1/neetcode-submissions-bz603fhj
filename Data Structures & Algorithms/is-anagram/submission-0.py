class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_string = ""
        t_string = ""

        for char in s:
            s_string += char
        s_string = "".join(sorted(s_string))


        for char in t:   
             t_string += char
        t_string = "".join(sorted(t_string))

        if s_string == t_string:
            return True
        else:
            return False

        