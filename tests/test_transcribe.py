# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Unit test for the transcribe function
    """
    # Test Case 1 RNA to DNA
    assert transcribe("ATCG") == "UAGC", "TC1 fail, there was a transcribe error"
    # Test Case 2 Return an empty string
    assert transcribe("") == "", "TC2 fail, empty string unable to return a empty string"
    # Test Case 3 Lowercase input
    assert transcribe("atcg") == "UAGC", "TC3 fail, lowercase input should return"
    # Test Case 4 Mixed case input
    assert transcribe("ATcg") == "UAGC", "TC4 fail, mixed case input should return"
    # Test Case 5 Input invalid characters
    try:
        transcribe("XATCG")
    except ValueError as e:
        assert str(e) == "Input invalid character. Only A, T, C, G ", "TC5 fail, invalid characters should raise a ValueError"
    # Test Case 6: Long sequence
    assert transcribe("ATCG" * 1000) == "UAGC" * 1000, "TC6 fail, long sequence failed"
    # Test Case 7: Repetitive sequence
    assert transcribe("AAAA") == "UUUU", "TC7 fail, repetitive sequence failed"
    # yay!
    pass


def test_reverse_transcribe():
    """
    Unit test for the reverse transcribe function
    """
    # Test Case 1 DNA to RNA
    assert reverse_transcribe("T") == "U", "TC1 fail, DNA was not converted to RNA"
    # Test Case 2 Reverse
    assert reverse_transcribe("ATCG") == "GCUA", "TC2, fail, there was no reversal of the sequence"
    # Test Case 3 Return and empty string
    assert reverse_transcribe("") == "", "TC3 fail, empty string unable to return a empty string"
    # Test Case 4 Lowercase input
    assert reverse_transcribe("atcg") == "GCUA", "TC4 fail, lowercase input should return"
    # Test Case 5 Mixed case input
    assert reverse_transcribe("Atcg") == "GCUA", "TC5 fail, mixed case input should return"
    # Test Case 6 Input invalid characters
    try:
        reverse_transcribe("XATCG")
    except ValueError as e:
        assert str(e) == "Input invalid character. Only A, T, C, G", "TC6 fail, invalid characters should raise a ValueError"
    # Test Case 7: Long sequence
    assert reverse_transcribe("ATCG" * 1000) == "GCUA" * 1000, "TC7 fail, long sequence failed"
    # Test Case 8: Repetitive sequence
    assert reverse_transcribe("AAAA") == "UUUU", "TC8 fail, repetitive sequence failed"
    # yay!
    pass
