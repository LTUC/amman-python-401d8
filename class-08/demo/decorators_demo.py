# def say_hello(name):
#     return f"Hello {name}"

# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"

# def greet_bob(greeter_func):
#     return greeter_func("Bob")


# def parent():
#     print("Printing from the parent() function")

#     def first_child():
#         print("Printing from the first_child() function")

#     def second_child():
#         print("Printing from the second_child() function")

#     second_child()
#     first_child()



# def print_hello():
#     print("*****************")
#     print("Hello world")
#     print("*****************")



# def print_goodbye():
#     print("*****************")
#     print("Hello goodbye")
#     print("*****************")



# def print_weather():
#     print("*****************")
#     print("Weather is cold today and it is : 10 c!")
#     print("*****************")


def prettry_printer(func):
    def _wrapper(*args, **kwargs):
        print("*****************")
        func(*args, **kwargs)
        print("*****************")
    return _wrapper


@prettry_printer
def print_hello():    
    print(f"Hello world")


@prettry_printer
def print_greetings(name):    
    print(f"Hello {name}")


@prettry_printer
def print_goodbye():
    print("Hello goodbye")

@prettry_printer
def print_weather():
    print("Weather is cold today and it is : 10 c!")


if __name__ == "__main__":
    # print(greet_bob(say_hello))
    # print(greet_bob(be_awesome))
    # parent()
    print_hello()
    print_goodbye()
    print_weather()
    print_greetings("John")

    # a = None
    # b = "cat"
    # c = a or b




