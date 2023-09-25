class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # Create a string with the length of each string and the string itself
        result = ""
        for s in strs:

            # Add the length of the string and the string itself
            result += str(len(s)) + ":" + s
        return result

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result, i = [], 0

        # While we haven't reached the end of the string
        while i < len(s):
            j = i
            while s[j] != ":":
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1 : j + length + 1])
            i = j + length + 1
        return result
           