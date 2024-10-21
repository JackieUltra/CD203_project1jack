from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function 
    """
    # Create instance of FastaParser
    fasta_parser = FastaParser('data/test.fa')
    # Create instance of FastqParser
    fastq_parser = FastqParser('data/test.fq')
        
    # For each record of FastaParser, Transcribe the sequence
    print("Transcribed Fasta Sequences:")
     # Iterate over individual record in the FASTA file
    for header, sequence in fasta_parser:
        transcribed_seq = transcribe(sequence)
        # print it to console
        print(f"{header}\n{transcribed_seq}")
       
    # For each record of FastqParser, Transcribe the sequence
    print("Transcribed Fastq Sequences:")
    # Iterate over individual record in the FASTQ file
    for header, sequence, _ in fastq_parser:
        transcribed_seq = transcribe(sequence)
        # print it to console
        print(f"{header}\n{transcribed_seq}")


    # For each record of FastaParser, Reverse Transcribe the sequence
    print("Reverse Transcribed Fasta Sequences:")
     # Iterate over individual record in the FASTA file
    for header, sequence in fasta_parser:
        reverse_transcribed_seq = reverse_transcribe(sequence)
        # print to console
        print(f"{header}\n{reverse_transcribed_seq}")
       
    # For each record of FastqParser, Reverse Transcribe the sequence and print it to console
    print("Reverse Transcribed Fastq Sequences:")
     # Iterate over individual record in the FASTQ file
    for header, sequence, _ in fastq_parser:
        reverse_transcribed_seq = reverse_transcribe(sequence)
        # print to console
        print(f"{header}\n{reverse_transcribed_seq}")


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
