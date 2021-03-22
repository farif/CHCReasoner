'''
Created on Mar 21, 2021

@author: farif
'''
import copy
from data.KnowledgeBase import KnowledgeBase

#Forward chaining
def forward_chaining(facts, rules):
    
    #Initialize KB
    kb = KnowledgeBase()
    
    kb.add_facts(facts)
    kb.add_rules(rules)
    
    #State := Agenda + Working Memory
    agenda = copy.deepcopy(facts)
    w_memory = copy.deepcopy(rules)        
    
    entailedFacts = []
    binding = {}
    
    while len(agenda) > 0:
        #Select a fact
        p_fact = agenda.pop()
        #Enumerate over rules.
        for w_rule in w_memory:
            #Enumerate over atoms in body of rule
            for antecedent in w_rule.body:
                if antecedent.is_unifiable(p_fact):
                    kb.unify(antecedent, p_fact, binding)

                antecedent.subst(binding)
                #1. Evaluate Expression with Operator
                if antecedent.is_constraint():
                    output = eval(str(antecedent))
                    if output:
                        w_rule.body.remove(antecedent)
                    else:
                        continue
                #2. Antecedent fact is true
                elif antecedent in kb.facts: 
                    w_rule.body.remove(antecedent)
            #If premise is true then add consequent fact
            if w_rule.is_head():
                w_rule.head.subst(binding)
                agenda.append(w_rule.head)
                entailedFacts.append(w_rule.head)
                w_memory.remove(w_rule)
    
    return entailedFacts[::-1]            

# Backward chaining
def backward_chaining(query, facts, rules): 
    print("NOT supported yet.")
