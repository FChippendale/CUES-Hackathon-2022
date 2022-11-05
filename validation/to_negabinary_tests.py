def validate(function):
    INPUTS = [
        2,
        3,
        4,
        18,
        -15,
        -3,
        0,
        21230123,
    ]
    EXP_OUTPUTS = [
        "110",
        "111",
        "100",
        "10110",
        "110001",
        "1101",
        "0",
        "1010001000011011001111111",
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(test_input)
        assert isinstance(func_output, str), "Function did not return a str"

        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')