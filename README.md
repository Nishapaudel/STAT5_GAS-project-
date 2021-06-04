# STAT5_GAS-project-
This code first fetch the fasta sequence(chromosome specific fasta file ) and the get the co_cordinates of genes from gff/gtf file 
(here I have made Zebra_output.txt from gff file, can see as example)and find a pattern with python RegEx.
Finally, it generates the output file. A sample output file is also shown.
Particularly, I made this code for my friend for his PhD.
It fetches the match.group by this python RegEx TTC[TC][ATGCN][GA]GAA
Examples of sequences
TTCTGGGAA
TTCTGGGAA
TTCTGGGAA
TTCTGGGAA
TTCTGGGAA
TTCTGGGAA
TTCTGGGAA
TTCTGGGAA
TTCTGGGAA
TTCTGGGAA
TTCTGGGAA
TTCTGGGAA
TTCTGGGAA
TTCTGGGAA
TTCTGGGAA
TTCTGGGAA ... and few more
Requires three arguments a fasta file, a gene info file (bed file), chromosome number 
                                            _____________________________________________
                                            $  python3 chromosome.fa zebra_output.txt 7 
                                     
