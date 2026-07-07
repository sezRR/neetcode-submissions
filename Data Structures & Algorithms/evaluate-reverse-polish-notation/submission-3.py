class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for token in tokens:
            if token.lstrip("+-").isdigit():
                operands.append(int(token))
            else:
                operand1 = operands.pop()
                operand2 = operands.pop()
                if token == "+":
                    operands.append(operand2 + operand1)
                elif token == "-":
                    operands.append(operand2 - operand1)
                elif token == "*":
                    operands.append(operand2 * operand1)
                elif token == "/":
                    operands.append(int(operand2 / operand1))
        return operands.pop()
            