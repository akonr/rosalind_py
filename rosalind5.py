from Bio import SeqIO
from Bio.SeqUtils import GC
import collections

# rosalind_vaja = open("resitev_rosalind_gc.txt", "w")
# for seq_record in SeqIO.parse("probaGC.txt", "fasta"):
#     print(seq_record.id + "\n" + str(GC(repr(seq_record)))
#                         + "\n")
#
# rosalind_vaja.close()


def read_genome(filename):
    genome = ""
    with open(filename, "r") as f:
        for line in f:
            if not line[0] == ">":
                genome += line.rstrip()
    return genome


genome = read_genome("probaGC.txt")
print(len(genome))

print(collections.Counter(genome))
