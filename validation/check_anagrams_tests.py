def validate(test_idx, is_anagram):
    CORRECT = [
        True, 
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False
    ]

    assert isinstance(test_idx, int)
    assert isinstance(is_anagram, bool)
    assert test_idx >= 0
    assert test_idx < len(CORRECT)

    return is_anagram is CORRECT[test_idx]