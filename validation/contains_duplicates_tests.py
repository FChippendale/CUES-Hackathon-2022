def validate(function):
    INPUTS = [
        [1, 2, 3, 4],
        [1, 2, 3, 1],
        [1, 1, 2, 2, 5, 3],
        list(range(0, 100)),
        list(range(0, 1000000)),
        list(range(0, 1000000)) + [69]
    ]
    EXP_OUTPUTS = [
        False,
        True,
        True,
        False,
        False,
        True,
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(test_input)
        assert isinstance(func_output, bool), "Function did not return a bool"

        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')