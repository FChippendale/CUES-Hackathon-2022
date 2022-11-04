def validate(function):
    INPUTS = [
        "This Is A Test",
        "ThIs Is AlSo A tEsT",
        "Bryan had made peace with himself and felt comfortable with the choices he made. This had made all the difference in the world. Being alone no longer bothered him and this was essential since there was a good chance he might spend the rest of his life alone in a cell.",
        
    ]
    EXP_OUTPUTS = [
        "this is a test",
        "this is also a test",
        "bryan had made peace with himself and felt comfortable with the choices he made. this had made all the difference in the world. being alone no longer bothered him and this was essential since there was a good chance he might spend the rest of his life alone in a cell.",
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(test_input)
        assert isinstance(func_output, str), "Function did not return string"
        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')