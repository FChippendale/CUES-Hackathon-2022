def validate(function):
    INPUTS = [
        "hackathon",
        "cues",
        "aabb",
        "abcdefghiabcdefgh",
    ]
    EXP_OUTPUTS = [
        2,
        0,
        -1,
        8,
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