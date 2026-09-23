class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketKey = {")" : "(", "]" : "[", "}" : "{"}

        for char in s:
            if char in bracketKey:
                if stack and stack[-1] == bracketKey[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False 
