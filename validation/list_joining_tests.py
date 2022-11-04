def validate(function):
    INPUTS = [
        ([-1,0,5],[5,2,5]),
        ([-1.1],[0]),
        ([0],[0]),
        ([1,4,5],[2,7,10,10,2,7,5.5]),
    ]
    EXP_OUTPUTS = [
        [-1,0,2,5],
        [-1.1,0],
        [0],
        [1,2,4,5,5.5,7,10],
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(*test_input)
        assert isinstance(func_output, bool), "Function did not return bool"
        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')