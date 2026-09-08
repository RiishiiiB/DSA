class Solution:
    def lengthOfLastWord(self, text: str) -> int:
        text = text.strip()
        length = 0
        for index in range(len(text) - 1, -1, -1):
            if text[index] == " ":
                break
            length += 1
        return length