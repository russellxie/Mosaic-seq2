# Mosaic-seq2

## Author
Shiqi 'Russell' Xie
## Acknoledgement
The author thanks Dr. Jialei Duan for his helpful discussion and input.
## Requirements
Code tested in Python 3.6
## Introduction
Mosaic-seq is the technique developed in Gary Hon Lab which allows acquisition of sgRNA information and transcriptome simultaneously from the same cell during single-cell RNA-seq [1]. We've recently developed Mosaic-seq2, an improved version with several key changes to increase sensitivity and throughput.
1. We adopt the 10X Genomics single-cell RNA-seq platform and analysis pipeline.
2. We incorporated the CROP-seq design for sgRNA expression, which enables direct detection of sgRNAs without the need to barcode [1]. This design dramatically simplifies the construction of sgRNA plasmid libraries, and also eliminates the shuffling of sgRNAs and barcodes due to retroviral recombination [2, 3]. 
3. As in Perturb-Seq, we implement an enrichment PCR step to increase the detection efficiency of the sgRNAs in each single cell [4]. These improvements significantly increase the throughput of Mosaic-seq, which now allows simultaneous perturbation of hundreds to thousands of enhancers.

## Overview of the pipeline
## Description
### Overview of the pipeline 
![alt text](https://github.com/russellxie/Mosaic-seq2/blob/master/MISC/Flowchart-01.png "Logo Title Text 1")

1. Use extract_sgRNA_from_reads.py to extract possible sgRNA and cell barcode from fastq files
Example:
```bash
./extract_sgRNA_from_reads.py\
	-i FASTQ1.gz FASTQ2.gz\
	-b barcodes.tsv\
	-r known_sgRNA.txt\
	-t 30\
	-m 1\
	-o sgRNA_cell-bc.summary.txt
```
- barcodes.tsv is the direct output file from the 10X cellranger pipeline.
- known_sgRNA.txt contains known list of sgRNAs, in the following fomrat:
```
AAAAAACGTCCTTCGAACT
AAAAACACCCCAGGAGGGT
AAAAACATACGTATTTCAC
AAAAACGAGAAAAGGCCAG
AAAAACGCCTATAGCAATG
```
- '-t' specifies the threading number.
- '-m' specified the mismatches allowed. Default is 1.

2. Use 'summarize_sgRNA.py' to summarize the sgRNA to each cell.
Example:
```bash
./summarize_sgRNA.py\
	-i sgRNA_cell-bc.summary.txt\
	-o sgRNA_count.txt
```

## Reference
1. 	Xie S, Duan J, Li B, et al (2017) Multiplexed Engineering and Analysis of Combinatorial Enhancer Activity in Single Cells. Mol Cell 66:285–299.e5
2. 	Thakore PI, D’Ippolito AM, Song L, et al (2015) Highly specific epigenome editing by CRISPR-Cas9 repressors for silencing of distal regulatory elements. Nat Methods 12:1143–1149
3. 	Xie S, Cooley A, Armendariz D, et al (2018) Frequent sgRNA-barcode Recombination in Single-cell Perturbation Assays. bioRxiv 255638
4. 	Hill AJ, McFaline-Figueroa JL, Starita LM, et al (2018) On the design of CRISPR-based single-cell molecular screens. Nat Methods 15:271–274
5. 	Dixit A, Parnas O, Li B, et al (2016) Perturb-Seq: Dissecting Molecular Circuits with Scalable Single-Cell RNA Profiling of Pooled Genetic Screens. Cell 167:1853–1866.e17
