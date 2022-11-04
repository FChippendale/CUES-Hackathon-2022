def validate(function):
    func_output = function()
    assert isinstance(func_output, str), "Function did not return string"
    assert func_output == "Hello World", f'Expected "Hello World", received {func_output}'
    print("Test Case passed")