from linearstructures.PyStack import Stack


def toStr(n, base):
    my_stack = Stack()
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            my_stack.push(convertString[n])
        else:
            my_stack.push(convertString[n % base])
        n = n // base
    res = ''
    while not my_stack.is_empty():
        res = res + my_stack.pop()
    return res


print toStr(102, 8)
print toStr(10, 2)

