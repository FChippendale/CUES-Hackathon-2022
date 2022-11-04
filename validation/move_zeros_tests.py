def validate(function):
    INPUTS = [
        [0, 5, 0, 3, 12], 
        [0, 0, 0, 0], 
        [1, 2, 3], 
        [0], 
        [-1, 0, 0, 0, 2, 0],
    ]
    EXP_OUTPUTS = [
        [5, 3, 12, 0, 0],
        [0, 0, 0, 0],
        [1, 2, 3],
        [0],
        [-1, 2, 0, 0, 0, 0],
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(test_input)
        assert isinstance(func_output, list), "Function did not return a list"

        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')