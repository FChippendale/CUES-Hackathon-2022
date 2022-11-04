def validate(function):
    INPUTS = [
        [1, 4, 2],
        [1, 3],
        [1, 4, 2, 5, 3],
        [5, 2, 0, 8, 8, 5, 2, 2, 4, 1, 4, 6, 1, 1, 6, 5, 3, 6, 4, 2],
        [3, 19, 41, 16,  3, 23, 32,  6, 18, 43,  1,  3,  1, 44, 41, 27, 45, 3, 11, 40, 45, 22, 37, 37, 21, 45, 18, 18,  2,  7, 46, 23, 21,  3]
    ]
    EXP_OUTPUTS = [
        14,
        4,
        58,
        2853,
        86304,
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(test_input)
        assert isinstance(func_output, int), "Function did not return an int"
        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')