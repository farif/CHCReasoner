#!/usr/bin/env python3
# encoding: utf-8
'''
@Program: Reasoner is a simple forward chaining algorithm implementation.
@License: Use of this source code is governed by a BSD 3-Clause License that can be found in the LICENSE file.
@Contact: fareed.arif@yahoo.com
'''
from algorithms.Reasoner import forward_chaining, backward_chaining
from parser.Parser import parse

from pathlib import Path
import optparse

def read_args():
    p = optparse.OptionParser()

    p.add_option('--file', '-i', default="examples/fwd-chaining-eg.txt")
    p.add_option('--algo', '-a', default="fwc")
    
    #Query provided for backward reasoning
    p.add_option('--query', '-q')
    
    options, _ = p.parse_args()

    print('Input: %s'% options.file)
    return (options.file, options.algo)

if __name__ == '__main__':
    
    (ifile, algo) = read_args()
    
    data_read = Path(ifile).read_text()
 
    kb = parse(data_read)
    
    print(kb)

    if algo == "fwc":
        entailedFacts = forward_chaining(kb.facts, kb.rules)
        print(set(entailedFacts))
    else:
        query = None
        backward_chaining(query, kb.facts, kb.rules)
        
