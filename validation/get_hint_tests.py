def validate(function):
    INPUTS = [
        ("1807", "7810"),
        ("1123", "0111"),
        ("19053", "42149"),
        ("11059", "13149"),
        ("190565423763", "421542342449"),
    ]
    EXP_OUTPUTS = [
        "1G3Y",
        "1G1Y",
        "0G2Y",
        "2G1Y",
        "1G5Y",
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(*test_input)
        assert isinstance(func_output, str), "Function did not return string"
        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')