# Constrained Horn Clause (CHC) Reasoner: 
A simple forward chaining algorithm implementation.


1) Forward Chaining: In this we are given a knowledge base which includes the rules and the facts. The basic idea behind forward chaining is that
	from facts we go through the rules and see which of them can be fired. The rule which is fired,its consequence is added to the list of facts. Then the collective list of facts are then used to fire further rules.
	
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
`./src/Driver.py --help`

![](demo/fwc-running.gif)

## Supported Algorithms
The tool currently supports a list of algorithms that can be invoked with `-a` option:

1. Forward Chaining Algorithm `fwc`  
2. Backward Chaining Algorithm `bcw` [Not supported yet]

## References
1. Mattos, Nelson Mendonça. An approach to knowledge base management. Vol. 513. Berlin: Springer, 1991.
2. Russell, S. J., and P. Norvig. "Artificial intelligence: a modern approach/Stuart J." Russell and Peter Norvig contributing writers, Ernest Davis...[et al.].
3.  https://www.ics.uci.edu/~kkask/Fall-2017%20CS271/slides/06-prop-logic.pdf
4. Deductive database system, DLV user manual: http://www.dlvsystem.com/html/DLV_User_Manual.html

