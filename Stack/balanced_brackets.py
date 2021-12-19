from stack import Stack


def is_match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    else:
        return False


def is_balanced(parentheses):
    s = Stack()
    balanced = True
    i = 0

    while i < len(parentheses) and balanced:
        p = parentheses[i]
        if p in "([{":
            s.push(p)
        else:
            if s.is_empty():
                balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, p):
                    balanced = False
                    break
        i += 1

    if s.is_empty() and balanced:
        return True
    else:
        return False

# Test


print("String : (((({})))) Balanced or not?")
print(is_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_balanced("[][]"))
