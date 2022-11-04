import numpy as np

def validate(function):
    INPUTS = [
        [5, 4, 7, 9],
        [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        [143, 109, 48, 170, 123, 27, 135, 199, 130, 11, 94, 68, 156, 55, 167, 15, 47, 47, 194, 95, 32, 198, 137, 159, 128, 10, 145, 96, 1, 37, 35, 174, 113, 191, 75, 175, 31, 192, 104, 45, 197, 104, 93, 191, 182, 133, 189, 164, 105, 95],
        list(range(100000))[::-1], 
        list(np.random.randint(0, 200, 100000)),
    ]
    EXP_OUTPUTS = [sorted(test) for test in INPUTS]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(test_input)
        assert isinstance(func_output, list), "Function did not return a list"
        if i < 3:
            level = "Easy"
        else:
            level = "Medium"

        if func_output == exp_output:
            print(f"{level} Test Case {i+1} Passed")
        else:
            print(f"{level} Test Case {i+1} Failed")