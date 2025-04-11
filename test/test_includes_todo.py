from lib.includes_todo import includes_todo


#given input of a string #TODO  returns True

def test_returns_true_for_valid_string():
    assert includes_todo("#TODO") == True

#given input of a string without "#TODO" returns False

def test_returns_false_for_invalid_string():
    assert includes_todo("invalid") == False

def test_returns_false_for_empty_string():
    assert includes_todo("") == False

def test_returns_message_for_non_string_input():
    assert  includes_todo(1) == "Input needs to be a string"

def test_returns_true_for_valid_long_string():
    assert includes_todo("hello #TODO hello") == True