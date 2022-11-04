def validate(function):
    INPUTS = [
        "dcba",
        "aeioubcdfghlmnpqrstvz",
        "xfyRNOz39UwFFc9EAvDScMEy9S6AbB1MtqeVI4RtNQKhWw5NC80LAu6DrJ3xag8F5F1HQXTp3Im5x3VkTcEH8kjM4e8DTh80axEj",
        "LiqhwGJvw5iWSs8uZFdynYzEFpA9yAt7UhL8nt0c6GgbPcdNnXrQt2XibMPcpmVNYEK4297EKRPVwU8REFOzh3JYoWgCiZi84eXb6tWZvlvmpkBqQap6efx46UWFeKXAWIv70Xum8G0SbWQNdhvyCEeINdRGkdNOAqrEFcKMarT9WYqJxl3kM4O78TQCWR8a85Rke8bLX0isoNa5X9XTOq8oj5PWMJdZCFHE1JryOMQI395MQzZn8rpsoMGyWxapbWNh81BPgsSexQ1bbd4uQamtTSEpxFxxnYfPDGXUHqZGbvKWWn3hWxDRnvZ0tSjukMEzgC5kyAo0AMRhxcZOKfHbr3ZqR2nHStOO3eyH59v3mHsWc37d5siSUOD5nGSH2frNyFi1a1MxuFkmsJJschqNk1b5UCPdwn30sA3iKBINUpeU2PJZ8akeTOWBus9AzHr0Uy5p2qCANdukoTkt1TPDfrQwhj8KXZRt6oOLeqGSAOiaEpi10kQ2Fy0SCARMOJgHy5VQx7kExkJFafhtABoFsc2NetfYCNkXsuotwRhscNNwi8IrGDy4YpGmoYzHVTWUOqhPT6KOdb3NYK8BOkfawWoVjXdtRgU24goJOEimEydugFGAFbqvdE2AX90NHZVJrd7vfyxiWwCXNEbndBHLfVprIZjIpcgeKfN20uuwQ4ZcI8yBwRyAH2Wlcjg1Ky3X1cUJUGUyOnlJxbigfvkl72ouBedf8eJ27dtdMYqzEN3IjY66r8MjlkGpb7QDFbABHJsePtQ9TGdosrUkx6Cxn1yhCQk46L1dO4a74WmPzImZWT8fWjwJUe9nRDoHgUzf2tFOQQ7EniwRfzhyAawYXVUpePD5Dua8gLXNQbO3E3GixdFDgqUCBswP7altBVHDSTAuo4atHpYYs0wAbOCSA8knI8QDuRTQiB18ik9U8NzPjHGU9S52oDiUZsRL9NVfXVioZBTjQTwMRW481uIf8jskJwjNkjMESBAH",
    ]
    EXP_OUTPUTS = [
        "abcd",
        "zvtsrqpnmlhgfdcbuoiea",
        "jExa08hTD8e4Mjk8HEcTkV3x5mI3pTXQH1F5F8gax3JrD6uAL08CN5wWhKQNtR4IVeqtM1BbA6S9yEMcSDvAE9cFFwU93zONRyfx",
        "HABSEMjkNjwJksj8fIu184WRMwTQjTBZoiVXfVN9LRsZUiDo25S9UGHjPzN8U9ki81BiQTRuDQ8Ink8ASCObAw0sYYpHta4ouATSDHVBtla7PwsBCUqgDFdxiG3E3ObQNXLg8auD5DPepUVXYwaAyhzfRwinE7QQOFt2fzUgHoDRn9eUJwjWf8TWZmIzPmW47a4Od1L64kQChy1nxC6xkUrsodGT9QtPesJHBAbFDQ7bpGkljM8r66YjI3NEzqYMdtd72Je8fdeBuo27lkvfgibxJlnOyUGUJUc1X3yK1gjclW2HAyRwBy8IcZ4Qwuu02NfKegcpIjZIrpVfLHBdnbENXCwWixyfv7drJVZHN09XA2EdvqbFAGFgudyEmiEOJog42UgRtdXjVoWwafkOB8KYN3bdOK6TPhqOUWTVHzYomGpY4yDGrI8iwNNcshRwtousXkNCYfteN2csFoBAthfaFJkxEk7xQV5yHgJOMRACS0yF2Qk01ipEaiOASGqeLOo6tRZXK8jhwQrfDPT1tkTokudNACq2p5yU0rHzA9suBWOTeka8ZJP2UepUNIBKi3As03nwdPCU5b1kNqhcsJJsmkFuxM1a1iFyNrf2HSGn5DOUSis5d73cWsHm3v95Hye3OOtSHn2RqZ3rbHfKOZcxhRMA0oAyk5CgzEMkujSt0ZvnRDxWh3nWWKvbGZqHUXGDPfYnxxFxpESTtmaQu4dbb1QxeSsgPB18hNWbpaxWyGMospr8nZzQM593IQMOyrJ1EHFCZdJMWP5jo8qOTX9X5aNosi0XLb8ekR58a8RWCQT87O4Mk3lxJqYW9TraMKcFErqAONdkGRdNIeECyvhdNQWbS0G8muX07vIWAXKeFWU64xfe6paQqBkpmvlvZWt6bXe48iZiCgWoYJ3hzOFER8UwVPRKE7924KEYNVmpcPMbiX2tQrXnNdcPbgG6c0tn8LhU7tAy9ApFEzYnydFZu8sSWi5wvJGwhqiL"
    ]
    
    print(f"Running {len(INPUTS)} Testcases")
    for i, (test_input, exp_output) in enumerate(zip(INPUTS, EXP_OUTPUTS)):
        func_output = function(test_input)
        assert isinstance(func_output, str), "Function did not return a string"

        if func_output == exp_output:
            print(f"Test Case {i+1} Passed")
        else:
            print(f'Given Input "{test_input}",')
            print(f'Expected "{exp_output}",')
            print(f'Received {func_output}')