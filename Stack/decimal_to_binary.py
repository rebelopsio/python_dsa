from stack import Stack


def decimal_to_binary(dec):
    if dec == 0:
        return 0
    s = Stack()
    binans = ""
    while dec != 0:
        if (dec % 2) != 0:
            s.push("1")
        else:
            s.push("0")
        dec = dec // 2
    while not s.is_empty():
        binans += s.pop()
    return binans


print(decimal_to_binary(242))