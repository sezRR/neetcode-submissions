class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for st in strs:
            encoded_str += str(len(st)) + "#" + st
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        ind = 0
        print(s)
        while ind < len(s):
            decoded_str = ""
            will_read = ""
            while s[ind] != '#':
                will_read += s[ind]
                ind += 1
            to_read = int(will_read)
            for j in range(to_read):
                decoded_str += s[j + ind + 1]
            res.append(decoded_str)
            ind += to_read + 1 
        return res