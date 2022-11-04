def validate(function):
    INPUTS = [
        ([(0.0, 0.0), (0.0, 2.0), (4.0, 2.0), (4.0, 0.0)], [(1.0, 0.0), (1.0, 2.0), (5.0, 2.0), (5.0, 0.0)]),
        ([(0.0, 0.0), (0.0, 2.0), (4.0, 2.0), (4.0, 0.0)], [(-4.0, 0.0), (0.5, 3.0), (-5.0, 2.0)]),
        ([(0.0, 0.0), (1.0, 1.0), (0.0, 2.0)], [(0.55, 0.5), (1.5, 0.5), (0.55, 0.0), (1.5, 0.0)]),
        ([(0.0, -1.0), (1.0, 1.0), (0.0, 2.0)], [(0.55, 0.5), (1.5, 0.5), (0.55, 0.0), (1.5, 0.0)]),
        ([(1.0, 0.3), (0.8, 0.1), (1.4, 0.2)], [(0.55, 0.5), (1.5, 0.5), (0.55, 0.0)]),
        ([(0.55, 0.5), (1.5, 0.5),(0.55, 0.0), (2, 0.0), (1.0, -1.0)], [(1, 0), (1.1, 0), (1.1, 0.1)])
    ]
    EXP_OUTPUTS = [
        True,
        False,
        False,
        True,
        True,
        True,
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(*test_input)
        assert isinstance(func_output, bool), "Function did not return a bool"
        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')