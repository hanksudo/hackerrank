def isBalanced(s):
    if not s:
        return "NO"

    brackets_pairs = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    stack = []
    for c in s:
        if c in brackets_pairs.keys():
            stack.append(c)
        elif c in brackets_pairs.values():
            if not stack or brackets_pairs[stack.pop()] != c:
                return "NO"
    if stack:
        return "NO"

    return "YES"
