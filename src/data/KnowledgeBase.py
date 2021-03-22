'''
Created on Mar 21, 2021

@author: farif
'''

class KnowledgeBase:
    
    def __init__(self):
        
        self.rules = []
        self.facts = []
        self.queries = []

    #Facts
    def add_fact(self, fact):
        self.facts.append(fact)

    def add_facts(self, facts):
        self.facts.extend(facts)

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_rules(self, rules):
        self.rules.extend(rules)
        
    def add_query(self, query):
        self.queries.append(query)

    def __str__(self):
        print_str = []
        
        print_str.append("---KB---")
        #Print Facts
        for st in self.facts:
            print_str.append(str(st) + ".")
        #Print Rules
        for st in self.rules:
            print_str.append(str(st) + ".")
        #Print Queries
        for st in self.queries:
            print_str.append(":-" + str(st))

        print_str.append("--------")

        return '\n'.join(print_str)

    def is_unificable(self, a1, a2):
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

    def unify(self, a1, a2, binding):
        if binding is None:
            return None
                 
        for (t1,t2) in zip(a1.terms, a2.terms):
            binding = t1.unify(t2, binding)
         
        return binding