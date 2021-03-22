# CHC Reasoner 
A simple forward chaining algorithm implementation.

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
`./Driver.py`

![](resources/recorded-syslite.gif)

## Supported Algorithms:
The tool currently supports a list of algorithms that can be invoked with `-a` option:

1. Forward Chaining Algorithm `fwc`  
2. Backward Chaining Algorithm `bcw` [Not supported yet]

##References:

