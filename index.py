from Bio.Seq import Seq # pip install biopython
from Bio import SeqIO

dna = Seq("ATGCAGTACAGACGTGATAG")
print(dna)
print(dna.complement())
print(dna.reverse_complement())

for sequence in SeqIO.parse("globin.fasta", "fasta"):
    print(sequence.id)
    print(repr(sequence.seq))
    print(len(sequence))