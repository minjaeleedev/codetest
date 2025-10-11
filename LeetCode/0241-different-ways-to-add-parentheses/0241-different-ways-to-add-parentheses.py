class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        
        result = []
        op = set('+-*')
        for i, c in enumerate(expression):
            if c in op:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                
                for l in left:
                    for r in right:
                        if c == '+':
                            result.append(l + r)
                        elif c == '-':
                            result.append(l - r)
                        else:
                            result.append(l * r)

        return result
