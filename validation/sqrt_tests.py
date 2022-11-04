import math

def validate(function):
    INPUTS = [
        0, 1, 100, 13, 120,
        1000000, 1<<30, (1<<29)+1,
    ]
    EXP_OUTPUTS = [int(math.sqrt(test)) for test in INPUTS]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(test_input)
        assert isinstance(func_output, int), "Function did not return a int"
        if i < 5:
            level = "Easy"
        else:
            level = "Medium"

        if func_output == exp_output:
            print(f"{level} Test Case {i+1} Passed")
        else:
            print(f"{level} Test Case {i+1} Failed")