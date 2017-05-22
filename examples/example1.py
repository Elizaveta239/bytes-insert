from bytesinsert import insert_code


def hello():
    print("1")
    print("3")


def new_code():
    print("2")


code_orig = hello.__code__
code_to_insert = new_code.__code__
success, result = insert_code(code_orig, code_to_insert, 6)
if success:
    exec(result)
