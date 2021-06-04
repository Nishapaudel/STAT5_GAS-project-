# import all modules
import sys
import os
import re

#setting up all variables
#fasta_file = '/home/nisha/Downloads/Danio_rerio.GRCz11.dna.chromosome.17.fa'
fasta_file = sys.argv[1]
#gene_file = 'Zebra_output.txt'  
# this file all gene cordinates that i extract from gtf file 
gene_file =sys.argv[2]

chromosome_number =sys.argv[3]
#-------------------------------------Gets string of the sequence of chromosome ------------------------------------#
def fetch_seq(fasta_file):
    ''' ###### fetching the  seq of a chromosome and find the Gamma Activated sequence where the STAT5 binds
        Requires three arguments a fasta file, a gene info file (bed file), chromosome number 
                                            $  python3 chromosome.fa zebra_output.txt 7 '''
    
    print("Fetchning the sequence from " + fasta_file)
    seq = ''
    try:
        fa = open(fasta_file)
        for line in fa:
            if line.startswith('>'):
                continue
            else:
                seq += line.strip().upper()
    
    except:
        print('FASTA file error')
        sys.exit()
    return seq

# ---------------------------GAS in promoter of zebra fish--------------------------------------------------------
sequence = fetch_seq(fasta_file)
print("Fetchning the promoter region coordinates from " + gene_file)

f_out = open('25Gamma_activated_sequence_profile.bed','w')
print('count', 'match.group', 'match.start', 'match.end', 
'chromosome', 'gene', 'strand','start_gene', 'end_gene',
'promoter_start', 'promoter_end',sep ='\t',file=f_out)
count = 0
    
    
fh = open(gene_file)
for i in fh:
    columns = i.strip().split('\t')
    chrom = columns[0]
    start = int(columns[2])
    if start < 5000:
        continue
    end = int(columns[3])
    if end < 5000:
        continue
    strand = columns[4]
    gene = columns[5]
  
    if chrom == chromosome_number:#make change on chromosome number
        if strand == '+':
            promoter_start = start - 5000 # u can chage this 10000
            promoter_end = promoter_start + 5000
            
        else:
            promoter_start = end - 5000 # this too
            promoter_end = promoter_start + 5000
           
        for match in re.finditer("TTC[TC][ATGCN][GA]GAA", sequence[promoter_start:promoter_end]):
            count += 1
   
            print(count, match.group(), match.start(), match.end(), 
            chrom, gene, strand,start, end,promoter_start, 
            promoter_end,sep ='\t',file = f_out)
fh.close()
f_out.close()     

print(' Coooooooooooool !!! ;) The program has ended ')