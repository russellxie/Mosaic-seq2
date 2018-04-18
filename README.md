# Mosaic-seq2

Mosaic-seq is the technique developed in Gary Hon Lab which allows acquisition of sgRNA information and transcriptome simultaneously from the same cell during single-cell RNA-seq. This is the pipeline used in Gary Hon Lab for Mosaic-seq analysis.

## Description
We've recently developed Mosaic-seq2, an improved version with several key changes to increase sensitivity and throughput.
1. We adopt the 10X Genomics single-cell RNA-seq platform and analysis pipeline.
2. We incorporated the CROP-seq design for sgRNA expression, which enables direct detection of sgRNAs without the need to barcode [1]. This design dramatically simplifies the construction of sgRNA plasmid libraries, and also eliminates the shuffling of sgRNAs and barcodes due to retroviral recombination [2, 3]. 
3. As in Perturb-Seq, we implement an enrichment PCR step to increase the detection efficiency of the sgRNAs in each single cell [4]. These improvements significantly increase the throughput of Mosaic-seq, which now allows simultaneous perturbation of hundreds to thousands of enhancers.


## Authors
Shiqi 'Russell' Xie

## Acknoledgement
The author thanks Dr. Jialei Duan for the help of writing part of the code.

## Requirements
Code tested in Python 3.6

## Reference
1. 	Thakore PI, D’Ippolito AM, Song L, et al (2015) Highly specific epigenome editing by CRISPR-Cas9 repressors for silencing of distal regulatory elements. Nat Methods 12:1143–1149
2. 	Xie S, Cooley A, Armendariz D, et al (2018) Frequent sgRNA-barcode Recombination in Single-cell Perturbation Assays. bioRxiv 255638
3. 	Hill AJ, McFaline-Figueroa JL, Starita LM, et al (2018) On the design of CRISPR-based single-cell molecular screens. Nat Methods 15:271–274
4. 	Dixit A, Parnas O, Li B, et al (2016) Perturb-Seq: Dissecting Molecular Circuits with Scalable Single-Cell RNA Profiling of Pooled Genetic Screens. Cell 167:1853–1866.e17
