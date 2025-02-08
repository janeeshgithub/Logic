class Solution(object):
    def decodeString(self, s):
        # Stack to store previous string and multiplier when encountering '['
        stack = []
        curNum = 0  # Stores the current number before '['
        curString = ""  # Stores the current decoded string
        for c in s:
            if c == '[':
                # Push the current string and number onto the stack
                stack.append(curString)
                stack.append(curNum)
                # Reset curString and curNum for the new bracketed expression
                curNum = 0
                curString = ""
            elif c == ']':
                # When ']' is encountered, pop the number and previous string
                num = stack.pop()  # Multiplier for the substring
                prevString = stack.pop()  # Previous string before '['
                # Expand the substring by repeating it num times and append it to the previous string
                curString = prevString + num * curString
            elif c.isdigit():
                # Construct the number (handles multi-digit cases)
                curNum = curNum * 10 + int(c)
            else:
                # Append regular characters to the current string
                curString += c

        return curString  # The final decoded string

# Test cases to validate the solution
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        "3[a]2[bc]",  # Expected output: "aaabcbc"
        "3[a2[c]]",  # Expected output: "accaccacc"
        "2[abc]3[cd]ef",  # Expected output: "abcabccdcdcdef"
        "10[a]",  # Expected output: "aaaaaaaaaa"
        "3[a2[b4[F]c]]"  # Expected output: "abFFFFcbFFFFcabFFFFcbFFFFc"
    ]

    for s in test_cases:
        print(f"Input: {s} => Output: {solution.decodeString(s)}")

