class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        decoded_str = []
        while i < len(s):
             while s[j] != "#":
                 j += 1
             length = int(s[i:j])
             i = j + 1
             j = i + length
             decoded_str.append(s[i:j])
             i = j
        return decoded_str
