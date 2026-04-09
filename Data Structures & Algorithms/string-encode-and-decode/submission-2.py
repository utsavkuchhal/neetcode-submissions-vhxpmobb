class Solution:

    def encode(self, strs: List[str]) -> str:     
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # find length
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            
            # extract string
            word = s[j+1 : j+1+length]
            res.append(word)
            
            # move pointer
            i = j + 1 + length
        
        return res