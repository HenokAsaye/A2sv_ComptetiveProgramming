# Problem: Decode XORed Array - https://leetcode.com/problems/decode-xored-array/description/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]
        for num in encoded:
            decoded.append(num ^ decoded[-1])
        return decoded
