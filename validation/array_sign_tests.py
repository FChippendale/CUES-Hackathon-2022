def validate(function):
    INPUTS = [
        [-1,-2,-3,-4,3,2,1],
        [1,5,0,2,-3],
        [-1,1,-1,1,-1],
        [1, -1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, -1, 1],
        [-1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 0, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1],
        [-1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000],
    ]
    EXP_OUTPUTS = [
        1,
        0,
        -1,
        -1,
        0,
        1
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(test_input)
        assert isinstance(func_output, int), "Function did not return int"
        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')