def validate(function):
    EXP_OUTPUT = -5982218138347061190
    
    print(f"Running Testcase")
    func_output = function()
    assert isinstance(func_output, str), "Function did not return a string"

    if hash(func_output) == EXP_OUTPUT:
        print("Test Case Passed")
    else:
        print('Test Case Failed')