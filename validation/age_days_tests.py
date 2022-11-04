def validate(function):
    INPUTS = [
        (2020,4,20),
        (2000,5,11),
        (420,4,20),
        (1970, 1, 1),
    
    ]
    EXP_OUTPUTS = [
        928,
        8212,
        585316,
        19300,
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(*test_input)
        assert isinstance(func_output, int), "Function did not return int"
        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')