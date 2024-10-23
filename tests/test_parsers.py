# write tests for parsers
import io
import os
import itertools

from seqparser import (
        FastaParser,
        FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

    # Test 1  
def test_FastaParser():
    """
    Unit test for FastaParser class.
    """
    import os
    import itertools
    
    # Expected records (header, sequence) in test.fa
    expected_records_test_fa = [
        (">seq0", "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA"),
        (">seq1", "TCCGCCCGCTGTGCTGACGAGACTAGCAGGGAAATAAATAGAGGGTTTAGTTATACTCAGTAGGCAGTTCGATGGCTTATATCTAACTTCTTATTCCGAT"),
        (">seq2", "TGTAGAGGCATTATTAGAGTTTCGCCACAACGGGGGCCTGCTGATCAAATCAGAATTCGTACAATCGGTTCGGGAGACACGGCTCTAAAGATACCGCTAG")
    ]


def test_FastqParser():
    """
    Write your unit test for your FastqParserclass here. 
    You should generate an instance of your FastqParser class and assert that it properly reads in the example Fastq File.
    """
    # List of tuples (header, sequence, score) in test.fq
    expected_records_test_fq = [
        ("@seq0", "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG",
         "*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7\"94(>7='(!5\"2/!%\"4#32="),
        ("@seq1", "CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGGCAAGCAGACCCATATCGTCCTGCTGGCAACGCTATCCGGGTGCGAGTAAATCGAAACCTCG",
         "'(<#/0$5&!$+,:=%7=50--1;'(-7;0>=$(05*9,,:%0!<),%646<8#%\".\"-'*-0:.+*&$5!'8)(%3*+9/&/%=363*,6$20($97,\""),
        ("@seq2", "GATAAACTTCTATCACGAATACTGCGGGACCATGCAGTTGTCCCTCACCTCGATAGTTCAGGTCTTTTGGTTCTGAGCGATATTGGGCGCGTCACCACTG",
         "1,758$,:7654/7<0%5/12%-3>-2.>$$443-,'9,5$;\"\"%7**)-'%:**&;<35(!<1'.5>51)1%:9>4=(&+3$2!-.8!>=+1$:,*&9!")
    ]

