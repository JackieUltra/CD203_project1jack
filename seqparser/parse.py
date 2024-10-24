import io
from typing import Tuple, Union


class Parser:
    """
    Base Class for Parsing Algorithms
    """
    def __init__(self, filename: str):
        """
        Initialization to be shared by all inherited classes.
        """
        
        self.filename = filename

    def get_record(self, f_obj: io.TextIOWrapper) -> Union[Tuple[str, str], Tuple[str, str, str]]:
        """
        Returns a sequencing record that will either be a tuple of two strings (header, sequence)
        or a tuple of three strings (header, sequence, quality). 

        """
        return self._get_record(f_obj)

    def __iter__(self):
        """
        This is an overriding of the Base Class Iterable function. Here, for the purposes of this
        assignment, we are defining how this class and all inherited classes interact with loops.
        """
        with open(self.filename, "r") as f_obj:

            while True:
                rec = self.get_record(f_obj)
                # Stop the loop at the end of the file
                if rec is None: 
                    break
                yield rec

    def _get_record(self, f_obj: io.TextIOWrapper) -> Union[Tuple[str, str], Tuple[str, str, str]]:
        """
        a method to be overridden by inherited classes.
        """
        raise NotImplementedError(
                """
                This function is not meant to be called by the Parser Class.
                It is expected to be overridden by `FastaParser` and `FastqParser`
                """)

class FastaParser(Parser):
    """
    Fasta Specific Parsing
    """
    
    def _get_record(self, f_obj: io.TextIOWrapper) -> Union[Tuple[str, str], None]:
        """
        Returns the next fasta record as a 2-tuple of (head, seq)
        """
        # create head str
        head = f_obj.readline().rstrip()
        # End of file should not be included as empty tuple
        if not head:  
            return None
        # create seq str
        seq = f_obj.readline().rstrip()

        # file format error
        # find >seq
        if '>seq' not in head:
            raise ValueError("expect >seq in head")
            
        # return the tuple
        return (head, seq)


class FastqParser(Parser):
    """
    Fastq Specific Parsing 
    """
    def _get_record(self, f_obj: io.TextIOWrapper) -> Tuple[str, str, str]:
        """
        Returns the next fastq record as a 3-tuple of (header, sequence, quality)
        """
        # create head str
        head = f_obj.readline().rstrip()
        # End of file should not be included as empty tuple
        if not head: 
            return None
        # create seq str
        seq = f_obj.readline().rstrip()
        # file format error
        # find +
        if not f_obj.readline().startswith('+'):
            raise ValueError("expect + between seq and qual")
        # create qual str
        qual = f_obj.readline().rstrip()
 
        # file format error
        # find @seq
        if '@seq' not in head and head != "":
            return ValueError("expect @seq in head")

        # return the tuple
        return (head, seq, qual)