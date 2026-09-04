class Solution:
    def romanToInt(self, s: str) -> int:
        roman = s
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        answer = 0
        for i in range(len(roman)):
            current = values[roman[i]]
            if i + 1 < len(roman):
                next_value = values[roman[i + 1]]
                if current < next_value:
                    answer -= current
                else:
                    answer += current
            else:
                answer += current
        return answer