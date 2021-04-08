'''
Created on Mar 21, 2021

@author: farif
'''

class KnowledgeBase:
    
    def __init__(self):
        #Rules        
        self.rules = []
        #Facts
        self.facts = []
        #Queries
        self.queries = []

    #Adding Fact/Facts
    def add_fact(self, fact):
        self.facts.append(fact)
    def add_facts(self, facts):
        self.facts.extend(facts)

    #Adding Rule/Rules
    def add_rule(self, rule):
        self.rules.append(rule)
    def add_rules(self, rules):
        self.rules.extend(rules)

    #Adding Query        
    def add_query(self, query):
        self.queries.append(query)

    #Printing KB
    def __str__(self):
        
        print_str = []
        
        print_str.append("---KB---")
        print_str.append("-F-")

        #Print Facts
        for f in self.facts:
            print_str.append(str(f) + ".")
        print_str.append("-R-")

        #Print Rules
        for r in self.rules:
            print_str.append(str(r) + ".")
        print_str.append("-Q-")
        
        #Print Queries
        for g in self.queries:
            print_str.append(str(g) + ".")
        
        print_str.append("--------")

        return '\n'.join(print_str)
    
