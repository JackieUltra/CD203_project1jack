# write tests for parsers

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

def test_FastqParser():
    
    fq_parser = FastqParser("data/test.fq")
    # Loop through all tuples
    for record in fq_parser:
        # Check if the head '@seq' in the head of tuple
        if "@seq" not in record[0]:
            # If the head does not contain @seq fail
            assert False
        # Ensure valid nucleotides A,C,G,T in the seq part of tuple
        for nucleotide in record[1]:
            if nucleotide not in 'ACGT':
                # Invalid characters found
                assert False
    # All g homie       
    assert True
    

def test_FastaParser():
    
    fa_parser = FastaParser("data/test.fa")
    # Loop through all tuples
    for record in fa_parser:
        # Check if the head '>seq' in the head of tuple
        if ">seq" not in record[0]:
            # If the head does not contain >seq fail
            assert False
        # Ensure valid nucleotides A,C,G,T in the seq part of tuple
        for nucleotide in record[1]:
            if nucleotide not in 'ACGT':
                # Invalid characters found
                assert False
    # All g homie
    assert True