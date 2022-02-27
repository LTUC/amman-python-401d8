from datetime import datetime


def text_fromatter(username, age):
    '''
        text formatter is a function that is responsible for formatting text

        Input: 
                username: String
                age: integer
        
        Output: returns formatted string with the name and the age
    '''
    # Way 1 : f strings
    print( f'Hello my name is {username} and Im {age} years old!')

    #Way2 : Concatination
    # return "Hello my name is " + name + " and Im " + str(age) + " years old!"

    #Way3: Format method
    # return "Hello my name is {} and Im {} years old!".format(name, age)

    #Way4: Percentage sign

    # return "Hello my name is %s and Im %d years old!"%(name, age)

#print(help(text_fromatter))
def time_printer():
    return datetime.now()
# We want to excute this file when it is called
if __name__ == "__main__":
    print(text_fromatter("Ahmad", 25))
    print("Amman-Python-401d8")