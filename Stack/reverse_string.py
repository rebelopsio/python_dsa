from stack import Stack


def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        s.push(input_str[i])
    t = ""
    while not stack.is_empty():
        t += s.pop()
    return t


s = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(s, input_str))