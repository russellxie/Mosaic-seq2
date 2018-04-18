#!/usr/bin/env python3
import numpy as np
import scipy
import argparse
from scipy.special import factorial
from scipy.stats import multinomial

def null_probability_helper(x, n):
    n_0 = np.size(np.where(x > 0))
    p = np.power((1/n), np.sum(x)) * factorial(n, exact=True) / factorial((n-n_0), exact=True)
    return p

def probability_helper(x, B, B_0):
    model_probability = []
    #caculate the null model, in which there is no sgRNA
    model_probability.append(null_probability_helper(x, B))
    
    p_model = []
    for i in np.arange(0, B_0):
        current = 1
        p_list  = np.array([])
        for j in np.arange(0, i+1):
            current = current * 0.9        
            p_list = np.append(p_list, current)
        p_model.append((p_list / sum(p_list)))

        #compute the multinomial probability
        p_multinomial = multinomial.pmf(x[0:i+1], np.sum(x[0:i+1]), p_model[i])

        #compute null probability for other datapoints
        p_remainder   = null_probability_helper(x[i+1:], (B-i-1))

        #compute the final pval
        pval = p_multinomial * p_remainder

        model_probability.append(pval)
    
    return model_probability

def calculate_probability(x):
    #define parameters
    B   = np.size(x)
    B_0 = np.size(np.where(x > 0))

    #caculate the null model, in which there is no sgRNA
    model_probabilities = null_probability_helper(x, B)

    #caculate the probability
    model_probabilities = probability_helper(x, B, B_0)

    #get the maximum probability
    #if this events is not 2X as likely as null, use the null
    min_prob = np.max(model_probabilities)
    min_prob_index = np.argmax(model_probabilities)

    if (min_prob_index > 0 and (min_prob / model_probabilities[0]) < 2):
        min_prob_index = 1
        
    model_index = min_prob_index
    
    return(model_index)

def print_output(input):
    cell_bc = input[0]
    sgRNA   = input[1]
    umi     = input[2]
    i       = input[3]

    print(cell_bc, end='\t', file=output_fh)
    print(i, end='\t', file=output_fh)
    print(';'.join(sgRNA[0:i]), end='\t', file=output_fh)
    print(';'.join(umi[0:i]), end='\n', file=output_fh)

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', dest='input', required=True,
                    type=str,
                    help='specify an input file \
                    (output of summarize_sgRNA.py)')
parser.add_argument('-o', '--output', dest='output', required=False,
                    help='specify an output file')

args = parser.parse_args()
input_file  = args.input
output_file = args.output

input_fh  = open(input_file, 'r')
output_fh = open(output_file, 'w')

#define parameters
cell_bc_list   = []
num_sgRNA_list = np.array([])
sgRNAs         = []
umis           = []

#read the line
for line in input_fh:
    cell_bc    = line.strip().split('\t')[0]
    num_sgRNA  = line.strip().split('\t')[2]
    sgRNA_list = line.strip().split('\t')[3].split(';')
    umi_list   = line.strip().split('\t')[5].split(';')
        
    cell_bc_list.append(cell_bc)
    num_sgRNA_list = np.append(num_sgRNA_list, num_sgRNA)
    sgRNAs.append(sgRNA_list)
    umis.append(umi_list)

#get the maximum sgRNA number
max_sgRNA_num = np.amax(num_sgRNA_list.astype(int))

#print(umis[1])
model_index_list = []
for line in umis:
    line_int = np.array(line).astype(int)

    line_int = np.pad(line_int, (0, (max_sgRNA_num - np.size(line))), 'constant')
    model_index_list.append(calculate_probability(line_int))

for i in zip(cell_bc_list, sgRNAs, umis, model_index_list):
    print_output(i)
    
output_fh.close()
