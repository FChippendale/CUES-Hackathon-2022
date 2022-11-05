def validate(function):
    INPUTS = [
        [1],
        [1, 2, 2, 2, 2, 3, 1],
        [2] * 100 + [3] * 100 + [1203],
        list(range(10**5)) * 2 + [10**5 + 1] + list(range(10**5 + 2, 2 * 10**5)) * 2
    ]
    EXP_OUTPUTS = [
        1,
        3,
        1203,
        10**5 + 1,
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