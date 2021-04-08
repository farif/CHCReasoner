# Constrained Horn Clause (CHC) Reasoner: 
A simple forward chaining algorithm implementation.

<p align="justify">
1) Forward Chaining: Given a knowledge base that contains rules and facts, a forward-chaining algorithm uses these facts for the matching and firing of existing rules. A rule matching criteria is to unify premises with existing and entailed facts, if all premises of a rule hold,  a consequence of the rule gets added to the entailed facts.
</p>

## Build
Run commands on Terminal:
0. Setup Virtual Environment: `sudo apt-get install python3-venv`
1. Build: `./tool-setup`
   * Continue? [Y]es/[N]o: Y 
   * only required once to setup the reasoner
   
## Test
1. Enable execution: `source env/bin/activate`
   * Required before executing the tool on a new terminal.  
2. Run: `./src/Driver.py --help`
3. Disable execution: `deactivate`
    
## Usage

A default example file is added to test the reasoner (fwd-chaining-eg.txt). 
`./src/Driver.py`

![](https://github.com/farif/CHCReasoner/blob/main/install_reasoner.gif)


## Supported Algorithms
The tool currently supports a list of algorithms that can be invoked with `-a` option:

1. Forward Chaining Algorithm `fwc`  
![](https://github.com/farif/CHCReasoner/blob/main/demo/fwc-running.gif)

2. Backward Chaining Algorithm `bcw` [Not supported yet]

3. DLV Rewrite
![](https://github.com/farif/CHCReasoner/blob/main/demo/fwc-dlv-eg.gif)

## References
1. Mattos, Nelson Mendonça. An approach to knowledge base management. Vol. 513. Berlin: Springer, 1991.
2. Russell, S. J., and P. Norvig. "Artificial intelligence: a modern approach/Stuart J." Russell and Peter Norvig contributing writers, Ernest Davis...[et al.].
3. The slide notes: https://www.ics.uci.edu/~kkask/Fall-2017%20CS271/slides/06-prop-logic.pdf