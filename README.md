# Mosaic-seq2

## Description
Here we introduce Mosaic-seq2, with several key changes to increase sensitivity and throughput.
1. We adopt the 10X Genomics single-cell RNA-seq platform, which enables the generation of 80,000 single-cell RNA-Seq libraries in a single run. 
2. We incorporated the CROP-seq design for sgRNA expression, which enables direct detection of sgRNAs without the need to barcode [6]. This design dramatically simplifies the construction of sgRNA plasmid libraries, and also eliminates the shuffling of sgRNAs and barcodes due to retroviral recombination [7, 8]. Third, as in Perturb-Seq, we implement an enrichment PCR step to increase the detection efficiency of the sgRNAs in each single cell [4]. These improvements significantly increase the throughput of Mosaic-seq, which now allows simultaneous perturbation of hundreds to thousands of enhancers.


## Authors

## Requirements

## Reference
