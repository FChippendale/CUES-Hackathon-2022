def validate(function):
    INPUTS = [
        [1, 2, 4],
        [5, 1, 3],
        [0, -2, 2],
        [160, 265, 139, 167, 20, 132, 272, 55, 125, 146, 244, 251, -8, -29, 118, 223, 209, -50, 279, 97, 34, 293, -15, 6, -22, 111, 41, 202, 195, 181, 83, 286, 90, 69, 104, 153, 62, -36, 13, 216, 258, 27, -43, -1, 48, 237, 230, 174, 188, 76],
        [160, 265, 139, 167, 20, 132, 272, 55, 125, 146, 244, 251, -8, -29, 118, 223, 209, -50, 279, 97, 34, 293, -15, 6, -22, 111, 41, 202, 195, 181, 83, 286, 90, 69, 104, 153, 62, -36, 13, 216, 258, 27, -43, -1, 48, 237, 230, 174, 188],

    ]
    EXP_OUTPUTS = [
        False,
        True,
        True,
        True,
        False,
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