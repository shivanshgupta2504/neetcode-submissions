class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for opr in operations:
            if len(stack) > 1 and opr == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2)
                stack.append(num1)
                stack.append(num1 + num2)
            elif len(stack) > 0 and opr == "D":
                num = stack.pop()
                stack.append(num)
                stack.append(2 * num)
            elif len(stack) > 0 and opr == "C":
                stack.pop()
            else:
                stack.append(int(opr))
        return sum(stack)