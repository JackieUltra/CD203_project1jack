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

def test_FastaParser():
    fa_parser = FastaParser('data/test.fa')
    fa_expected_records = [
        ('>seq0', 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'),
        ('>seq1', 'TCCGCCCGCTGTGCTGACGAGACTAGCAGGGAAATAAATAGAGGGTTTAGTTATACTCAGTAGGCAGTTCGATGGCTTATATCTAACTTCTTATTCCGAT'),
        ('>seq2', 'TGTAGAGGCATTATTAGAGTTTCGCCACAACGGGGGCCTGCTGATCAAATCAGAATTCGTACAATCGGTTCGGGAGACACGGCTCTAAAGATACCGCTAG')
    ]

    # Loop through first three tuples
    for i, record in enumerate(fa_parser):
        # Check if the head '>seq' in the head of tuple
        if '>seq' not in record[0]:
            assert False

        # Ensure valid nucleotides A,C,G,T in the seq part of tuple
        for nucleotide in record[1]:
            if nucleotide not in 'ACGT':
                assert False
        
        # Check if the record matches the expected record
        if i < 3:
            assert record == fa_expected_records[i]
        
        if i == 2:
            break

    # All g homie
    assert True

def test_FastqParser():
    fq_parser = FastqParser('data/test.fq')
    fq_expected_records = [
        ('@seq0', 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG', '*540($=*,=.062565,2>\'487\')!:&&6=,6,*7>:&132&83*8(58&59>\'8!;28<94,0*;*.94**:9+7"94(>7=\'(!5"2/!%"4#32='),
        ('@seq1', 'CCCCGGACGACTGATCCCGATAGAGCTCACTCTTCGAGGCAAGCAGACCCATATCGTCCTGCTGGCAACGCTATCCGGGTGCGAGTAAATCGAAACCTCG', '\'(<#/0$5&!$+,:=%7=50--1;\'(-7;0>=$(05*9,,:%0!<),%646<8#%"."-\'*-0:.+*&$5!\'8)(%3*+9/&/%=363*,6$20($97,"'),
        ('@seq2', 'GATAAACTTCTATCACGAATACTGCGGGACCATGCAGTTGTCCCTCACCTCGATAGTTCAGGTCTTTTGGTTCTGAGCGATATTGGGCGCGTCACCACTG', '1,758$,:7654/7<0%5/12%-3>-2.>$$443-,\'9,5$;""%7**)-\'%:**&;<35(!<1\'.5>51)1%:9>4=(&+3$2!-.8!>=+1$:,*&9!')
    ]

    # Loop through first three tuples
    for i, record in enumerate(fq_parser):
        # Check if the head '@seq' in the head of tuple
        if '@seq' not in record[0]:
            assert False

        # Ensure valid nucleotides A,C,G,T in the seq part of tuple
        for nucleotide in record[1]:
            if nucleotide not in 'ACGT':
                assert False

        # Check if the record matches the expected record
        if i < 3:
            assert record == fq_expected_records[i]

        if i == 2:
            break

    # All g homie
    assert True
