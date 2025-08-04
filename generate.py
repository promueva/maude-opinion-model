# Generating random networks

import random
import argparse
import sys
import time
import numpy as np

def random_partition(n):
    return np.random.dirichlet(np.ones(n))


def main():
    parser = argparse.ArgumentParser(description="Generating Random Networks")
    parser.add_argument("--agents", help="Number of Agents", type=int, required=True)
    parser.add_argument("--mode", help="Possible values: degroot, gossip or hybrid", required=True)
    args = parser.parse_args()

    num_agents = args.agents 

    seed = int(time.time_ns())  
    random.seed(seed)

    match args.mode:
        case "degroot":
            mode = '''
                    eq model = deGroot .
                    eq update(STATE, SETEDGE, AG) = update-dgroot-CB(STATE, SETEDGE, AG) .
                    '''
        case  "gossip":
            mode = '''
                    eq model = gossip .
                    eq update(STATE, SETEDGE, AG) = update-gossip(STATE, SETEDGE, AG) .
                   '''
        case "hybrid":
            mode = '''
                    eq model = hybrid .
                    eq update(STATE, SETEDGE, AG) = update-hybrid(STATE, SETEDGE, AG) .
                   '''
        case _:
            sys.exit(f'Illegal mode "{args.mode}"')

    # Influence matrix and initial believes 
    inf = [ random_partition(num_agents) for _ in range(num_agents)]
    belief = [random.random() for _ in range(num_agents)] 
    
    snodes = 'eq nodes = ' + \
             ' , '.join([f' < {i} : [ {x:,.3f} ] >' for i,x in enumerate(belief)]) + \
             ' . '
    
    sedges = '  eq edges = \n\t\t' + \
            ',\n\t\t'.join([ f'< ( {i} , {j} ) : {inf[i][j]:,.3f} >' for i in range(num_agents) for j in range(num_agents)]) + \
            ' .'
    
    smod = f'''
    
    load semantics .
    
    
    mod MODEL is
      pr REW-RELATION-UPDATE . 
      eq EPSILON = 0.001 .
      subsort Nat < Agent .
      
      
      vars S L R : State .
      
      op nodes   : -> SetOpinion .
      op edges   : -> SetEdge .
      op initnet : -> Network .
      
      {snodes}
      
      {sedges}
      
      eq initnet =  < nodes: nodes ; edges: edges >  .
      
      op init : -> State .
      eq init =  initnet  in step: 0 comm: 0 edge-sel: empty .
    endm'''
    
    
    stest = f'''
    
    mod TEST is
      pr MODEL .
      
      --- --------------------
      var STATE   : State .
      var SETEDGE : SetEdge .
      var AG      : Agent .
      --- --------------------
      
      eq moduleName = 'TEST .

      {mode}
    
    endm
    
    eof
    
    --- Example of use
    search  init =>* STATE such that consensus(STATE) .
    
    '''
    print(smod)
    print(stest)


if __name__ == "__main__":
    main()

