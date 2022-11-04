def validate(function):
    INPUTS = [
        [3,2,1,0,4],
        [3,2,1,1,4],
        [1,0],
        [0,0],
        [1,1,1,1,1,1,1],
        [1,1,1,2,0,1,1],
        [1,1,1,2,4,1,0],
        [1,1,0,2,0,0,1],
    ]
    EXP_OUTPUTS = [
        False,
        True,
        True,
        False,
        True,
        True,
        True,
        False,
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(test_input)
        assert isinstance(func_output, bool), "Function did not return bool"
        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')