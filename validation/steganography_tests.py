import hashlib

def validate(function):
    EXP_OUTPUT = "a6d72baa3db900b03e70df880e503e9164013b4d9a470853edc115776323a098"
    
    print(f"Running Testcase")
    func_output = function()
    assert isinstance(func_output, str), "Function did not return a string"

    if hashlib.sha256(func_output.encode("utf-8")).hexdigest() == EXP_OUTPUT:
        print("Test Case Passed")
    else:
        print('Test Case Failed')