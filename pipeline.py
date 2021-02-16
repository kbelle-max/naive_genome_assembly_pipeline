#!/usr/bin/env python3
import random

test_ref="ACGATCGATGCTAGTCTATTACTGACTAGCTAGCATGCATCTAGCTATCGATCAGTCATCCTCTCTAGTCACTATCATTGCATGCTACGATCACTACTATGCATGTCGATCATCATTGCATGATCTAGCTACTACATGCATCATGCACTAGCATCATGATGTCATCTACTCAGTTGTGTACATGCTAGCTA"

def create_reads(ref,read_length=100,read_count=1000000):
    """returns generated reads as a 2d list 
    Params:
    ------
    ref: reference sequence as type string
    read_length: length of each read generated
    read_count: total read count
    Returns:
    reads as 2d list each read as a string

    ------
    """

    reads=[]
    while len(reads)<read_count:
        num= random.randint(0,len(ref))
        read=ref[num:num+read_length]
        if len(read)==read_length:
            reads.append(read)
    return reads

def assemble_genome(ref,reads):
    """returns a assembly as a 2d list 
    Params:
    ------
    ref: reference genome as string
    reads: list of read sequences as strings
    Returns:
    ------
    alignemnt of reads on reference genome as string
    """
    assembly=[ref]
    alignment=""
    for read in reads:
        start=ref.find(read)
        for idx in range(start+1):
            alignment+='N'
        alignment+=read
        while len(alignment)<len(ref):
            alignment+="N"
        assembly.append(alignment)
        alignment=""
    return assembly[::-1]

if __name__=='__main__':
    test_reads=create_reads(test_ref)
    assembly=assemble_genome(test_ref,test_reads)
    print(assembly)




