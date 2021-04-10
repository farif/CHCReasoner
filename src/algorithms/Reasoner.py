'''
Created on Mar 21, 2021

@author: farif
'''

import copy
from data.KnowledgeBase import KnowledgeBase
from utils.Util import subst, unify

#Forward chaining algorithm
def forward_chaining(facts, rules):
    
    #Initialize KB
    kb = KnowledgeBase()
    
    #Adding facts and rules to the KB
    kb.add_facts(facts)
    kb.add_rules(rules)
    
    #working memory
    wm = []
    
    #Standardize and copy rules to working memory
    for r in rules:
        r.std_vars()         
        wm.append(r)

    #State := Agenda + Working Memory
    agenda = copy.deepcopy(facts)
    binding = {}
    eFacts = []
    
    while len(agenda) > 0:
        #Select a fact
        pfact = agenda.pop()
        
        #select a rule from memory
        for r in wm:
            #iterate over the body of a rule
            for a_premise in r.body:
                #matching
                if a_premise.is_unifiable(pfact):
                    #Unify and update binding
                    unify(a_premise, pfact, binding)
                #Apply substitution
                w_atom = subst(a_premise, binding)
            
                #1. Evaluate Expression with Operator
                if w_atom.is_cons():
                    output = eval(str(w_atom))
                    if output:
                        r.dec_count()
                    else:
                        continue
                #2. Antecedent fact is true
                elif (w_atom in kb.facts) or (w_atom in eFacts): 
                    r.dec_count()
     
                # Fire rule.
                if r.is_enabled():
                    conseq = subst(r.head, binding)
                    if not conseq in eFacts:
                        agenda.append(conseq)
                        eFacts.append(conseq)
                    break;
    
#     goals = []
# 
#     for q in queries:
#         for qatom in q.body:
#             for ef in eFacts:                
#                 if qatom.is_unifiable(ef):
#                     eg = subst(ef, binding)
#                     goals.append(eg)
#     
#     if len(goals) > 0:
#         print('G:', goals)
        
    return eFacts[::-1]            

# Backward chaining algorithm
def backward_chaining(query, facts, rules): 
    print("NOT supported yet.")

