class Solution:

    def encode(self, strs: List[str]) -> str:
        # so i guess the solution of this the encoding part was to 
        # get the len of the word concatenate with the word and put a dlimeter on the spot for the encoding
        encoded =""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded
    def decode(self, s: str) -> List[str]:
        # i would have 4#neet4#code4#love
        i = 0
    
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j + 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end
        return res

        