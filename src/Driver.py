#!/usr/bin/env python3
# encoding: utf-8
'''
@Program: CHCReasoner is a simple forward chaining algorithm implementation.
@License: Use of this source code is governed by a BSD 3-Clause License that can be found in the LICENSE file.
@Contact: fareed.arif@yahoo.com
'''
from algorithms.Reasoner import forward_chaining, backward_chaining
from parser.Parser import parse

from pathlib import Path
import optparse

#Process command line arguments.
def read_args():
    
    p = optparse.OptionParser()

    p.add_option('--file', '-i', default="examples/fwd-chaining-eg.txt")
    p.add_option('--algo', '-a', default="fwc")
    
    #Query is not provided yet
    p.add_option('--query', '-q')
    
    options, _ = p.parse_args()

    print('Input: %s'% options.file)
    
    return (options.file, options.algo)

#Program Driver Method.
if __name__ == '__main__':
    
    #Read Input Arguments
    (ifile, algo) = read_args()
    
    try:        
        #Read input Data
        data_read = Path(ifile).read_text()

        #Parse Data and Initialize KB
        kb = parse(data_read)
        
        #Print Initial KB
        print(kb)
    
        #Supported Algorithm
        if algo == "fwc":
            #Invoke Forward Chaining Algorithm
            eFacts = forward_chaining(kb.facts, kb.rules)
            #Entailed Factss
            print('E. Facts: ', eFacts)
            print("--------")
            
        else:
            #Nor Supported ye.
            query = None
            backward_chaining(query, kb.facts, kb.rules)

    except FileNotFoundError as e:
        print(str(e))
    
        
