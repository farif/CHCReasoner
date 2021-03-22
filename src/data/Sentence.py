'''
Created on Mar 21, 2021

@author: farif
'''
from data.Term import Term, OPS

class AtomicSentence:
    
    #Predicate
    pred = None
    #Arguments contain One or more Terms
    terms = []
    
    def __init__(self, predicate, args):
        self.pred = predicate
        self.terms = [Term(a) for a in args]
    #No Type Checker yet.
    
    #Unary Predicate
    def is_unary(self):
        return len(self.terms) == 1
    #Binary Relation
    def is_binary(self):
        return len(self.terms) == 2
    #Constraint Relation
    def is_constraint(self):
        return self.pred in OPS
    
    # Equality
    def __eq__(self, cmp):
        #Predicate are different
        if (self.pred != cmp.pred or len(self.terms) != len(cmp.terms)): 
            return False
        #recursive comparison.
        return all([x == y for (x, y) in zip(self.terms, cmp.terms)])
            
    # Hash for Dictionaries
    def __hash__(self):
        return hash(self.pred) and hash(str(self.terms))

    # Representation for humans
    def __repr__(self):
        print_terms = ",".join([str(a) for a in self.terms])
        if self.pred in OPS:
            op = " " + str(self.pred) + " " 
            return op.join([str(a) for a in self.terms])

        return str(self.pred) + "("+ print_terms +")"
    
    #Operator has to be a statement
#     def get_op(self):
#         if self.pred == '=' :
#             return operator.eq
#         if self.pred == '!=':
#             return operator.ne
#         if self.pred == '>':
#             return operator.gt
#         if self.pred == '>=':
#             return operator.ge
#         if self.pred == '<':
#             return operator.lt
#         if self.pred == '<=':
#             return operator.le
    
    #renaming all variables
    def std_vars(self,bind_dict = {}):
        global MAX_VAR
        
        for index, term in enumerate(self.terms):
            
            if term.is_var:
                if not term.tid in bind_dict:
                    bind_dict[term.tid] = term.std_vars()
                self.terms[index] = Term(bind_dict[term.tid])
        
        return bind_dict
    
    def get_vars(self):
        all_vars = []
        for term in self.terms:
            if term.is_var():
                all_vars.append(term)
        return all_vars


    def is_unifiable(self, cmp):
        if self.pred != cmp.pred:
            return False 
        if len(self.terms) != len(cmp.terms):
            return False
        
        for (t1,t2) in zip(self.terms, cmp.terms):
            if (t1.is_unifiable(t2)):
                continue
            else:
                False
        return True

    def unify(self, cmp, rho):
        if rho is None:
            return None
                
        for (t1,t2) in zip(self.terms, cmp.terms):
            rho = t1.unify(t2, rho)
        
        return rho

    def subst(self, rho):
        new_terms = []

        for t in self.terms:
            if t in rho:
                t  = rho[t]
            new_terms.append(t)
            
        self.terms = new_terms
        