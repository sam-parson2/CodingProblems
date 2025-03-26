def isBalanced(s):
    stk = []
    lft = {'{', '[', '('}
    for k in s:
        if k in lft:
            stk.append(k)
            continue
        if not stk:
            return "NO"
        match [k, stk.pop()]:
            case ['}', '{']:
                continue
            case [')', '(']:
                continue
            case [']', '[']:
                continue
            case _: 
                return "NO"
    return "YES" if not stk else "NO"