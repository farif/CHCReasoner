'''
Created on Mar 19, 2021

@author: farif
'''
from data.Sentence import AtomicSentence
from data.Rule import Rule

from data.KnowledgeBase import KnowledgeBase
from algorithms.Reasoner import forward_chaining
from parser.Parser import parse
from pathlib import Path

if __name__ == '__main__':
    
    kb = KnowledgeBase()
 
    f = AtomicSentence("Person", ["_id(1)"]);
    f1 = AtomicSentence("Person", ["_id(2)"]);
    f2 = AtomicSentence("child", ["_id(1)", "_id(2)"]);
    f3 = AtomicSentence("has_age", ["_id(2)", 15]);
      
    kb.add_facts([f,f1,f2,f3])
      
    head = AtomicSentence("dependent", ["?taxpayer", "?child"]);
  
    sub_g = AtomicSentence("child", ["?taxpayer", "?child"]);
    sub_g1 = AtomicSentence("has_age", ["?child", "?age"]);
    sub_g2 = AtomicSentence("<", ["?age", 18]);
      
    one_rule = Rule(head, [sub_g, sub_g1, sub_g2])
      
    kb.add_rule(one_rule)

    data_read = Path('../examples/fwd-chaining-eg.txt').read_text()
 
    kb = parse(data_read)
    
    print(kb)

    eFacts = forward_chaining(kb.facts, kb.rules)
    
    print('E. Facts: ', eFacts)
    print("--------")

    