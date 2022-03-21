import builtins


# def custom_str(value):
#     return bool(value)

# def mock_print(string):
#     return print (f'You are not allowed to print things here your string is {string}')


if __name__ == "__main__":
    my_number = 1
    print(my_number)
    print(type(my_number))
    # builtins.str = custom_str
    # old_print = print
    # builtins.print = mock_print
    casted_number = str(my_number)
    print(casted_number)
    print(type(casted_number))

