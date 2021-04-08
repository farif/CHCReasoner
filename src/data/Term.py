'''
Created on Mar 21, 2021

@author: farif
'''

OPS = ['=','!=','>','>=','<','<=']
MAX_VAR = 0

class Term:
    
    tid = None
    is_var = False
    
    def __init__(self, tid):
        self.tid = str(tid)
 
    def is_var(self):
        return self.tid.startswith('?')

    def is_constant(self):
        return not self.tid.startswith('?')

    def std_vars(self):
        global MAX_VAR
        MAX_VAR += 1
        
        return self.tid + str(MAX_VAR)

    def is_unifiable(self, cmp):
        return (self.is_var() and cmp.is_constant()) or (self.is_constant() and cmp.is_var())
    
    def unify(self, var_term, bind):

        if self.is_constant() and var_term.is_var():
            bind[Term(self.tid)] = var_term
            
        elif self.is_var() and var_term.is_constant():
            bind[Term(self.tid)] = var_term
            
        return bind
        
    # Equality
    def __eq__(self, cmp):
        return self.tid == cmp.tid or (self.is_var() and cmp.is_var())

    # Hash for Dictionaries
    def __hash__(self):
        return hash(self.tid)

    # Representation for humans
    def __repr__(self):
        return str(self.tid)