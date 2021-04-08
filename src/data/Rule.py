'''
Created on Mar 21, 2021

@author: farif
'''

# Var is a class of for variables
#
# @field id: a 
# @field assignment : an assignment (True, False or None)
#

# Unique global Constant#
#identifier = 0

#Term := Variable | Lit
#Lit := "String" | Boolean | Number
#class Lit:
#import types
from data.Sentence import AtomicSentence
MAX_VAR = 0
#?How to deal with Instance
class Rule:
    #Zero or Atomic sentence
    head = None
    #Zero or Atomic or Conjunction of Sentences
    body = None
    
    b_count = 0
    
    def __init__(self, lhs, rhs):
        
        self.head = lhs
        
        if isinstance(rhs, list):
            self.body = rhs
        else:
            self.body = [rhs]
#            self.body_count = 1
        self.b_count = len(self.body)

#        self.t_isvar = t_id.startswith('?')
 
    def is_fact(self):
        return (not self.body) and len(self.head.get_vars()) == 0
    #Variables exist in head are universally quantified.
    def univ_vars(self):
        return self.head.get_vars()
    
    def ex_vars(self):
        h_vars = set(self.head.get_vars())
        b_vars = []
        
        for atom in self.body:     
            b_vars.append(atom.get_vars())
        
        return list(set(h_vars) & set(b_vars))
    #Variables exist not in head but body are existentially quantified
    def is_head(self):
        return (not self.body)

    def is_body(self):
        return (not self.head)

    def dec_count(self):
#        if self.body_count > 0:
        self.b_count -= 1
    
    def revert_count(self):
        self.b_count = len(self.body)

    def is_enabled(self):
        return self.b_count <= 0
    
    def is_clause(self):
        return (self.head and self.body)

    def subst(self, rho):
        new_atom = []
        for atom in self.body:
            terms = atom.subst(rho)
            n = AtomicSentence(atom.pred, terms)
            new_atom.append(n)
            n_vars = n.get_vars()
            print(atom, new_atom, len(n_vars))
        print(new_atom)

    def std_vars(self):
        binding = {}
        self.head.std_vars(binding)
        for b in self.body:
            b.std_vars(binding)

    def __eq__(self, cmp):
        return self.head == cmp.head and all([x == y for (x,y) in zip(self.body == cmp.body)])

    # Hash for Dictionaries
    def __hash__(self):
        return hash(self.head) and hash(str(self.body))

    # Representation for humans
    def __repr__(self):
        IMPLIES = " :- "
        #Head/Fact
        if self.head and not self.body:
            return str(self.head) 
        #Query
        if self.body and not self.head:
            return  ' ^ '.join(str(b) for b in self.body)
        #Rules
        return str(self.head) + IMPLIES + ' ^ '.join(str(b) for b in self.body)