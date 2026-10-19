class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack, res = [], 0
        for opr in operations:
            if len(stack) > 1 and opr == "+":
                res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif len(stack) > 0 and opr == "D":
                res += (2 * stack[-1])
                stack.append(2 * stack[-1])
            elif len(stack) > 0 and opr == "C":
                res -= stack.pop()
            else:
                res += int(opr)
                stack.append(int(opr))
        return res