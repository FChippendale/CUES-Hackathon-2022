def validate(function):
    INPUTS = [
        [1, 3, 2, 4, 3],
        [1,8,6,2,5,4,8,3,7],
        [1, 1],
        [88, 84, 86, 27, 51, 17, 77, 83, 32, 37, 97, 20, 4, 50, 97, 54, 76, 76, 63, 66, 72, 73, 56, 73, 47, 7, 24, 98, 16, 36, 77, 21, 32, 15, 31, 44, 86, 78, 2, 80, 63, 67, 35, 76, 19, 30, 56, 44, 69, 56, 65, 22, 7, 96, 32, 5, 42, 47, 34, 96, 69, 66, 73, 92, 84, 25, 95, 52, 36, 63, 63, 58, 89, 54, 56, 43, 31, 32, 12, 28, 81, 56, 91, 2, 59, 78, 37, 42, 66, 73, 23, 80, 66, 17, 41, 58, 26, 28, 29, 77],
        [92, 3, 22, 60, 91, 32, 58, 4, 49, 1, 12, 43, 36, 79, 1, 57, 86, 84, 65, 80, 71, 44, 61, 77, 55, 83, 88, 60, 18, 72, 79, 98, 72, 11, 3, 16, 69, 79, 54, 10, 99, 94, 24, 36, 98, 19, 62, 57, 59, 81, 2, 10, 33, 22, 70, 84, 58, 16, 74, 82, 8, 41, 71, 73, 3, 27, 99, 70, 63, 94, 1, 75, 38, 15, 78, 10, 49, 41, 3, 89, 86, 58, 87, 29, 55, 56, 17, 10, 31, 17, 37, 66, 63, 31, 48, 95, 62, 74, 22, 73],

    ]
    EXP_OUTPUTS = [
        9,
        49,
        1,
        7623,
        8740,
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