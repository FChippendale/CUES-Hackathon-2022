def validate(function):
    INPUTS = [
        0b111100000,
        0b1,
        0b0,
        0b101,
        1<<200,
    ]
    EXP_OUTPUTS = [
        4, 
        1, 
        0, 
        2, 
        1,
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(test_input)
        assert isinstance(func_output, int), "Function did not return a int"

        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')