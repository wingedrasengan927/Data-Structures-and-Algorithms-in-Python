
# let's create a linter to see stacks in action

# first let's define our errors
class NoClosingBrace(Exception):
    '''This is when there is an opening brace that doesn’t have a corresponding closing brace'''
    pass

class NoOpeningBrace(Exception):
    '''This is when there is a closing brace that was never preceded by a corresponding opening brace'''
    pass

class DissimilarBrace(Exception):
    '''This is when a closing brace is not the same type of brace as the immediately preceding opening brace,'''
    pass



def isBracketOpen(char):
    if char in ["(", "{", "["]:
        return True
    return False

def isBracketClose(char):
    if char in [")", "}", "]"]:
        return True
    return False

def linter(string):
    # We use a simple array to serve as our stack
    data=[]
    # let's also create a mapping between open and close brackets
    mapping = {")":"(", "}":"{", "]":"["}
    # We start a loop which reads each character in our text
    try:
        for i in string:
            # If the character is an opening brace, we push it onto the stack:
            if isBracketOpen(i):
                data.append(i)
            # if closing brace occurs, compare with the last opening brace in our stack using the mapping dictionary
            if isBracketClose(i):
                # Let's check if our stack contains any elements.
                # if None, then the closing brackets have occured first and is an error
                if data:
                    # Compare with the last opening brace in our stack array

                    # if the closing brace is equal to the last opening brace in our stack, then no error
                    if mapping[i]==data[-1]:
                        data.pop()
                    # else, there is DissimilarBrace error
                    else:
                        raise DissimilarBrace
                # if there is no data then the closing braces must have preceded the opening braces
                else:
                    raise NoOpeningBrace

        # if we make to the end of line and still there is data on the stack
        # then it's an error
        # most probably, opening base may not have a corresponding closing brace
        if data:
            raise NoClosingBrace
        else:
            print("Everything is fine. Very Good.")
    except NoClosingBrace:
        print("Hello, seems like an opening brace doesn’t have a corresponding closing brace. Please check")
    except NoOpeningBrace:
        print("Hello, seems like a closing brace has not been preceded by a corresponding opening base. Please Check")
    except DissimilarBrace:
        print("Hello, seems like a closing brace does not match to the corresponding opening base. Please Check")


str1 = "(var x = {y: [1, 2, 3]})"
linter(str1)