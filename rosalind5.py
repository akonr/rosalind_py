from Bio import SeqIO
from Bio.SeqUtils import GC
import collections


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
