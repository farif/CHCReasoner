'''
Created on March 21, 2021

@author: farif
'''
from data.Sentence import AtomicSentence

#Utility Function
def subst(a, rho):
    new_terms = []

    for t in a.terms:
        if t in rho:
            t  = rho[t]
        new_terms.append(t)

    a = AtomicSentence(a.pred, new_terms)
    
    return a

#Does two statements unify
def is_unificable(a1, a2):
    
    if a1.pred != a2.pred:
        return False 
    if len(a1.terms) != len(a2.terms):
        return False
    
    for (t1,t2) in zip(a1.terms, a2.terms):
        if (t1.is_unifiable(t2)):
            continue
        else:
            False
            
    return True

#Unify two statement given a knowledge base
def unify(a1, a2, binding):
    
    if binding is None:
        return None
             
    for (t1,t2) in zip(a1.terms, a2.terms):
        binding = t1.unify(t2, binding)
     
    return binding

        