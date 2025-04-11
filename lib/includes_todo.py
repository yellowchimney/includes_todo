def includes_todo(string):
    if type(string) != str:
        return "Input needs to be a string"
    if "#TODO" in string:
        return True
    else:
        return False

"""function takes a string and returns True if 
the string contains substring #TODO"""