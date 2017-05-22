from bytesinsert import insert_code
import sys


def calculate():
    sum = 0
    for i in range(3):
        sum += i
    return sum


def print_locals():
    frame = sys._getframe(0)
    print("Local variables: ", frame.f_locals)


code_orig = calculate.__code__
code_to_insert = print_locals.__code__
success, result = insert_code(code_orig, code_to_insert, code_orig.co_firstlineno + 3)

if success:
    exec(result)
