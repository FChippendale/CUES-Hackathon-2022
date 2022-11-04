def validate(function):
    INPUTS = [
        "Engineering Society",
        "Hello world this is a long sentence",
        "Double Trouble ",
        "A suit of armor provides excellent sun protection on hot days",
        "his seven layer cake only had six layers"
    ]
    EXP_OUTPUTS = [
        "gnireenignE yteicoS",
        "olleH dlrow siht si a gnol ecnetnes",
        "elbuoD elbuorT",
        "A tius fo romra sedivorp tnellecxe nus noitcetorp no toh syad",
        "sih neves reyal ekac ylno dah xis sreyal",
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