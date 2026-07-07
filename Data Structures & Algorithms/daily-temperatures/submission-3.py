class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        len_temperatures = len(temperatures)
        res = [0] * len_temperatures
        stack = []

        for i in range(len_temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res