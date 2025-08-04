# Generating random networks

import random
import argparse


def main():
    parser = argparse.ArgumentParser(description="Generating Random Networks")
    parser.add_argument("--agents", help="Number of Agents", type=int, required=True)
    args = parser.parse_args()

    num_agents = args.agents 

    # Influence matrix and initial believes 
    inf = [[random.random() for _ in range(num_agents)] for _ in range(num_agents)]
    belief = [random.random() for _ in range(num_agents)] 
    
    # 1.0 in the diagonal 
    for i in range(num_agents):
        inf[i][i] = 1.0 
    
    snodes = 'eq nodes = ' + \
             ' , '.join([f' < {i} : [ {x:,.3f} ] >' for i,x in enumerate(belief)]) + \
             ' . '
    
    sedges = '  eq edges = \n\t\t' + \
            ',\n\t\t'.join([ f'< ( {i} , {j} ) : {inf[i][j]:,.3f} >' for i in range(num_agents) for j in range(num_agents)]) + \
            ' .'
    
    smod = f'''
    
    load ./semantics-gossip .
    
    
    mod MODEL is
      pr GOSSIP . 
      eq EPSILON = 0.05 .
      subsort Nat < Agent .
      
      
      vars S L R : State .
      
      op nodes   : -> SetOpinion .
      op edges   : -> SetEdge .
      op initnet : -> Network .
      
      {snodes}
      
      {sedges}
      
      eq initnet =  < nodes: nodes ; edges: edges >  .
      
      op init : -> State .
      eq init =  initnet  in step: 0 comm: 0 strat: empty .
    endm'''
    
    
    stest = f'''
    
    mod TEST is
      pr MODEL .
      
      --- --------------------
      var STATE   : State .
      var SETEDGE : SetEdge .
      var AG      : Agent .
      --- --------------------
    endm
    
    eof
    
    --- Example of use
    search  init =>* STATE such that consensus(STATE) .
    
    '''
    print(smod)
    print(stest)


if __name__ == "__main__":
    main()

