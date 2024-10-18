# DNA -> RNA Transcription
# DNA -> RNA Transcription

def transcribe(seq: str) -> str:
    """
    Transcribes DNA to RNA by generating the complement sequence with T -> U replacement
    """
    # Dict of complement base pairing
    complement = {'A' : 'U', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
    # Generate our RNA complement seq
    rna_seq = ''.join(complement[base] for base in seq)
    
    return rna_seq


def reverse_transcribe(seq: str) -> str:
    """
    Transcribes DNA to RNA then reverses the strand
    """
    # Transcribe DNA seq into RNA seq
    rna_seq = seq.replace('T', 'U')
    # Reverse the RNA seq
    reversed_rna_seq = rna_seq[::-1]
    
    return reversed_rna_seq