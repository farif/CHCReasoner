'''
Created on Mar 21, 2021

@author: farif
'''
from lark import Lark, Transformer, ParseError
from pathlib import Path

from data.Term import Term, OPS
from data.Sentence import AtomicSentence
from data.Rule import Rule
from data.KnowledgeBase import KnowledgeBase

rules_grammar = r"""
?start: kb

kb: rule+ 

rule: head ":-" body ["."]
      | head ["."] 
      | ":-" body ["."] 

?head: atom 
?body: atom ("^" atom)*

?atom: ID "(" term ")" | ID "(" term "," term ")" 
       | term OP term
       
?term:     constant
       | variable
        
!constant: string
        | NUMBER
        | sid
                
sid: "_id" "(" NUMBER ")"
        
string : ESCAPED_STRING        

OP: "=" |"!=" | ">=" | ">" | "<" | "<=" 

variable: ("?") ID

ID: (LETTER) ("_"|LETTER|DIGIT)*

COMMENT: /%.*/

%import common.ESCAPED_STRING
%import common.LETTER
%import common.DIGIT
%import common.NUMBER        
%import common.WS
%ignore WS 
%ignore COMMENT
"""
class TreeToRule(Transformer):
    
    def kb(self, args):
        kb = KnowledgeBase()
        
        for r in args:
            if r.is_head():
                kb.add_fact(r.head)
            elif r.is_clause():
                kb.add_rule(r)
            else:
                kb.add_query(r.body)

        return kb
                    
    def rule(self, args):
        #a rule clause
        if len(args) > 1:
            arule = Rule(args[0], args[1])
        else:
            arule = Rule(args[0], args[1:])
                    
        return arule
    
    def atom(self, args):
        if args[1] in OPS:
            predicate = args[1]
            t1 = args[0]
            t2 = args[2] 
            atom = AtomicSentence(predicate,[t1,t2])
        else:
            predicate = args[0]
            terms =  args[1:]                        
            atom = AtomicSentence(predicate, terms)                
        return atom

    def head(self, args):  
        return args
            
    def body(self, args):
        return args
        
    def term(self, term_value):
        t = Term(term_value)
        return t[0]
            
    def variable(self, var_name):
        return  "?" + var_name[0]

    def constant(self, const):
#        print("Constant", const)
        const = const[0].replace(".", "")
        return const

    def sid(self, instance):
        i = instance[0]
#        print("Symbol(Instance) ID:", i)
        return "_id(" + i + ")"

    def ID(self, value):
#        print("ID:", value)
        return value
        
def parse(s_input):
    
#    rules_grammar = open(grammar_file).read()
    parser = Lark(rules_grammar, parser='lalr', lexer='standard', transformer=TreeToRule())
    
    try:
        rule = parser.parse(s_input)            

    except ParseError as e:    
        print('Failed to Parse Formula, error:', e)

    return rule 
   
if __name__ == '__main__':
    data_read = Path('../examples/fwd-chaining-eg.txt').read_text()

    kb = parse(data_read)
    print(kb)