# Mosaic-seq2

Mosaic-seq is the technique developed in Gary Hon Lab which allows acquisition of sgRNA information and transcriptome simultaneously from the same cell during single-cell RNA-seq. This is the pipeline used in Gary Hon Lab for Mosaic-seq analysis.

## Description
We've recently developed Mosaic-seq2, an improved version with several key changes to increase sensitivity and throughput.
1. We adopt the 10X Genomics single-cell RNA-seq platform and analysis pipeline.
2. We incorporated the CROP-seq design for sgRNA expression, which enables direct detection of sgRNAs without the need to barcode [6]. This design dramatically simplifies the construction of sgRNA plasmid libraries, and also eliminates the shuffling of sgRNAs and barcodes due to retroviral recombination [7, 8]. 
3. As in Perturb-Seq, we implement an enrichment PCR step to increase the detection efficiency of the sgRNAs in each single cell [4]. These improvements significantly increase the throughput of Mosaic-seq, which now allows simultaneous perturbation of hundreds to thousands of enhancers.


## Authors

## Requirements

## Reference
