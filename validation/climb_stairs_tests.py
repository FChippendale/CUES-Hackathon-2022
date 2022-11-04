def validate(function):
    INPUTS = [
        3,
        5,
        10,
        100,
        300,
    ]
    EXP_OUTPUTS = [
        3,
        8,
        89,
        573147844013817084101,
        359579325206583560961765665172189099052367214309267232255589801,
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(test_input)
        assert isinstance(func_output, int), "Function did not return a int"
        if i < 3:
            level = "Easy"
        else:
            level = "Medium"

        if func_output == exp_output:
            print(f"{level} Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')